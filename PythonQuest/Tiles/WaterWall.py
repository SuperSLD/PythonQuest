from MapClasses.Tile import Tile


class WaterWall(Tile):
    def __init__(self, x, y):
        super(WaterWall, self).__init__(x, y)

        self._drawing_order = 0
        self._is_solid = True
        self._texture_name = ["water_wall", "water_wall2", "water_wall3", "water_wall4", "water_wall5", "water_wall6",
                             "water_wall6", "water_wall5", "water_wall4", "water_wall3", "water_wall2", "water_wall"]
        self.__last_time = 0
        return

    def update(self, t, map, sec):
        self.__last_time = t
        return

    def get_texture_name(self):
        step = int(self.__last_time * 10) % 12
        step_map = self._tile_x % 12
        return self._texture_name[(step + step_map) % 12]