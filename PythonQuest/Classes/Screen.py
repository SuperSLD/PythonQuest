class Screen:
    def __init__(self, texture_manager, tile_size, length):
        self._id = length
        self._texture_manager = texture_manager
        self._tile_size = tile_size

        self._FPS = 60

        self._BLACK = (0, 0, 255)
        self._WHITE = (255, 255, 255)
        print("Screen init id= " + str(self._id))
        return

    def draw(self, screen, clock, w, h):
        return

    def get_id(self):
        return self._id
