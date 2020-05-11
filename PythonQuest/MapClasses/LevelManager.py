from MapClasses.Level import Level


class LevelManager:
    """
    Управление уровнями
    """

    def __init__(self, tile_size):
        self.__tile_size = tile_size
        return

    def parse_level(self, name):
        """
        Создание уровня по файлу
        :param name: название уровня
        :return: уровень
        """
        f = open('res/levels/'+name+".lvl", 'r')
        text = ""
        for line in f:
            text += line
        level = Level(text, self.__tile_size)
        return level
