"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

sensor_visibility_exclusions - Falcon Machine Learning Exclusions API Interface Class

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
from ._util import force_default, process_service_request, handle_single_argument
from ._service_class import ServiceClass
from ._endpoint._sensor_visibility_exclusions import _sensor_visibility_exclusions_endpoints as Endpoints


class SensorVisibilityExclusions(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, a
    existing instance of the authentication class as an object or a
    valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_exclusions(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get a set of Sensor Visibility Exclusions by specifying their IDs
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /sensor-visibility-exclusions/getSensorVisibilityExclusionsV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getSensorVisibilityExclusionsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def create_exclusions(self: object, body: dict) -> dict:
        """
        Create the Sensor Visibility exclusions
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /sensor-visibility-exclusions/createSVExclusionsV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="createSVExclusionsV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_exclusions(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete the Sensor Visibility exclusions by ID.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #            /sensor-visibility-exclusions/deleteSensorVisibilityExclusionsV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteSensorVisibilityExclusionsV1",
            keywords=kwargs,
            params=parameters
            )

    def update_exclusions(self: object, body: dict) -> dict:
        """
        Update the Sensor Visibility Exclusions
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /sensor-visibility-exclusions/updateSensorVisibilityExclusionsV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateSensorVisibilityExclusionsV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_exclusions(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Sensor Visibility Exclusions.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /sensor-visibility-exclusions/querySensorVisibilityExclusionsV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="querySensorVisibilityExclusionsV1",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    getSensorVisibilityExclusionsV1 = get_exclusions
    createSVExclusionsV1 = create_exclusions
    deleteSensorVisibilityExclusionsV1 = delete_exclusions
    updateSensorVisibilityExclusionsV1 = update_exclusions
    querySensorVisibilityExclusionsV1 = query_exclusions


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Sensor_Visibility_Exclusions = SensorVisibilityExclusions  # pylint: disable=C0103
