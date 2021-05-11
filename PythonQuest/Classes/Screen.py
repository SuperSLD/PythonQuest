class Screen:
    """
    Класс для разделения графических и логических процессов
    при выборе какого-то игрового экрана
    """

    def __init__(self, texture_manager, tile_size, length):
        self._id = length
        self._next_id = length
        self._texture_manager = texture_manager
        self._tile_size = tile_size

        self._FPS = 60

        self._BLACK = (0, 0, 255)
        self._WHITE = (255, 255, 255)
        print("Screen init id= " + str(self._id))
        return

    def draw(self, screen, clock, w, h):
        """
        Отрисовка и обновление окна.
        :param screen: скрин pygame
        :param clock: часы pygame
        :param w: ширина дисплея
        :param h: высота дисплея
        """
        return

    def get_id(self):
        """
        Получение id скрина
        :return: id
        """
        return self._id

    def get_next_screen(self):
        return
