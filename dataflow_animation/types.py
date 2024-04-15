from typing import TypedDict, Any, Tuple


from dataflow_animation.enums import Direction


Dataflow = Any
"""Type alias for the Dataflow class."""

Color = Tuple[int, int, int]
Coordinates = Tuple[int, int]


class ConfigOptions(TypedDict, total=False):
    width: int
    height: int
    x: int
    y: int
    sdl_video_window_pos: str
    fps: int
    font_name: str
    font_size: int
    font_color: Color
    background_color: Color
    data_direction: Direction
    padding: int
