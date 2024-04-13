from abc import ABC, abstractmethod


class Dataflow(ABC):
    @abstractmethod
    def setup(self):
        """Setup the entities and resources for the animation."""

    @abstractmethod
    def play(self, surface):
        """Play the animation script to the window."""
