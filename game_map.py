import numpy as np
from tcod.console import Console

import tile_types


class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.floor, order='F')

        self.tiles[30:33, 33] = tile_types.wall

    def in_bounds(self, x: int, y: int):
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console):
        console.rgb[0:self.width, 0:self.height] = self.tiles["dark"]
