from pygame import Rect

from dataflow_animation.settings.config import get_config

CONFIG = get_config()
WINDOW = Rect(0, 0, CONFIG.width, CONFIG.height)
