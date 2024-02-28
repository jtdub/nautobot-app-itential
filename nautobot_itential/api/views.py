"""API views for nautobot_itential."""

from nautobot.apps.api import NautobotModelViewSet

from nautobot_itential import filters, models
from nautobot_itential.api import serializers


class AutomationGatewayModelViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """AutomationGatewayModel viewset."""

    queryset = models.AutomationGatewayModel.objects.all()
    serializer_class = serializers.AutomationGatewayModelSerializer
    filterset_class = filters.AutomationGatewayModelFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]


class InventoryGroupModelViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """InventoryGroupModel viewset."""

    queryset = models.InventoryGroupModel.objects.all()
    serializer_class = serializers.InventoryGroupModelSerializer
    filterset_class = filters.InventoryGroupModelFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
