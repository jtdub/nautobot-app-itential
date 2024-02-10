"""API serializers for nautobot_itential."""
from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from nautobot_itential import models


class AutomationGatewayModelSerializer(
    NautobotModelSerializer, TaggedModelSerializerMixin
):  # pylint: disable=too-many-ancestors
    """AutomationGatewayModel Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.AutomationGatewayModel
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
