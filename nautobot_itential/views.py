"""Views for nautobot_itential."""

from nautobot.apps.views import NautobotUIViewSet

from nautobot_itential import filters, forms, models, tables
from nautobot_itential.api import serializers


class AutomationGatewayModelUIViewSet(NautobotUIViewSet):
    """ViewSet for AutomationGatewayModel views."""

    bulk_update_form_class = forms.AutomationGatewayModelBulkEditForm
    filterset_class = filters.AutomationGatewayModelFilterSet
    filterset_form_class = forms.AutomationGatewayModelFilterForm
    form_class = forms.AutomationGatewayModelForm
    lookup_field = "pk"
    queryset = models.AutomationGatewayModel.objects.all()
    serializer_class = serializers.AutomationGatewayModelSerializer
    table_class = tables.AutomationGatewayModelTable
