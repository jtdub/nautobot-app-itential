"""Django urlpatterns declaration for nautobot_itential app."""

from nautobot.apps.urls import NautobotUIViewSetRouter

from nautobot_itential import views


router = NautobotUIViewSetRouter()
router.register("automationgatewaymodel", views.AutomationGatewayModelUIViewSet)
router.register("inventorygroupmodel", views.InventoryGroupModelUIViewSet)

urlpatterns = router.urls
