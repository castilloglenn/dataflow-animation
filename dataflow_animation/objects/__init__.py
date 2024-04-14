from typing import Optional, Tuple

from pygame import Surface
from pygame.sprite import Sprite
from pygame.font import Font

from dataflow_animation.settings.config import get_config

CONFIG = get_config()


class BaseObject(Sprite):
    def __init__(self, collection, name: str):
        super().__init__()
        self.collection = collection
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
    def __init__(self, collection, *, name: str, level: int):
        super().__init__(collection, name)
        self.level = level

        collection.register(self)

    def __str__(self):
        return f"Entity: {self.name} (Level {self.level})"

    def __eq__(self, other):
        if not isinstance(other, Entity):
            return False
        return self.name == other.text and self.level == other.level


class Information(BaseObject):
    def __init__(self, collection, *, name: str, starts_at: str):
        super().__init__(collection, name)
        self.starts_at = collection.find_entity(starts_at)

        collection.register(self)

    def __str__(self):
        return f"Information: {self.name} (Starts at {self.starts_at})"

    def __eq__(self, other):
        if not isinstance(other, Information):
            return False
        return self.name == other.text and self.starts_at == other.starts_at
