"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

ioc - CrowdStrike Falcon Indicators of Compromise API interface class v2

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
from ._util import force_default, process_service_request
from ._service_class import ServiceClass
from ._endpoint._ioc import _ioc_endpoints as Endpoints


class IOC(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, an
    authorization object (oauth2.py) or a credential dictionary with
    client_id and client_secret containing valid API credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_combined(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get Combined for Indicators.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.combined.v1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_combined_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_get(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get Indicators by ids.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.get.v1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_get_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_create(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Create Indicators.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.create.v1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_create_v1",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_delete(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete Indicators by ids.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.delete.v1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_delete_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_update(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Update Indicators.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.update.v1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_update_v1",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_search(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Indicators.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.search.v1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_search_v1",
            keywords=kwargs,
            params=parameters
            )

    # These names are acceptable and match the API operation IDs.
    # They are defined here for ease of use purposes.
    indicator_combined_v1 = indicator_combined
    indicator_get_v1 = indicator_get
    indicator_create_v1 = indicator_create
    indicator_delete_v1 = indicator_delete
    indicator_update_v1 = indicator_update
    indicator_search_v1 = indicator_search
