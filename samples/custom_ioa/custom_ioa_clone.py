r"""Custom IOA duplicator.

 ______                         __ _______ __         __ __
|      |.----.-----.--.--.--.--|  |     __|  |_.----.|__|  |--.-----.
|   ---||   _|  _  |  |  |  |  _  |__     |   _|   _||  |    <|  -__|
|______||__| |_____|________|_____|_______|____|__|  |__|__|__|_____|

 ____                     __                           ______   _____   ______
/\  _`\                  /\ \__                       /\__  _\ /\  __`\/\  _  \
\ \ \/\_\  __  __    ____\ \ ,_\   ___     ___ ___    \/_/\ \/ \ \ \/\ \ \ \L\ \
 \ \ \/_/_/\ \/\ \  /',__\\ \ \/  / __`\ /' __` __`\     \ \ \  \ \ \ \ \ \  __ \
  \ \ \L\ \ \ \_\ \/\__, `\\ \ \_/\ \L\ \/\ \/\ \/\ \     \_\ \__\ \ \_\ \ \ \/\ \
   \ \____/\ \____/\/\____/ \ \__\ \____/\ \_\ \_\ \_\    /\_____\\ \_____\ \_\ \_\
    \/___/  \/___/  \/___/   \/__/\/___/  \/_/\/_/\/_/    \/_____/ \/_____/\/_/\/_/

                                                 ______ __
                                                |      |  |.-----.-----.-----.----.
                                                |   ---|  ||  _  |     |  -__|   _|
                                                |______|__||_____|__|__|_____|__|

                                                 CrowdStrike FalconPy v.1.1
"""
from argparse import ArgumentParser, RawTextHelpFormatter
from falconpy import CustomIOA
from tabulate import tabulate


class Color:  # pylint: disable=R0903
    """Class to represent the text color codes used for terminal output."""

    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    MAGENTA = "\033[35m"
    BLUE = "\033[34m"
    LIGHTBLUE = "\033[94m"
    GREEN = "\033[32m"
    LIGHTGREEN = "\033[92m"
    LIGHTYELLOW = "\033[93m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    LIGHTRED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def consume_arguments():
    """Consume any user provided arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-n", "--nocolor",
                        help="Disable color output",
                        required=False,
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-b", "--base_url",
                        help="Base URL",
                        required=False,
                        default="auto"
                        )
    parser.add_argument("-t", "--table_format",
                        help="Tabular display format",
                        required=False,
                        default="fancy_grid"
                        )
    srch = parser.add_argument_group("search arguments")
    srch.add_argument("-f", "--filter",
                      help="String to filter results (IOA rule group name)",
                      required=False,
                      default=None
                      )
    act = parser.add_argument_group("action arguments")
    act.add_argument("-c", "--clone",
                     help="Clone all IOA rule group matches to new rule groups",
                     required=False,
                     action="store_true",
                     default=False
                     )
    act.add_argument("-d", "--delete",
                     help="List of rule group IDs to delete (comma-delimit)",
                     required=False,
                     default=None
                     )
    req = parser.add_argument_group("required arguments")
    req.add_argument("-k", "--falcon_client_id",
                     help="CrowdStrike Falcon API Client ID",
                     required=False
                     )
    req.add_argument("-s", "--falcon_client_secret",
                     help="CrowdStrike Falcon API Client Secret",
                     required=False
                     )

    return parser.parse_args()


def open_sdk(client_id: str, client_secret: str, base: str):
    """Create instances of our the Custom IOA Service Class and return it."""
    return CustomIOA(client_id=client_id, client_secret=client_secret, base_url=base)


def chunk_long_description(desc, col_width) -> str:
    """Chunks a long string by delimiting with CR based upon column length."""
    desc_chunks = []
    chunk = ""
    for word in desc.split():
        new_chunk = f"{chunk} {word.strip()}"
        if len(new_chunk) >= col_width:
            if new_chunk[0] == " ":
                new_chunk = new_chunk[1:]
            desc_chunks.append(new_chunk)
            chunk = ""
        else:
            chunk = new_chunk

    delim = "\n"
    desc_chunks.append(chunk[1:])

    return delim.join(desc_chunks)


def get_ioa_list(sdk: CustomIOA, filter_string: str = None):
    """Return the list of IOAs based upon the provided filter."""
    parameters = {}
    if filter_string:
        parameters["filter"] = f"name:*'*{filter_string}*'"
    return sdk.query_rule_groups_full(parameters=parameters)


def show_ioas(matches: dict, table_format: str):
    """Display the IOA listing in tabular format."""
    banner = [
        f"{Color.MAGENTA}",
        "_______ _     _ _______ _______  _____  _______      _____  _____  _______",
        "|       |     | |______    |    |     | |  |  |        |   |     | |_____|",
        f"|_____  |_____| ______|    |    |_____| |  |  |      __|__ |_____| |     |{Color.END}\n"
        ]
    headers = {
        "name": f"{Color.BOLD}Custom IOA Name{Color.END}",
        "description": f"{Color.BOLD}Description{Color.END}",
        "platform": f"{Color.BOLD}Platform{Color.END}",
        "rules": f"{Color.BOLD}Rules{Color.END}"
    }
    ioas = []
    for match in matches["body"]["resources"]:
        ioa = {}
        ioa["name"] = f"{match['name']}\n{Color.CYAN}{match['id']}{Color.END}\n{match['comment']}"
        ioa["description"] = chunk_long_description(match["description"], 40)
        if match["enabled"]:
            enabled = f"{Color.GREEN}Enabled{Color.END}"
        else:
            enabled = f"{Color.LIGHTRED}Disabled{Color.END}"
        platform = [f"{match['platform']}",
                    f"{enabled}",
                    f"Version: {Color.BOLD}{match['version']}{Color.END}"
                    ]
        ioa["platform"] = "\n".join(platform)
        rules = [f"{rule['name']} (ver: {rule['instance_version']})" for rule in match["rules"]]
        ioa["rules"] = "\n".join(rules)
        ioas.append(ioa)

    if not ioas:
        fail = [
            fr"{Color.BOLD}{Color.YELLOW}_  _ ____    ____ ____ ____ _  _ _    ___ ____",
            r"|\ | |  |    |__/ |___ [__  |  | |     |  [__",
            fr"| \| |__|    |  \ |___ ___] |__| |___  |  ___]{Color.END}"
            ]
        print("\n".join(fail))
    else:
        print("\n".join(banner))
        print(tabulate(ioas, headers=headers, tablefmt=table_format))


def duplicate_ioas(sdk: CustomIOA, matches: dict, filter_string: str = None):
    """Duplicate all IOAs that match our provided filter."""
    for rulegroup in matches["body"]["resources"]:
        create = falcon.create_rule_group(name=f"{rulegroup['name']} clone",
                                          description=rulegroup["description"],
                                          comment=f"Cloned from Rule Group {rulegroup['id']}",
                                          platform=rulegroup["platform"]
                                          )
        create_id = create["body"]["resources"][0]["id"]
        print(f"Cloned rule group {rulegroup['name']} to new rule group {create_id}")
        for rule in rulegroup["rules"]:
            rule_body = {
                "description": rule["description"],
                "disposition_id": rule["disposition_id"],
                "comment": "Cloned",
                "field_values": rule["field_values"],
                "pattern_severity": rule["pattern_severity"],
                "name": f"Clone of {rule['name']}",
                "rulegroup_id": create_id,
                "ruletype_id": rule["ruletype_id"]
            }
            rule_create = falcon.create_rule(body=rule_body)
            print(f"Cloned rule to new rule {rule_create['body']['resources'][0]['name']}")
        print(f"Completed clone of rule group {rulegroup['name']}")

    return get_ioa_list(sdk, filter_string)


def delete_ioas(sdk: CustomIOA, ids_to_delete: str, filter_string: str = None):
    """Delete all IOAs in the provided ID list."""
    id_list = ids_to_delete.split(",")
    delete_result = sdk.delete_rule_groups(ids=id_list)
    if delete_result["status_code"] != 200:
        for error in delete_result["body"]["errors"]:
            ecode = f"{Color.LIGHTRED}{error['code']}{Color.END}"
            emsg = f"{Color.YELLOW}{error['message']}{Color.END}"
            print(f"\n{Color.BOLD}[{ecode}{Color.END}{Color.BOLD}] {emsg}")
    else:
        msg = "IOA rule group deleted"
        print(
            f"\n{Color.BOLD}[{Color.GREEN}200{Color.END}{Color.BOLD}] {msg}{Color.END}"
            )
    return get_ioa_list(sdk, filter_string)


def monochrome():
    """Disable color output."""
    return [setattr(Color, item, "") for item in dir(Color) if "__" not in item]


if __name__ == "__main__":
    # Retrieve our command line
    args = consume_arguments()
    if args.nocolor:
        # They don't want shiny, turn off the colors
        monochrome()
    # Create an instance of our Custom IOA Service Class
    falcon = open_sdk(args.falcon_client_id, args.falcon_client_secret, args.base_url)
    # Retrieve all IOA rule groups matching the provided filter
    ioa_rules = get_ioa_list(falcon, args.filter)
    if args.clone:
        if args.filter:
            # Clone any rule groups that match our filter
            ioa_rules = duplicate_ioas(falcon, ioa_rules, args.filter)
        else:
            # Prevent them from cloning every IOA rule group within the tenant
            fail_msg = f"{Color.YELLOW}You must specify a filter in order to clone rule groups"
            print(
                f"\n{Color.BOLD}[{Color.LIGHTRED}400{Color.END}{Color.BOLD}] {fail_msg}{Color.END}"
            )
    if args.delete:
        # Delete any rule groups with IDs in the provided ID list
        ioa_rules = delete_ioas(falcon, args.delete, args.filter)
    # Display all IOA rule group matches in tabular format
    show_ioas(ioa_rules, args.table_format)
