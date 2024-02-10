"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab


items = (
    NavMenuItem(
        link="plugins:nautobot_itential:automationgatewaymodel_list",
        name="Automation Gateway",
        permissions=["nautobot_itential.view_automationgatewaymodel"],
        buttons=(
            NavMenuAddButton(
                link="plugins:nautobot_itential:automationgatewaymodel_add",
                permissions=["nautobot_itential.add_automationgatewaymodel"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="Itential", items=tuple(items)),),
    ),
)
