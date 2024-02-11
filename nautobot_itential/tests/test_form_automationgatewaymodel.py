"""Test automationgatewaymodel forms."""
from django.test import TestCase

from nautobot_itential import forms, models
from nautobot_itential.tests import fixtures

from nautobot.dcim.models import Location
from nautobot.extras.models import ExternalIntegration


class AutomationGatewayModelTest(TestCase):
    """Test AutomationGatewayModel forms."""

    def setUp(self):
        """setup test fixtures."""
        fixtures.create_locations()

        self.location = Location.objects.first()
        self.gateway = ExternalIntegration.objects.create(name="TEST GW", remote_url="https://test.gw.example.com")

    def test_specifying_all_fields_success(self):
        form = forms.AutomationGatewayModelForm(
            data={
                "name": "TEST",
                "description": "Test description.",
                "location": self.location.pk,
                "location_descendants": True,
                "gateway": self.gateway.pk,
                "enabled": False,
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.AutomationGatewayModelForm(
            data={
                "name": "TEST",
                "location": self.location.pk,
                "gateway": self.gateway.pk,
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_automationgatewaymodel_is_required(self):
        form = forms.AutomationGatewayModelForm(
            data={
                "location": self.location.pk,
                "gateway": self.gateway.pk,
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])
