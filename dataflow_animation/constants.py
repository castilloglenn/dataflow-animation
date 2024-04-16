from pygame import Rect

from dataflow_animation.settings.config import get_config

WINDOW = Rect(0, 0, get_config().width, get_config().height)
