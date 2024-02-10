"""Test AutomationGatewayModel."""

from django.test import TestCase

from nautobot_itential import models


# class TestAutomationGatewayModel(TestCase):
#     """Test AutomationGatewayModel."""
# 
#     def test_create_automationgatewaymodel_only_required(self):
#         """Create with only required fields, and validate null description and __str__."""
#         automationgatewaymodel = models.AutomationGatewayModel.objects.create(name="Development")
#         self.assertEqual(automationgatewaymodel.name, "Development")
#         self.assertEqual(automationgatewaymodel.description, "")
#         self.assertEqual(str(automationgatewaymodel), "Development")
# 
#     def test_create_automationgatewaymodel_all_fields_success(self):
#         """Create AutomationGatewayModel with all fields."""
#         automationgatewaymodel = models.AutomationGatewayModel.objects.create(
#             name="Development", description="Development Test"
#         )
#         self.assertEqual(automationgatewaymodel.name, "Development")
#         self.assertEqual(automationgatewaymodel.description, "Development Test")
