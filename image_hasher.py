import os.path
import binascii
from PIL import Image
import time
from utils import hash_image_generator


class ImageHasher:

    def __init__(self, width: int = 16, height: int = 16) -> None:
        self._size: tuple = [width, height]

    def _load_image(self, path: str):
        if not os.path.exists(path):
            self._image = None

        with Image.open(path) as self._image:
            self._image.load()

    def _resize_image(self):
        if not self._image:
            self._resized = None

        self._resized = self._image.resize(size=self._size)

    def _get_colors(self):
        if not self._resized:
            return None

        _average_color = 0
        _color_map = []
        for w in range(self._size[0]):
            for h in range(self._size[1]):
                c = self._resized.getpixel(xy=[w, h])
                color = int(f"{c[0]}{c[1]}{c[2]}")
                _average_color += color
                _color_map.append(color)

        _average_color = round(_average_color / (self._size[0] * self._size[1]), 0)

        return {"avg": _average_color, "map": _color_map}

    def _get_binary_map(self):
        _map = self._get_colors()

        bicolor_str = ""
        for color in _map["map"]:
            if color > _map["avg"]:
                bicolor_str += "1"
            else:
                bicolor_str += "0"

        self._bicolor_str = bicolor_str
        self._binary_map = int(bicolor_str, 2)

    def _calculate_hash(self):
        self._hash = hex(self._binary_map)[2:]

    def _set_image(self):
        hash_image_generator(self._size[0], self._size[1], self._bicolor_str).show()

    def run(self, path: str):
        self._load_image(path)
        self._resize_image()
        self._get_binary_map()
        self._calculate_hash()

        # <- Временный функционал ->#
        # self._set_image()
        # self._resized.show()
        return self._hash


ImageHasher().run(path=f"C:/Users/oxeek/Downloads/test1.png")
ImageHasher().run(path=f"C:/Users/oxeek/Downloads/test2.png")
ImageHasher().run(path=f"C:/Users/oxeek/Downloads/test3.png")
ImageHasher().run(path=f"C:/Users/oxeek/Downloads/test4.png")
