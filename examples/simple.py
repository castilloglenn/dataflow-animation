import pygame

from dataflow import Dataflow


class Animation(Dataflow):
    def setup(self):
        pass

    def play(self, surface):
        pygame.draw.circle(surface, (0, 255, 255), (400, 300), 50)
        pygame.draw.circle(surface, (255, 0, 0), (100, 375), 50)
        pygame.draw.circle(surface, (0, 255, 0), (525, 100), 25)
