import os
from typing import Optional
import logging

from pygame import Surface
import pygame

from dataflow_animation.constants import CONFIG
from dataflow_animation import Dataflow


class PygameRenderer:
    def __init__(self):
        self.animation: Optional[Dataflow] = None
        self.screen: Surface = None
        self.clock: pygame.time.Clock = None
        self.running = True

    @property
    def is_ready(self):
        if not self.animation:
            return False
        return self.animation.engine.is_ready

    def set_animation(self, animation):
        self.animation = animation
        if self.animation:
            self.build_animation_sequence()

    def init(self):
        os.environ["SDL_VIDEO_WINDOW_POS"] = CONFIG.sdl_video_window_pos
        pygame.init()

        self.screen = pygame.display.set_mode((CONFIG.width, CONFIG.height))
        self.clock = pygame.time.Clock()

        self.run()

    def run(self):
        try:
            while self.running:
                self.parse_events()
                self.render()

        finally:
            pygame.quit()
            logging.info("Pygame stopped.")

    def parse_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render(self):
        self.screen.fill(CONFIG.background_color)

        pygame.display.update()
        self.clock.tick(CONFIG.fps)

    def build_animation_sequence(self):
        if self.animation is None:
            return

        try:
            self.animation.engine.set_surface(self.screen)
            self.animation.setup()

        except pygame.error as e:
            logging.error("Pygame error: %s", e)

        # pylint: disable=W0718
        except Exception as e:
            logging.error(
                "Error building the animations:\n%s: %s",
                type(e).__name__,
                e,
            )
            self.set_animation(None)

    def stop(self):
        self.running = False
