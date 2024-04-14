from typing import Optional

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

    def init(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.run()

    def set_animation(self, animation):
        self.animation = animation

    def run(self):
        try:
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                self.screen.fill((0, 0, 0))
                if self.animation:
                    self.animation.play(self.animation, self.screen)

                pygame.display.flip()
                self.clock.tick(60)
        except pygame.error:
            pass
        except KeyboardInterrupt:
            pass
        finally:
            pygame.quit()

    def stop(self):
        self.running = False
