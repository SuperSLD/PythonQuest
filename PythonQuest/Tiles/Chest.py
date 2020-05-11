from MapClasses.Tile import Tile


class Chest(Tile):
    def __init__(self, x, y):
        super(Chest, self).__init__(x, y)

        self._drawing_order = 6
        self._is_solid = True
        self.__texture_name = "chest"
        return

    def get_texture_name(self):
        return self.__texture_name
