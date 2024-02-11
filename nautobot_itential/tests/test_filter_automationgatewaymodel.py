"""Test AutomationGatewayModel Filter."""

# from django.test import TestCase
# from nautobot_itential import filters
# from nautobot_itential import models
# from nautobot_itential.tests import fixtures


# class AutomationGatewayModelFilterTestCase(TestCase):
#     """AutomationGatewayModel Filter Test Case."""
#
#     queryset = models.AutomationGatewayModel.objects.all()
#     filterset = filters.AutomationGatewayModelFilterSet
#
#     @classmethod
#     def setUpTestData(cls):
#         """Setup test data for AutomationGatewayModel Model."""
#         fixtures.create_automationgatewaymodel()
#
#     def test_q_search_name(self):
#         """Test using Q search with name of AutomationGatewayModel."""
#         params = {"q": "NYC Gateway"}
#         self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)
#
#     def test_q_invalid(self):
#         """Test using invalid Q search for AutomationGatewayModel."""
#         params = {"q": "test-five"}
#         self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
