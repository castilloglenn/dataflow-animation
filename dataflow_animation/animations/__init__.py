from dataclasses import dataclass

from dataflow_animation.objects import Entity, Information

from dataflow_animation.enums import Path


@dataclass
class AnimationStep:
    information: Information
    entity: Entity
    path: Path
    duration: int

    @property
    def name(self):
        return f"{self.information.name} -> {self.entity.name}"


def animate(
    collection,
    *,
    info: Information,
    to: Entity,
    path: Path = Path.LINEAR,
    duration: int = 1000,
):
    information = collection.find_information(info)
    entity = collection.find_entity(to)
    collection.register(AnimationStep(information, entity, path, duration))
