from random import randint

from MapClasses.Tile import Tile


class Wall(Tile):
    def __init__(self, x, y):
        super(Wall, self).__init__(x, y)

        self._drawing_order = 6
        self._is_solid = False
        self.__type = randint(0, 2)
        self.__texture_name = ["wall1", "wall2", "wall3"]
        return

    def get_texture_name(self):
        return self.__texture_name[self.__type]
