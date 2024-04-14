"""
This example demonstrates how to create a simple animation using the Dataflow
abstract class. It directly uses pygame to draw the animation to show how the
library functions, where in other examples they will utilize dataflow
animations to make it easier to use.
"""

import pygame

from dataflow_animation import Dataflow


class Animation(Dataflow):
    def setup(self):
        pass

    def play(self, surface):
        pygame.draw.circle(surface, (122, 0, 126), (400, 300), 50)
        pygame.draw.circle(surface, (0, 32, 84), (100, 375), 50)
        pygame.draw.circle(surface, (128, 96, 0), (525, 100), 25)
