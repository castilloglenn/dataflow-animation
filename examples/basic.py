from dataflow_animation import Dataflow
from dataflow_animation.animations import animate
from dataflow_animation.objects import Entity, Information
from dataflow_animation.constants import CONFIG


class Animation(Dataflow):
    def setup(self):
        CONFIG.update(width=1000)

        Entity(self, name="Frontend", level=1)
        Entity(self, name="Backend", level=2)
        Information(
            self,
            name="Data",
            starts_at="Frontend",
        )

        animate(self, info="Data", to="Backend")
