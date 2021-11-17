from enum import Enum
from typing import Tuple

import cv2


class Color(Enum):
    RED = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLUE = (255, 0, 0)


def draw_text(img,
              text: str,
              coords: Tuple[int, int] = (100, 100),
              font=cv2.FONT_HERSHEY_PLAIN,
              font_size: float = 3,
              color: Color = Color.GREEN,
              thickness: int = 2):
    cv2.putText(img,
                text, coords,
                font, font_size,
                color.value, thickness)


def draw_rectangle(img,
                   left_top_coords: Tuple[int, int],
                   right_bottom_coords: Tuple[int, int],
                   color: Color = Color.GREEN,
                   thickness: int = 2):
    cv2.rectangle(img, left_top_coords, right_bottom_coords, color.value, thickness)
