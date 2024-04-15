from dataflow_animation import Dataflow
from dataflow_animation.animations import animate
from dataflow_animation.objects import Entity, Information
from dataflow_animation.constants import CONFIG


class Animation(Dataflow):
    def setup(self):
        # Optional: Override configuration setting
        CONFIG.update(
            width=400,
            height=400,
            background_color=(255, 255, 255),
        )

        # Step 1: Create entities and informations
        Entity(self, name="Web App", level=1)
        Entity(self, name="Mobile App", level=1)
        Entity(self, name="Backend", level=2)

        Information(
            self,
            name="Request",
            starts_at="Web App",
        )

        # Step 2: Animate the data flow
        animate(self, info="Request", to="Backend")

        # Final step: Save the file and run the animation
        # Updating the file will apply the changes realtime in the window
