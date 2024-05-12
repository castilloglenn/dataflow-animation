from dataclasses import dataclass, field
from typing import Optional
import logging

from dataflow_animation.types import Color, ConfigOptions, Milliseconds, Pixels
from dataflow_animation.enums import Direction


@dataclass
class Config:
    # Screen dimensions
    width: Pixels = 350
    height: Pixels = 400

    # Window position
    x: Pixels = 0
    y: Pixels = 0

    # Derived field: SDL video window position
    sdl_video_window_pos: str = field(init=False)

    # Rendering
    fps: int = 60
    font_name: Optional[str] = None
    font_size: int = 20
    data_direction: Direction = Direction.RIGHT

    # Animation Timing
    stay_duration: Milliseconds = 1000

    # Spacing
    padding: Pixels = 10
    vertical_text_spacing: Pixels = 10

    # Colors
    font_color: Color = (255, 255, 255)
    background_color: Color = (0, 0, 0)

    def __post_init__(self):
        self.sdl_video_window_pos = f"{self.x},{self.y}"

    def update(self, **kwargs: ConfigOptions):
        for key, value in kwargs.items():
            if not hasattr(self, key):
                raise ValueError(f"Invalid configuration option: {key}")

            setattr(self, key, value)
            if key in ("x", "y"):
                self.sdl_video_window_pos = f"{self.x},{self.y}"

            logging.info("Configuration updated: %s -> %s", key, value)


_singleton_instance: Optional[Config] = None


def get_config() -> Config:
    # pylint: disable=W0603
    global _singleton_instance
    if _singleton_instance is None:
        _singleton_instance = Config()
    return _singleton_instance


def set_config(**kwargs: ConfigOptions):
    get_config().update(**kwargs)
    return get_config()


def reset_config():
    # pylint: disable=W0603
    global _singleton_instance
    _singleton_instance = None
