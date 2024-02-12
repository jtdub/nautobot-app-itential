"""Create fixtures for tests."""

from nautobot.dcim.models import Location, LocationType
from nautobot.extras.models import ExternalIntegration, Status
from nautobot_itential.models import AutomationGatewayModel


def create_locations():
    """Fixtures to create location data used for tests."""
    site = LocationType.objects.create(name="Site")
    status = Status.objects.get(name="Active")
    data = [
        {"site": "NYC"},
        {"site": "AUS"},
        {"site": "LAX"},
    ]

    for item in data:
        Location.objects.update_or_create(name=item["site"], location_type=site, status=status)


def create_external_integrations():
    """Fixtures to create external integrations used for tests."""
    data = [
        {"name": "NYC external gateway", "url": "https://iag.nyc.example.com"},
        {"name": "AUS external gateway", "url": "https://iag.aus.example.com"},
        {"name": "LAX external gateway", "url": "https://iag.lax.example.com"},
        {"name": "API View gateway1", "url": "https://apiview1.example.com"},
        {"name": "API View gateway2", "url": "https://apiview2.example.com"},
        {"name": "API View gateway3", "url": "https://apiview3.example.com"},
    ]

    for item in data:
        ExternalIntegration.objects.update_or_create(
            name=item["name"],
            remote_url=item["url"],
        )


def create_automationgatewaymodel():
    """Fixture to create necessary number of AutomationGatewayModel for tests."""
    create_locations()
    create_external_integrations()

    nyc = Location.objects.get(name="NYC")
    aus = Location.objects.get(name="AUS")
    lax = Location.objects.get(name="LAX")
    nyc_gateway = ExternalIntegration.objects.get(name="NYC external gateway")
    aus_gateway = ExternalIntegration.objects.get(name="AUS external gateway")
    lax_gateway = ExternalIntegration.objects.get(name="LAX external gateway")

    AutomationGatewayModel.objects.create(name="NYC Gateway", location=nyc, gateway=nyc_gateway, enabled=True)
    AutomationGatewayModel.objects.create(name="AUS Gateway", location=aus, gateway=aus_gateway, enabled=True)
    AutomationGatewayModel.objects.create(name="LAX Gateway", location=lax, gateway=lax_gateway, enabled=True)
