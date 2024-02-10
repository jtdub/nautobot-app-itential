"""Test AutomationGatewayModel."""

from django.test import TestCase

from nautobot_itential import models
from nautobot_itential.tests import fixtures

from nautobot.dcim.models import Location
from nautobot.extras.models import ExternalIntegration


class TestAutomationGatewayModel(TestCase):
    """Test AutomationGatewayModel."""

    def setUp(self):
        """Setup fixtures."""
        fixtures.create_locations()

    def test_create_automationgatewaymodel_only_required(self):
        """Create with only required fields, and validate null description and __str__."""

        location = Location.objects.get(name="NYC")
        external_integration = ExternalIntegration.objects.create(
            name="NYC external integration | 1",
            remote_url="https://iag1.nyc.example.com",
        )
        automationgatewaymodel = models.AutomationGatewayModel.objects.create(
            name="NYC1", gateway=external_integration, location=location
        )
        self.assertEqual(automationgatewaymodel.name, "NYC1")
        self.assertEqual(automationgatewaymodel.description, "")
        self.assertEqual(str(automationgatewaymodel), "NYC1")
        self.assertEqual(str(automationgatewaymodel.location), "NYC")
        self.assertEqual(automationgatewaymodel.location_descendants, True)
        self.assertEqual(
            str(automationgatewaymodel.gateway), "NYC external integration | 1 (https://iag1.nyc.example.com)"
        )
        self.assertEqual(automationgatewaymodel.enabled, False)

    def test_create_automationgatewaymodel_all_fields_success(self):
        """Create AutomationGatewayModel with all fields."""
        location = Location.objects.get(name="NYC")
        external_integration = ExternalIntegration.objects.create(
            name="NYC external integration | 2",
            remote_url="https://iag2.nyc.example.com",
        )
        automationgatewaymodel = models.AutomationGatewayModel.objects.create(
            name="NYC2",
            description="Development Test",
            gateway=external_integration,
            location=location,
            location_descendants=False,
            enabled=True,
        )
        self.assertEqual(automationgatewaymodel.name, "NYC2")
        self.assertEqual(automationgatewaymodel.description, "Development Test")
        self.assertEqual(str(automationgatewaymodel), "NYC2")
        self.assertEqual(str(automationgatewaymodel.location), "NYC")
        self.assertEqual(automationgatewaymodel.location_descendants, False)
        self.assertEqual(
            str(automationgatewaymodel.gateway), "NYC external integration | 2 (https://iag2.nyc.example.com)"
        )
        self.assertEqual(automationgatewaymodel.enabled, True)
