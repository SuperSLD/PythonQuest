import pygame

from MapClasses.Map import Map


class Level:
    def __init__(self, text, tile_size):
        self.__map = Map(text, tile_size)

        config = text.split("<!!!>")
        if config[2].replace("\n", "") != "null":
            font = pygame.font.SysFont('arial', 30)
            title = font.render(config[2].replace("\n", ""), 0, (255, 255, 255))
            self.__title = title
        else:
            self.__title = None

        self.__start_texture = ["start8", "start7", "start6", "start5",
                                "start4", "start3", "start2", "start1"]
        self._animation_run = True
        self.count = 0

    def get_map(self):
        return self.__map

    def get_title(self):
        return self.__title

    def delete_title(self):
        self.__title = None

    def draw_start_animation(self, screen, t, w, h, tile_size, tm):
        self.count += 1
        if self._animation_run:
            step = int(self.count / 1.5)
            texture = self.__start_texture[step % 8]
            if step % 8 == 7:
                self._animation_run = False

            for x in range(int(w/tile_size)+1):
                for y in range(int(h/tile_size)+1):
                    screen.blit(
                        tm.get_texture(texture),
                        (x*tile_size, y*tile_size)
                    )
            for x in range(int(w/tile_size)+2):
                for y in range(int(h/tile_size)+2):
                    screen.blit(
                        tm.get_texture(texture),
                        ((x-1)*tile_size - tile_size/2, (y-1)*tile_size - tile_size/2)
                    )
        return
