from typing import Dict, List

from dataflow_animation.objects import Entity, Information
from dataflow_animation.settings.config import get_config
from dataflow_animation.constants import WINDOW
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
    padding = get_config().padding

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
    if get_config().data_direction == Direction.RIGHT:
        return get_right_direction_position(
            main_axis_index,
            main_axis_total,
            cross_axis_index,
            cross_axis_total,
        )


def set_starting_points(
    entity_tree: List[List[Entity]],
    informations: Dict[str, Information],
):
    for main_axis_index, entities_ in enumerate(entity_tree):
        for cross_axis_index, entity in enumerate(entities_):
            entity.position = get_direction_position(
                main_axis_index,
                len(entity_tree),
                cross_axis_index,
                len(entities_),
            )

    for information in informations.values():
        entity_height = information.starts_at.rect.height
        vertical_text_spacing = get_config().vertical_text_spacing
        top_padding = entity_height + vertical_text_spacing
        position_offset = information.starts_at.position
        information.position = (
            position_offset[0],
            position_offset[1] + top_padding,
        )
