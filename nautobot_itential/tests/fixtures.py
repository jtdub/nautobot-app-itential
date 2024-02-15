"""Create fixtures for tests."""

from django.contrib.contenttypes.models import ContentType
from nautobot.dcim.models import Location, LocationType, Device, DeviceType, Manufacturer, Platform
from nautobot.extras.models import ExternalIntegration, Status, Role
from nautobot_itential.models import AutomationGatewayModel, InventoryGroupModel


def create_locations():
    """Fixtures to create location data used for tests."""
    status = Status.objects.get(name="Active")
    site, _ = LocationType.objects.update_or_create(name="Site")
    data = [
        {"site": "NYC"},
        {"site": "AUS"},
        {"site": "LAX"},
    ]

    for item in data:
        Location.objects.update_or_create(name=item["site"], location_type=site, status=status)


def create_manufacturers():
    """Fixtures to create manufacturer data used for tests."""
    data = ["Cisco", "Arista"]

    for item in data:
        Manufacturer.objects.update_or_create(name=item)


def create_platforms():
    """Fixtures to create platform data used for tests."""
    create_manufacturers()

    cisco = Manufacturer.objects.get(name="Cisco")
    arista = Manufacturer.objects.get(name="Arista")
    data = [
        {"name": "Cisco IOSXR", "network_driver": "cisco_xr", "manufacturer": cisco},
        {"name": "Cisco IOS", "network_driver": "cisco_ios", "manufacturer": cisco},
        {"name": "Arista EOS", "network_driver": "arista_eos", "manufacturer": arista},
    ]

    for item in data:
        Platform.objects.update_or_create(
            name=item["name"], network_driver=item["network_driver"], manufacturer=item["manufacturer"]
        )


def create_device_types():
    """Fixtures to create device_type data used for tests."""
    create_manufacturers()

    cisco = Manufacturer.objects.get(name="Cisco")
    arista = Manufacturer.objects.get(name="Arista")

    data = [
        {"name": cisco, "model": "NCS 5501"},
        {"name": cisco, "model": "Catalyst 8300"},
        {"name": arista, "model": "7280R"},
    ]

    for item in data:
        DeviceType.objects.update_or_create(manufacturer=item["name"], model=item["model"])


def create_roles():
    """Fixtures to crate role data used for tests."""
    device_content_type = ContentType.objects.get(app_label="dcim", model="device")

    data = [{"name": "Router", "content_types": device_content_type}]

    for item in data:
        role, _ = Role.objects.update_or_create(name=item["name"])
        role.content_types.add(device_content_type)
        role.save()


def create_devices():
    """Fixtures to create device data used for tests."""
    create_roles()
    create_device_types()
    create_platforms()
    create_locations()

    status = Status.objects.get(name="Active")
    role = Role.objects.get(name="Router")
    cisco_xr = Platform.objects.get(name="Cisco IOSXR")
    cisco_ios = Platform.objects.get(name="Cisco IOS")
    arista_eos = Platform.objects.get(name="Arista EOS")
    cisco_xr_type = DeviceType.objects.get(model="NCS 5501")
    cisco_ios_type = DeviceType.objects.get(model="Catalyst 8300")
    arista_eos_type = DeviceType.objects.get(model="7280R")
    location = Location.objects.first()

    data = [
        {"name": "router1", "location": location, "device_type": cisco_xr_type, "role": role, "platform": cisco_xr},
        {"name": "router2", "location": location, "device_type": cisco_ios_type, "role": role, "platform": cisco_ios},
        {"name": "router3", "location": location, "device_type": arista_eos_type, "role": role, "platform": arista_eos},
    ]

    for item in data:
        Device.objects.update_or_create(
            name=item["name"],
            location=item["location"],
            device_type=item["device_type"],
            role=item["role"],
            platform=item["platform"],
            status=status,
        )


def create_external_integrations():
    """Fixtures to create external integrations used for tests."""
    data = [
        {"name": "NYC external gateway", "url": "https://iag.nyc.example.com"},
        {"name": "AUS external gateway", "url": "https://iag.aus.example.com"},
        {"name": "LAX external gateway", "url": "https://iag.lax.example.com"},
        {"name": "API View gateway1", "url": "https://apiview1.example.com"},
        {"name": "API View gateway2", "url": "https://apiview2.example.com"},
        {"name": "API View gateway3", "url": "https://apiview3.example.com"},
        {"name": "Bulk View gateway1", "url": "https://bulkview1.example.com"},
        {"name": "Bulk View gateway2", "url": "https://bulkview2.example.com"},
        {"name": "Bulk View gateway3", "url": "https://bulkview3.example.com"},
        {"name": "Bulk View gateway4", "url": "https://bulkview4.example.com"},
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

    data = [
        {"name": "NYC Gateway", "location": nyc, "gateway": nyc_gateway},
        {"name": "AUS Gateway", "location": aus, "gateway": aus_gateway},
        {"name": "LAX Gateway", "location": lax, "gateway": lax_gateway},
    ]

    for item in data:
        AutomationGatewayModel.objects.create(
            name=item["name"], location=item["location"], gateway=item["gateway"], enabled=True
        )


def create_inventorygroupmodel():
    """Fixture to create necessary number of InventoryGroupModel for tests."""
    create_devices()

    data = [
        {
            "name": "Cisco IOSXR",
            "context": {
                "ansible_connection": "ansible.netcommon.network_cli",
                "ansible_network_os": "cisco.iosxr.iosxr",
            },
            "device": Device.objects.get(name="router1"),
        },
    ]

    for item in data:
        group = InventoryGroupModel.objects.create(name=item["name"], context=item["context"])
        group.devices.add(item["device"])
