from typing import Optional
import logging

import pygame

from dataflow_animation import Dataflow


class PygameRenderer:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.screen = None
        self.clock = None
        self.running = True
        self.animation: Optional[Dataflow] = None

    def set_animation(self, animation):
        self.animation = animation

    def init(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        try:
            self.run()
        except KeyboardInterrupt:
            logging.info("Pygame exiting...")
        finally:
            pygame.quit()
            logging.info("Pygame stopped.")

    def stop(self):
        self.running = False

    def render(self):
        self.screen.fill((0, 0, 0))
        if self.animation:
            self.animation.play(self.animation, self.screen)

        pygame.display.flip()
        self.clock.tick(60)

    def parse_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def loop(self):
        while self.running:
            self.parse_events()
            self.render()

    def run(self):
        try:
            self.loop()
        except pygame.error as e:
            logging.error("Pygame error: %s", e)
