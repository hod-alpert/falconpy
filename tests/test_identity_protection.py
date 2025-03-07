# test_identity_protection.py
# This class tests the identity_protection service class
import os
import sys
import json
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
# flake8: noqa=E402
from falconpy import IdentityProtection

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()

falcon = IdentityProtection(auth_object=config)
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestIdentityProtection:
    def idp_graphql(self):
        payload = {"query":"{\n  entities(first: 1)\n  {\n    nodes {\n      entityId    \n    }\n  }\n}"}
        # GraphQL is sometimes returning results as binary encoded
        result = falcon.GraphQL(body=payload)
        if not isinstance(result, dict):
            result = json.loads(result.decode())
        if "extensions" in result:
            if result["extensions"]["remainingPoints"] > 0:
                return True
            else:
                return False
        else:
            # Prolly failed login, check yer API key
            return False

    def idp_graphql_keywords(self):
        test_query = "{\n  entities(first: 1)\n  {\n    nodes {\n      entityId    \n    }\n  }\n}"
        # GraphQL is sometimes returning results as binary encoded
        result = falcon.graphql(query=test_query)
        if not isinstance(result, dict):
            result = json.loads(result.decode())
        if "extensions" in result:
            if result["extensions"]["remainingPoints"] > 0:
                return True
            else:
                return False
        else:
            # Prolly failed login, check yer API key
            return False

    @pytest.mark.skipif(config.base_url != "https://api.crowdstrike.com", reason="Unit testing unavailable on US-2")
    def test_graphql(self):
        assert self.idp_graphql() is True

    @pytest.mark.skipif(config.base_url != "https://api.crowdstrike.com", reason="Unit testing unavailable on US-2")
    def test_graphql_keywords(self):
        assert self.idp_graphql_keywords() is True
