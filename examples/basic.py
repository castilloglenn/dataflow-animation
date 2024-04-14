from dataflow_animation import Dataflow
from dataflow_animation.animations import animate
from dataflow_animation.objects import Entity, Information
from dataflow_animation.constants import CONFIG


class Animation(Dataflow):
    def setup(self):
        # Optional: Override configuration setting
        CONFIG.update(width=1000)

        # Step 1: Create entities and informations
        Entity(self, name="Frontend", level=1)
        Entity(self, name="Backend", level=2)
        Information(
            self,
            name="Data",
            starts_at="Frontend",
        )

        # Step 2: Animate the data flow
        animate(self, info="Data", to="Backend")

        # Final step: Save the file and run the animation
        # Updating the file will apply the changes realtime in the window
