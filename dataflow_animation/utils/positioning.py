from typing import Dict, List

from dataflow_animation.objects import Entity
from dataflow_animation.constants import CONFIG, WINDOW
from dataflow_animation.types import Coordinates
from dataflow_animation.enums import Direction


def transform_entities_to_tree(
    entities: Dict[str, Entity],
) -> List[List[Entity]]:
    entity_tree = []

    for entity in entities.values():
        while entity.level > len(entity_tree):
            entity_tree.append([])

        entity_tree[entity.level - 1].append(entity)

    return entity_tree


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

    return (int(x_position), int(y_position))


def get_direction_position(
    main_axis_index: int,
    main_axis_total: int,
    cross_axis_index: int,
    cross_axis_total: int,
) -> Coordinates:
    if CONFIG.data_direction == Direction.RIGHT:
        return get_right_direction_position(
            main_axis_index,
            main_axis_total,
            cross_axis_index,
            cross_axis_total,
        )


def set_starting_points(entity_tree: List[List[Entity]]):
    for main_axis_index, entities in enumerate(entity_tree):
        for cross_axis_index, entity in enumerate(entities):
            entity.position = get_direction_position(
                main_axis_index,
                len(entity_tree),
                cross_axis_index,
                len(entities),
            )
