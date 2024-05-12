from dataflow_animation.types import Coordinates


def get_relative_position(
    a: Coordinates, b: Coordinates, distance: float
) -> Coordinates:
    x = a[0] + (b[0] - a[0]) * distance
    y = a[1] + (b[1] - a[1]) * distance
    return (round(x), round(y))
