from typing import Optional, Tuple

from pygame import Surface
from pygame.sprite import Sprite
from pygame.font import Font

from dataflow_animation.constants import CONFIG
from dataflow_animation.types import Dataflow


class BaseObject(Sprite):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.visible = True

    @property
    def image(self) -> Optional[Surface]:
        if not self.visible or not self.name:
            return None

        font = Font(CONFIG.font_name, CONFIG.font_size)
        text_surface = font.render(self.name, True, CONFIG.font_color)
        return text_surface

    @property
    def rect(self) -> Optional[Surface]:
        if not self.image:
            return None
        return self.image.get_rect()

    @property
    def position(self) -> Optional[Tuple[int, int]]:
        if not self.rect:
            return None
        return self.rect.topleft

    @position.setter
    def position(self, value: Tuple[int, int]):
        if self.rect:
            self.rect.topleft = value

    # pylint: disable=W0221
    def update(self, surface: Surface):
        if not (self.image and self.rect):
            return

        surface.blit(self.image, self.rect)


class Entity(BaseObject):
    def __init__(self, animation: Dataflow, *, name: str, level: int):
        super().__init__(name)
        self.level = level

        animation.engine.register(self)


class Information(BaseObject):
    def __init__(self, animation: Dataflow, *, name: str, starts_at: str):
        super().__init__(name)
        self.starts_at = animation.engine.find_entity(starts_at)

        animation.engine.register(self)
