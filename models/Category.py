from dataclasses import dataclass
import models.enums.Color as Color

@dataclass
class Category:
    title: str = ""
    color: Color = None
    image: str = "" # Link to image

    