from typing import Optional, Tuple

from pygame import Rect, Surface
from pygame.sprite import Sprite
from pygame.font import Font, get_init, init

from dataflow_animation.settings.config import get_config
from dataflow_animation.types import Dataflow


class BaseObject(Sprite):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.visible = True

        self.image: Surface = None
        self.rect: Rect = None

        self.init()

    def init(self):
        if not self.visible or not self.name:
            return None

        if not get_init():
            init()

        font = Font(get_config().font_name, get_config().font_size)
        self.image = font.render(self.name, True, get_config().font_color)
        self.rect = self.image.get_rect()

    @property
    def position(self) -> Optional[Tuple[int, int]]:
        if not self.rect:
            return None
        return self.rect.center

    @position.setter
    def position(self, value: Tuple[int, int]):
        if self.rect:
            self.rect.center = value

    # pylint: disable=W0221
    def update(self, surface: Surface):
        if not (surface and self.image):
            return None

        surface.blit(self.image, self.rect)


class Entity(BaseObject):
    def __init__(self, animation: Dataflow, *, name: str, level: int):
        super().__init__(name)
        self.level = level

        animation.engine.register(self)

    def __str__(self):
        return f"Entity: '{self.name}' {self.position} level {self.level}"


class Information(BaseObject):
    def __init__(self, animation: Dataflow, *, name: str, starts_at: str):
        super().__init__(name)
        self.starts_at = animation.engine.find_entity(starts_at)

        animation.engine.register(self)

    def __str__(self):
        return (
            f"Information: '{self.name}' "
            f"{self.position} "
            f"Entity({self.starts_at.name}) "
        )
