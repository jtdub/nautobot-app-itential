"""Unit tests for views."""

from nautobot.apps.testing import ViewTestCases

from nautobot.dcim.models import Location
from nautobot.extras.models import ExternalIntegration

from nautobot_itential import models
from nautobot_itential.tests import fixtures


class AutomationGatewayModelViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the AutomationGatewayModel views."""

    model = models.AutomationGatewayModel

    @classmethod
    def setUpTestData(cls):
        fixtures.create_automationgatewaymodel()

        location = Location.objects.first()
        gw1 = ExternalIntegration.objects.get(name="Bulk View gateway1")
        gw2 = ExternalIntegration.objects.get(name="Bulk View gateway2")
        gw3 = ExternalIntegration.objects.get(name="Bulk View gateway3")
        gw4 = ExternalIntegration.objects.get(name="Bulk View gateway4")

        cls.bulk_edit_data = {"description": "Bulk edit views"}
        cls.form_data = {
            "name": "Test 1",
            "description": "Initial model",
            "location": location.pk,
            "gateway": gw1.pk,
        }
        cls.csv_data = (
            "name,location,gateway",
            f"Test 2,{location.pk},{gw2.pk}",
            f"Test 3,{location.pk},{gw3.pk}",
            f"Test 4,{location.pk},{gw4.pk}",
        )
