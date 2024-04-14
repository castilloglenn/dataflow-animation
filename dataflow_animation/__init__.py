"""
Dataflow is an innovative Python library designed to simplify the visualization
of data flows through real-time animations. Utilizing Pygame for rendering and
Watchdog for live updates, Dataflow makes it effortless to develop, visualize,
and refine complex data flow animations dynamically. This library is
particularly useful for developers and analysts who need to create and present
data-driven animations and diagrams that are both informative and visually
engaging. With Dataflow, users can write Python code to define animations and
see changes reflected instantaneously on the screen, making it an ideal tool
for rapid prototyping of data flow diagrams and animations.
"""

from abc import ABC, abstractmethod
from typing import Dict
import logging

from dataflow_animation.objects import BaseObject, Entity, Information


class Dataflow(ABC):
    """
    The Dataflow abstract class defines the structure of a data flow animation
    script. This class must be inherited by a subclass that implements the
    __init__() and play() methods. The __init__() method is used to define the
    entities and resources required for the animation, while the play() method
    is used to render the animation to the screen. By following this structure,
    users can create custom data flow animations that can be easily integrated
    into their projects.
    """

    @abstractmethod
    def __init__(self):
        """Setup the entities and resources for the animation."""
        self.entities: Dict[str, Entity] = {}
        self.informations: Dict[str, Information] = {}

    @abstractmethod
    def play(self, surface):
        """Play the animation script to the window."""

    def find_entity(self, name: str) -> Entity:
        """Find an entity by name."""
        entity = self.entities.get(name)
        if not entity:
            raise ValueError(f"Entity not found: {name}")
        return entity

    def find_information(self, name: str) -> Information:
        """Find an information by name."""
        information = self.informations.get(name)
        if not information:
            raise ValueError(f"Information not found: {name}")
        return information

    def register(self, instance: BaseObject):
        """Register an object with the animation."""
        if isinstance(instance, Entity):
            self.entities[instance.name] = instance
        elif isinstance(instance, Information):
            self.informations[instance.name] = instance

        logging.info(
            "Registered: %s %s",
            instance.__class__.__name__,
            instance.name,
        )
