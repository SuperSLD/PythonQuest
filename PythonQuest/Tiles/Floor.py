from random import randint

from MapClasses.Tile import Tile


class Floor(Tile):
    def __init__(self, x, y):
        super(Floor, self).__init__(x, y)

        self._drawing_order = 3
        self.__type = randint(0, 1)
        self._is_solid = False
        self.__texture_name = ["floor1", "floor2"]
        return

    def get_texture_name(self):
        return self.__texture_name[self.__type]
