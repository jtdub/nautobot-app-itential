"""Unit tests for nautobot_itential."""

from nautobot.apps.testing import APIViewTestCases

from nautobot.dcim.models import Location
from nautobot.extras.models import ExternalIntegration

from nautobot_itential import models
from nautobot_itential.tests import fixtures


class AutomationGatewayModelAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for AutomationGatewayModel."""

    model = models.AutomationGatewayModel

    @classmethod
    def setUpTestData(cls):
        fixtures.create_automationgatewaymodel()

        location = Location.objects.first()
        gw1 = ExternalIntegration.objects.get(name="API View gateway1")
        gw2 = ExternalIntegration.objects.get(name="API View gateway2")
        gw3 = ExternalIntegration.objects.get(name="API View gateway3")

        cls.create_data = [
            {
                "name": "Test Model 1",
                "description": "test description",
                "location": location.pk,
                "gateway": gw1.pk,
            },
            {
                "name": "Test Model 2",
                "location": location.pk,
                "gateway": gw2.pk,
            },
            {
                "name": "Test Model 3",
                "location": location.pk,
                "gateway": gw3.pk,
            },
        ]
        cls.bulk_update_data = {"description": "Test Bulk Update"}
