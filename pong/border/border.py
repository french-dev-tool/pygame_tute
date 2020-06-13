from enum import Enum


class Border(Enum):
    """Restricts the types that can be supplied to the determine_border_collision func
    """
    RIGHT = 'r'
    TOP = 't'
    BOTTOM = 'b'
