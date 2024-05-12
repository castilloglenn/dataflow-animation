from typing import Dict, List, Optional
import logging

from pygame import Surface
from pygame.sprite import Group

from dataflow_animation.animations import AnimationStep
from dataflow_animation.enums import MovementStatus
from dataflow_animation.objects import BaseObject, Entity, Information
from dataflow_animation.types import Milliseconds

from dataflow_animation.settings.config import get_config
from dataflow_animation.utils.math import get_relative_position
from dataflow_animation.utils.positioning import (
    transform_entities_to_tree,
    set_starting_points,
)
from dataflow_animation.utils.statuses import get_next_status, is_stay_status


class AnimationManager:
    def __init__(self):
        # Data
        self.entities: Dict[str, Entity] = {}
        self.informations: Dict[str, Information] = {}
        self.animation_steps: List[AnimationStep] = []
        self.surface: Surface = None

        # Logic
        self.entity_tree: List[List[Entity]] = []
        self.group: Group = Group()
        self.tick_accumulator: Milliseconds = 0
        self.animation_step: Optional[AnimationStep] = None
        self.animation_step_index: int = 0

    @property
    def is_ready(self):
        return all(
            [
                self.entities,
                self.informations,
                self.animation_steps,
            ]
        )

    def set_surface(self, surface: Surface):
        self.surface = surface

    def find_entity(self, name: str) -> Entity:
        entity = self.entities.get(name)
        if not entity:
            raise ValueError(f"Entity not found: {name}")
        return entity

    def find_information(self, name: str) -> Information:
        information = self.informations.get(name)
        if not information:
            raise ValueError(f"Information not found: {name}")
        return information

    def register(self, instance: BaseObject):
        if isinstance(instance, Entity):
            self.entities[instance.name] = instance
        elif isinstance(instance, Information):
            self.informations[instance.name] = instance
        elif isinstance(instance, AnimationStep):
            self.animation_steps.append(instance)

        logging.info(
            "Registered: %s %s",
            instance.__class__.__name__,
            instance.name,
        )

    def setup(self):
        self.build_entity_tree()

    def build_entity_tree(self):
        self.entity_tree = transform_entities_to_tree(self.entities)
        set_starting_points(self.entity_tree, self.informations)

        for entity in self.entities.values():
            logging.info(entity)
            self.group.add(entity)

        for information in self.informations.values():
            logging.info(information)
            self.group.add(information)

    def render(self, tick_duration: Milliseconds):
        self.tick_accumulator += tick_duration
        self.group.update(self.surface)

    def update_positions(self):
        if self.is_finished_status():
            return

        if is_stay_status(self.animation_step.movement_status):
            self.calculate_stay_status()
            return

        self.calculate_moving_status()

    def is_finished_status(self) -> bool:
        if self.animation_step.movement_status == MovementStatus.FINISHED:
            self.animation_step = None
            return True
        return False

    def calculate_stay_status(self):
        if self.tick_accumulator >= get_config().stay_duration:
            self.tick_accumulator -= get_config().stay_duration
            self.animation_step.movement_status = get_next_status(
                current_status=self.animation_step.movement_status,
                path=self.animation_step.path,
            )

    def calculate_moving_status(self):
        self.animation_step.information.position = get_relative_position(
            a=self.animation_step.starting_point,
            b=self.animation_step.ending_point,
            distance=self.tick_accumulator / self.animation_step.duration,
        )

        if self.tick_accumulator >= self.animation_step.duration:
            self.tick_accumulator -= self.animation_step.duration
            self.animation_step.movement_status = get_next_status(
                current_status=self.animation_step.movement_status,
                path=self.animation_step.path,
            )
