from typing import List

from dataflow_animation.objects import Entity
from dataflow_animation.constants import CONFIG, WINDOW
from dataflow_animation.types import Coordinates


def get_right_direction_position(
    main_axis_index: int,
    main_axis_total: int,
    cross_axis_index: int,
    cross_axis_total: int,
) -> Coordinates:
    padding = CONFIG.padding

    main_axis_length = WINDOW.width - 2 * padding
    cross_axis_length = WINDOW.height - 2 * padding

    main_axis_length = WINDOW.width - 2 * padding
    main_axis_spacing = main_axis_length / (main_axis_total + 1)
    x_position = padding + (main_axis_index + 1) * main_axis_spacing

    cross_axis_length = WINDOW.height - 2 * padding
    cross_axis_spacing = cross_axis_length / (cross_axis_total + 1)
    y_position = padding + (cross_axis_index + 1) * cross_axis_spacing

    return (x_position, y_position)


def set_starting_points(entity_tree: List[List[Entity]]):
    pass
