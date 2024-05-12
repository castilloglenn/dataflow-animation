from dataclasses import dataclass

from dataflow_animation.objects import Entity, Information

from dataflow_animation.types import Milliseconds
from dataflow_animation.enums import MovementStatus, Path


@dataclass
class AnimationStep:
    information: Information
    entity: Entity
    path: Path
    duration: Milliseconds

    def __post_init__(self):
        self.starting_point = self.information.position
        self.ending_point = self.entity.position

    def __str__(self):
        return self.name

    @property
    def name(self):
        return f"(Linear) {self.information.name} -> {self.entity.name}"

    @property
    def movement_status(self) -> MovementStatus:
        return self.information.movement_status

    @movement_status.setter
    def movement_status(self, status: MovementStatus):
        self.information.movement_status = status


def animate(
    animation,
    *,
    info: Information,
    to: Entity,
    path: Path = Path.LINEAR,
    duration: Milliseconds = 1000,
):
    information = animation.engine.find_information(info)
    entity = animation.engine.find_entity(to)
    animation.engine.register(
        AnimationStep(information, entity, path, duration),
    )
