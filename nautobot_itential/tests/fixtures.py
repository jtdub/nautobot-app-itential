"""Create fixtures for tests."""
from nautobot.dcim.models import Location, LocationType
from nautobot.extras models import ExternalIntegration
from nautobot_itential.models import AutomationGatewayModel


def create_automationgatewaymodel():
    """Fixture to create necessary number of AutomationGatewayModel for tests."""
    location_type = LocationType.objects.create(name="Site")
    location = Location.objects.create(name="NYC1", location_type=location_type, status="Active")
    remote_gateway = ExternalIntegration.objects.create(
        name="NYC Itential Automation Gateway",
        remote_url="https://iag.nyc1.example.com",
    )
    AutomationGatewayModel.objects.create(
        name="NYC Gateway",
        location=location,
        gateway=remote_gateway,
        enabled=True
    )
