from dataflow_animation.objects import Entity, Information

from dataflow_animation.enums import Path


class AnimationStep:
    def __init__(self, entity: Entity, information: Information, path: Path):
        self.entity = entity
        self.information = information
        self.path = path
