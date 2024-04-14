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


class Dataflow(ABC):
    """
    The Dataflow abstract class defines the structure of a data flow animation
    script. This class must be inherited by a subclass that implements the
    setup() and play() methods. The setup() method is used to define the
    entities and resources required for the animation, while the play() method
    is used to render the animation to the screen. By following this structure,
    users can create custom data flow animations that can be easily integrated
    into their projects.
    """

    @abstractmethod
    def setup(self):
        """Setup the entities and resources for the animation."""

    @abstractmethod
    def play(self, surface):
        """Play the animation script to the window."""
