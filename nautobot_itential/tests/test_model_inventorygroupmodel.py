"""Test InventoryGroupModel."""

from django.test import TestCase

from nautobot.dcim.models import Device, Platform

from nautobot_itential import models
from nautobot_itential.tests import fixtures


class TestInventoryGroupModel(TestCase):
    """Test InventoryGroupModel."""

    def setUp(self):
        """Setup test fixtures."""
        fixtures.create_devices()

        self.device = Device.objects.get(name="router1")
        self.platform = Platform.objects.get(name="Arista EOS")

    def test_create_inventorygroupmodel_only_required(self):
        """Tests creation of an inventory group with only required fields."""
        inventorygroupmodel = models.InventoryGroupModel.objects.create(name="Test 1")

        self.assertEqual(inventorygroupmodel.name, "Test 1")
        self.assertEqual(inventorygroupmodel.description, "")
        self.assertEqual(inventorygroupmodel.context, {})
        self.assertEqual(inventorygroupmodel.devices.count(), 0)
        self.assertEqual(inventorygroupmodel.platforms.count(), 0)

    def test_create_inventorygroupmodel_all_fields_device__success(self):
        inventorygroupmodel = models.InventoryGroupModel.objects.create(
            name="Test 2",
            description="This is test description two.",
            context={"key2": "value2"},
        )
        inventorygroupmodel.devices.add(self.device)
        inventorygroupmodel.save()

        self.assertEqual(inventorygroupmodel.name, "Test 2")
        self.assertEqual(inventorygroupmodel.description, "This is test description two.")
        self.assertEqual(inventorygroupmodel.context, {"key2": "value2"})
        self.assertEqual(inventorygroupmodel.devices.count(), 1)
        self.assertEqual(inventorygroupmodel.platforms.count(), 0)

    def test_create_inventorygroupmodel_all_fields_platform__success(self):
        inventorygroupmodel = models.InventoryGroupModel.objects.create(
            name="Test 3",
            description="This is test description three.",
            context={"key3": "value3"},
        )
        inventorygroupmodel.platforms.add(self.platform)
        inventorygroupmodel.save()

        self.assertEqual(inventorygroupmodel.name, "Test 3")
        self.assertEqual(inventorygroupmodel.description, "This is test description three.")
        self.assertEqual(inventorygroupmodel.context, {"key3": "value3"})
        self.assertEqual(inventorygroupmodel.devices.count(), 0)
        self.assertEqual(inventorygroupmodel.platforms.count(), 1)

    def test_create_inventorygroupmodel_all_fields__success(self):
        inventorygroupmodel = models.InventoryGroupModel.objects.create(
            name="Test 4",
            description="This is test description four.",
            context={"key4": "value4"},
        )
        inventorygroupmodel.devices.add(self.device)
        inventorygroupmodel.platforms.add(self.platform)
        inventorygroupmodel.save()

        self.assertEqual(inventorygroupmodel.name, "Test 4")
        self.assertEqual(inventorygroupmodel.description, "This is test description four.")
        self.assertEqual(inventorygroupmodel.context, {"key4": "value4"})
        self.assertEqual(inventorygroupmodel.devices.count(), 1)
        self.assertEqual(inventorygroupmodel.platforms.count(), 1)
