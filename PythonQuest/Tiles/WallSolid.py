from random import randint

from MapClasses.Tile import Tile


class WallSolid(Tile):
    def __init__(self, x, y):
        super(WallSolid, self).__init__(x, y)
        self._drawing_order = 4
        self._is_solid = True
        self.__type = randint(0, 2)
        self.__texture_name = ["wall_solid", "wall_solid2", "wall_solid3"]
        return

    def get_texture_name(self):
        return self.__texture_name[self.__type]
