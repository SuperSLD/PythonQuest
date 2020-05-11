from MapClasses.Tile import Tile


class BoxHead(Tile):
    def __init__(self, x, y):
        super(BoxHead, self).__init__(x, y)

        self._drawing_order = 6
        self._is_solid = False
        self.__texture_name = "box_head"
        return

    def set_x_y(self, x, y):
        self._x = x
        self._y = y
        return

    def get_texture_name(self):
        return self.__texture_name
