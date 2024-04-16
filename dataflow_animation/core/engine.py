from typing import Dict, List
import logging

from pygame import Surface

from dataflow_animation.animations import AnimationStep
from dataflow_animation.objects import BaseObject, Entity, Information
from dataflow_animation.utils.positioning import (
    transform_entities_to_tree,
    set_starting_points,
)


class AnimationManager:
    def __init__(self):
        # Data
        self.entities: Dict[str, Entity] = {}
        self.informations: Dict[str, Information] = {}
        self.animation_steps: List[AnimationStep] = []
        self.surface: Surface = None

        # Logic
        self.entity_tree: List[List[Entity]] = []

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
        set_starting_points(self.entity_tree)

        for entities in self.entity_tree:
            for entity in entities:
                logging.info(
                    "Entity: %s, Position: %s",
                    entity.name,
                    entity.position,
                )
