from typing import Optional

from pydantic import BaseModel


class Config(BaseModel):
    # Window position
    x: int = 0
    y: int = 0
    sdl_video_window_pos: str = f"{x},{y}"

    # Screen dimensions
    width: int = 600
    height: int = 800

    # Rendering
    fps: int = 60

    class Config:
        env_file = ".env"
        validate_assignment = True


_singleton_instance: Optional[Config] = None


def get_config() -> Config:
    # pylint: disable=global-statement
    global _singleton_instance
    if _singleton_instance is None:
        _singleton_instance = Config()
    return _singleton_instance
