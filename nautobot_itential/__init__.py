"""App declaration for nautobot_itential."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class NautobotItentialConfig(NautobotAppConfig):
    """App configuration for the nautobot_itential app."""

    name = "nautobot_itential"
    verbose_name = "Nautobot Itential"
    version = __version__
    author = "Network to Code, LLC"
    description = "Nautobot Itential."
    base_url = "nautobot-itential"
    required_settings = []
    min_version = "2.1.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}


config = NautobotItentialConfig  # pylint:disable=invalid-name
