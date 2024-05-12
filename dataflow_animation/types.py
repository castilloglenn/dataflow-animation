from typing import Optional, TypedDict, Any, Tuple


from dataflow_animation.enums import Direction


Dataflow = Any
"""Type alias for the Dataflow class."""

Color = Tuple[int, int, int]
Coordinates = Tuple[int, int]
Milliseconds = int
Pixels = int


class ConfigOptions(TypedDict, total=False):
    # Screen dimensions
    width: Pixels
    height: Pixels
    # Window position
    x: Pixels
    y: Pixels
    # Derived field: SDL video window position
    sdl_video_window_pos: str
    # Rendering
    fps: int
    font_name: Optional[str]
    font_size: int
    data_direction: Direction
    # Animation Timing
    stay_duration: Milliseconds
    # Spacing
    padding: Pixels
    vertical_text_spacing: Pixels
    # Colors
    font_color: Color
    background_color: Color
