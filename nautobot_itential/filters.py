"""Filtering for nautobot_itential."""

from nautobot.apps.filters import NautobotFilterSet, NameSearchFilterSet

from nautobot_itential import models


class AutomationGatewayModelFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for AutomationGatewayModel."""

    class Meta:
        """Meta attributes for filter."""

        model = models.AutomationGatewayModel

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description", "gateway", "location", "enabled"]
