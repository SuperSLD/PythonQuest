from MapClasses.Tile import Tile


class Water(Tile):
    def __init__(self, x, y):
        super(Water, self).__init__(x, y)

        self._drawing_order = 0
        self._is_solid = True
        self._texture_name = ["water", "water2", "water3", "water4", "water5", "water6",
                             "water6", "water5", "water4", "water3", "water2", "water"]
        self.__last_time = 0
        return

    def update(self, t, map, sec):
        self.__last_time = t
        return

    def get_texture_name(self):
        step = int(self.__last_time * 10) % 12
        step_map = self._tile_x % 12
        return self._texture_name[(step + step_map) % 12]
