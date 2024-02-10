"""Unit tests for nautobot_itential."""
from nautobot.apps.testing import APIViewTestCases

from nautobot_itential import models
from nautobot_itential.tests import fixtures


# class AutomationGatewayModelAPIViewTest(APIViewTestCases.APIViewTestCase):
#     # pylint: disable=too-many-ancestors
#     """Test the API viewsets for AutomationGatewayModel."""
#
#     model = models.AutomationGatewayModel
#     create_data = [
#         {
#             "name": "Test Model 1",
#             "description": "test description",
#         },
#         {
#             "name": "Test Model 2",
#         },
#     ]
#     bulk_update_data = {"description": "Test Bulk Update"}

#     @classmethod
#     def setUpTestData(cls):
#         fixtures.create_automationgatewaymodel()
