from enum import Enum


class Path(Enum):
    LINEAR = 0


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class MovementStatus(Enum):
    INITIAL = 0
    MOVING = 1
    STOPPED = 2
    FINISHED = 3
