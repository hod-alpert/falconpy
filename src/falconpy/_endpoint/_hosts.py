"""Internal API endpoint constant library.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""

_hosts_endpoints = [
  [
    "QueryDeviceLoginHistory",
    "POST",
    "/devices/combined/devices/login-history/v1",
    "Retrieve details about recent login sessions for a set of devices.",
    "hosts",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "QueryGetNetworkAddressHistoryV1",
    "POST",
    "/devices/combined/devices/network-address-history/v1",
    "Retrieve history of IP and MAC addresses of devices.",
    "hosts",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "PerformActionV2",
    "POST",
    "/devices/entities/devices-actions/v2",
    "Take various actions on the hosts in your environment. Contain or lift containment on a host. Delete or restore a host.",
    "hosts",
    [
      {
        "type": "string",
        "description": "Specify one of these actions:\n\n- `contain` - "
        "This action contains the host, which stops any network communications to "
        "locations other than the CrowdStrike cloud and IPs specified in your [containment policy]"
        "(https://falcon.crowdstrike.com/support/documentation/11/getting-started-guide#containmentpolicy)"
        "\n- `lift_containment`: This action lifts containment on the host, which returns its network "
        "communications to normal\n- `hide_host`: This action will delete a host. After the host is deleted, "
        "no new detections for that host will be reported via UI or APIs\n- `unhide_host`: "
        "This action will restore a host. Detection reporting will resume after the host is restored",
        "name": "action_name",
        "in": "query",
        "required": True
      },
      {
        "description": "The host agent ID (AID) of the host you want to contain. "
        "Get an agent ID from a detection, the Falcon console, or the Streaming API.\n\n"
        "Provide the ID in JSON format with the key `ids` and the value in square brackets, "
        "such as: \n\n`\"ids\": [\"123456789\"]`",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "UpdateDeviceTags",
    "PATCH",
    "/devices/entities/devices/tags/v1",
    "Append or remove one or more Falcon Grouping Tags on one or more hosts.",
    "hosts",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetDeviceDetails",
    "GET",
    "/devices/entities/devices/v1",
    "Get details on one or more hosts by providing agent IDs (AID). You can get a host's agent IDs "
    "(AIDs) from the /devices/queries/devices/v1 endpoint, the Falcon console or the Streaming API",
    "hosts",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The host agentIDs used to get details on",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "GetOnlineState_V1",
    "GET",
    "/devices/entities/online-state/v1",
    "Get the online status for one or more hosts by specifying each host’s unique ID. "
    "Successful requests return an HTTP 200 response and the status for each host identified "
    "by a `state` of `online`, `offline`, or `unknown` for each host, identified by host `id`."
    "\n\nMake a `GET` request to `/devices/queries/devices/v1` to get a list of host IDs.",
    "hosts",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The unique ID of the host to get the online status of.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "QueryHiddenDevices",
    "GET",
    "/devices/queries/devices-hidden/v1",
    "Retrieve hidden hosts that match the provided filter criteria.",
    "hosts",
    [
      {
        "type": "integer",
        "description": "The offset to start retrieving records from",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The maximum records to return. [1-5000]",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The property to sort by (e.g. status.desc or hostname.asc)",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The filter expression that should be used to limit the results",
        "name": "filter",
        "in": "query"
      }
    ]
  ],
  [
    "QueryDevicesByFilterScroll",
    "GET",
    "/devices/queries/devices-scroll/v1",
    "Search for hosts in your environment by platform, hostname, IP, and other criteria with "
    "continuous pagination capability (based on offset pointer which expires after 2 minutes with no maximum limit)",
    "hosts",
    [
      {
        "type": "string",
        "description": "The offset to page from, for the next result set",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The maximum records to return. [1-5000]",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The property to sort by (e.g. status.desc or hostname.asc)",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The filter expression that should be used to limit the results",
        "name": "filter",
        "in": "query"
      }
    ]
  ],
  [
    "QueryDevicesByFilter",
    "GET",
    "/devices/queries/devices/v1",
    "Search for hosts in your environment by platform, hostname, IP, and other criteria.",
    "hosts",
    [
      {
        "type": "integer",
        "description": "The offset to start retrieving records from",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The maximum records to return. [1-5000]",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The property to sort by (e.g. status.desc or hostname.asc)",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The filter expression that should be used to limit the results",
        "name": "filter",
        "in": "query"
      }
    ]
  ]
]
