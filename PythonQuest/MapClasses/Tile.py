from Classes.Subject_Observer import Observer


class Tile(Observer):
    def __init__(self, x, y):
        self._x = x*1000
        self._y = y*1000
        self._tile_x = x
        self._tile_y = y
        self._is_solid = False
        self._drawing_order = 5
        self._texture = "null"
        return

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def is_solid(self):
        return self._is_solid

    def get_drawing_order(self):
        return self._drawing_order

    def get_texture_name(self):
        return self._texture
