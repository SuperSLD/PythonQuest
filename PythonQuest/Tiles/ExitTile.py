from MapClasses.Tile import Tile


class ExitTile(Tile):
    def __init__(self, x, y):
        super(ExitTile, self).__init__(x, y)

        self._drawing_order = 3
        self._is_solid = False
        self.__texture_name = "exit_tile"
        return

    def update(self, t, map, sec):
        player = map.get_player()
        if (self._x < player.get_x() < self._x + 1000
            or self._x < player.get_x() + player.get_size() < self._x + 1000) \
                and (self._y < player.get_y() + player.get_size()/2 < self._y + 1000
                     or self._y < player.get_y() + player.get_size() < self._y + 1000):
            map.go_to_next_level()
        return

    def get_texture_name(self):
        return self.__texture_name
