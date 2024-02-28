"""Forms for nautobot_itential."""

from django import forms
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin

from nautobot_itential import models


class AutomationGatewayModelForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """AutomationGatewayModel creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.AutomationGatewayModel
        fields = [
            "name",
            "description",
            "location",
            "location_descendants",
            "gateway",
            "enabled",
        ]


class AutomationGatewayModelBulkEditForm(
    TagsBulkEditFormMixin, NautobotBulkEditForm
):  # pylint: disable=too-many-ancestors
    """AutomationGatewayModel bulk edit form."""

    pk = forms.ModelMultipleChoiceField(
        queryset=models.AutomationGatewayModel.objects.all(), widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class AutomationGatewayModelFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.AutomationGatewayModel
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")


class InventoryGroupModelForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """InventoryGroupModel creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.InventoryGroupModel
        fields = [
            "name",
            "description",
            "context",
        ]


class InventoryGroupModelBulkEditForm(
    TagsBulkEditFormMixin, NautobotBulkEditForm
):  # pylint: disable=too-many-ancestors
    """InventoryGroupModel bulk edit form."""

    pk = forms.ModelMultipleChoiceField(
        queryset=models.InventoryGroupModel.objects.all(), widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class InventoryGroupModelFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.InventoryGroupModel
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")
