"""Django API urlpatterns declaration for nautobot_itential app."""

from nautobot.apps.api import OrderedDefaultRouter

from nautobot_itential.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("automationgatewaymodel", views.AutomationGatewayModelViewSet)
router.register("inventorygroupmodel", views.InventoryGroupModelViewSet)

urlpatterns = router.urls
