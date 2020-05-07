"""
Класс для хранения информации об игровом мире.
"""
import math

from Classes.Subject_Observer import Subject
from Classes.TileFactory import TileFactory
from PlayerClasses.Player import Player


class Map(Subject):
    """
    Конструктор
    """

    def __init__(self, text, tile_size):
        parametrs = text.split("<!!!>")
        player_xy = [int(parametrs[1].split("<!>")[0]), int(parametrs[1].split("<!>")[1])]
        self.player = Player(tile_size, player_xy[0], player_xy[1])

        self.__tiles = []
        y = 0
        for line in parametrs[0].split("\n"):
            x = 0
            for type in line:
                self.__tiles.append(TileFactory.create_tile(int(type), x, y, self))
                x += 1
            y += 1

        self.tile_size = tile_size
        return

    def update(self, t, sec, w, h):
        self.player.update(t, self, sec)
        for tile in self.__tiles:
            if math.fabs(tile.get_x() / 1000 - self.player.get_x() / 1000) < w / self.tile_size / 2 + 2 \
                    and math.fabs(tile.get_y() / 1000 - self.player.get_y() / 1000) < h / self.tile_size / 2 + 2:
                tile.update(t, self, sec)
        return

    def draw(self, screen, texture_manager, w, h):
        window_k = self.tile_size / 1000

        for i in range(5):
            for tile in self.__tiles:
                if tile.get_drawing_order() == i:
                    self.draw_tile(screen,
                                   tile,
                                   window_k,
                                   texture_manager,
                                   self.player.get_x(),
                                   self.player.get_y(), w, h)

        screen.blit(
            texture_manager.get_texture(self.player.get_texture_name()),
            (w/2 - self.player.get_size()*window_k/2, h/2 - self.player.get_size()*window_k/2)
        )

        for i in range(5, 10):
            for tile in self.__tiles:
                if tile.get_drawing_order() == i:
                    self.draw_tile(screen,
                                   tile,
                                   window_k,
                                   texture_manager,
                                   self.player.get_x(),
                                   self.player.get_y(), w, h)

        return

    def get_player(self):
        return self.player

    def get_tiles(self):
        return self.__tiles

    def draw_tile(self, screen, tile, window_k, texture_manager, x, y, w, h):
        if math.fabs(tile.get_x()/1000 - x/1000) < w/self.tile_size/2 + 2 \
                and math.fabs(tile.get_y()/1000 - y/1000) < h/self.tile_size/2 + 2:
            screen.blit(
                texture_manager.get_texture(tile.get_texture_name()),
                (tile.get_x() * window_k - x*window_k
                 + w/2 - self.player.get_size()*window_k/2,
                 tile.get_y() * window_k - y*window_k +
                    h/2 - self.player.get_size()*window_k/2)
            )
        return
