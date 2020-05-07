from MapClasses.Map import Map


class Level:
    def __init__(self, text, tile_size):
        self.__map = Map(text, tile_size)

    def get_map(self):
        return self.__map
