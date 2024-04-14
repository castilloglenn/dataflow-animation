import os
from typing import Optional
import logging

from pygame import Surface
import pygame

from dataflow_animation.settings.config import get_config
from dataflow_animation import Dataflow


CONFIG = get_config()


class PygameRenderer:
    def __init__(self):
        self.animation: Optional[Dataflow] = None
        self.screen: Surface = None
        self.clock: pygame.time.Clock = None
        self.running = True

    def set_animation(self, animation):
        self.animation = animation

    def play_animation(self):
        if self.animation is None:
            return

        try:
            self.animation.play(self.screen)

        except pygame.error as e:
            logging.error("Pygame error: %s", e)

        # pylint: disable=W0718
        except Exception as e:
            logging.error(
                "Error playing animation:\n%s: %s",
                type(e).__name__,
                e,
            )
            self.set_animation(None)

    def init(self):
        os.environ["SDL_VIDEO_WINDOW_POS"] = CONFIG.sdl_video_window_pos
        pygame.init()

        self.screen = pygame.display.set_mode((CONFIG.width, CONFIG.height))
        self.clock = pygame.time.Clock()

        try:
            self.run()
        finally:
            pygame.quit()
            logging.info("Pygame stopped.")

    def stop(self):
        self.running = False

    def parse_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render(self):
        self.screen.fill(CONFIG.background_color)
        self.play_animation()

        pygame.display.update()
        self.clock.tick(CONFIG.fps)

    def run(self):
        try:
            while self.running:
                self.parse_events()
                self.render()

        except pygame.error as e:
            logging.error("Pygame error: %s", e)

        except KeyboardInterrupt:
            logging.info("Pygame exiting...")
