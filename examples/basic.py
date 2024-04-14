from pygame import Surface

from dataflow_animation import Dataflow
from dataflow_animation.objects import Entity, Information


class Animation(Dataflow):
    def __init__(self):
        super().__init__()
        Entity(self, name="A", level=1)
        Entity(self, name="B", level=2)
        Information(
            self,
            name="Information",
            starts_at="A",
        )

    def play(self, surface: Surface):
        pass
