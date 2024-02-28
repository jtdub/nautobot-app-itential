"""Test InventoryGroupModel forms."""

from django.test import TestCase

# from nautobot.dcim.models import Device, Platform

from nautobot_itential import forms
from nautobot_itential.tests import fixtures


class InventoryGroupModelTest(TestCase):
    """Test InventoryGroupModel forms."""

    def setUp(self):
        """setup test fixtures."""
        fixtures.create_devices()
        self.context = {"ansible_network_os": "cisco.iosxr.iosxr"}

    def test_specifying_all_fields_success(self):
        form = forms.InventoryGroupModelForm(
            data={
                "name": "TEST Form",
                "description": "Test description.",
                "context": self.context,
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.InventoryGroupModelForm(
            data={
                "name": "TEST Form",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_inventorygroupmodel_is_required(self):
        form = forms.InventoryGroupModelForm(data={"context": self.context})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])
