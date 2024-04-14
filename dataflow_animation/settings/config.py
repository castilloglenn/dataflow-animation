from dataclasses import dataclass, field
from typing import Tuple, Optional
import logging


# pylint: disable=R0902
@dataclass
class Config:
    # Screen dimensions
    width: int = 600
    height: int = 800

    # Window position
    x: int = 0
    y: int = 0

    # Derived field: SDL video window position
    sdl_video_window_pos: str = field(init=False)

    # Rendering
    fps: int = 60
    font_name: str = "Arial"
    font_size: int = 20

    # Colors
    font_color: Tuple[int, int, int] = (255, 255, 255)
    background_color: Tuple[int, int, int] = (0, 0, 0)

    def __post_init__(self):
        # Initialize `sdl_video_window_pos` based on `x` and `y`
        self.sdl_video_window_pos = f"{self.x},{self.y}"

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
                if key in ("x", "y"):
                    self.sdl_video_window_pos = f"{self.x},{self.y}"
        logging.info("Configuration updated: %s", kwargs)


_singleton_instance: Optional[Config] = None


def get_config() -> Config:
    # pylint: disable=W0603
    global _singleton_instance
    if _singleton_instance is None:
        _singleton_instance = Config()
    return _singleton_instance
