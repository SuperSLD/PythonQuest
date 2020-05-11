from MapClasses.Tile import Tile


class Box(Tile):
    def __init__(self, x, y, head, h):
        super(Box, self).__init__(x, y)

        self._head = head
        self._drawing_order = 4
        self._is_solid = False
        self.__texture_name = "box"
        self.__size = 1000
        self.__speed = 3000
        self.__up = True
        self.__horisontal = h
        return

    def update(self, t, map, sec):
        player = map.get_player()

        step = self.__speed * sec
        if step > 200: step = 0
        if not self.__horisontal:
            if self.__up:
                self._y -= step
            else:
                self._y += step
        else:
            if self.__up:
                self._x -= step
            else:
                self._x += step

        if (self._x < player.get_x() < self._x + self.__size
                or self._x < player.get_x() + player.get_size() < self._x + self.__size)\
            and (self._y < player.get_y() + player.get_size()/2 < self._y + self.__size
                or self._y < player.get_y() + player.get_size() < self._y + self.__size):
            player.take_life()

        for tile in map.get_tiles():
            if tile.is_solid():
                if self.__horisontal:
                    if (self._x <= tile.get_x() <= self._x + self.__size
                        or self._x <= tile.get_x() + 1000 <= self._x + self.__size) \
                            and self._y < tile.get_y() + 500 < self._y + self.__size:
                        if not self.__up:
                            self._x -= step
                        else:
                            self._x += step
                        self.__up = not self.__up
                else:
                    if self._x < tile.get_x() + 500 < self._x + self.__size \
                            and (self._y <= tile.get_y() <= self._y + self.__size
                                 or self._y <= tile.get_y() + 1000 <= self._y + self.__size):
                        if not self.__up:
                            self._y -= step
                        else:
                            self._y += step
                        self.__up = not self.__up

        self._head.set_x_y(self._x, self._y - self.__size)
        return

    def set_x_y(self, x, y):
        self._x = x
        self._y = y
        self._head.set_x_y(self._x, self._y - self.__size)
        return

    def get_texture_name(self):
        return self.__texture_name
