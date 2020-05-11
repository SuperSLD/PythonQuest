import pygame

from Classes.Subject_Observer import Observer
from Tiles.Box import Box


class Player(Observer):
    def __init__(self, tile_size, x, y):
        self.__n = [0, 0, 0, 0]
        self.__last_n = 4
        self.__tile_size = 1000
        self.__texture = ["player11", "player12", "player21", "player22",
                          "player31", "player32", "player41", "player42"]
        self.__x = x * 1000
        self.__y = y * 1000
        self.__size = 700
        self.__tile_x = int(self.__x / 1000)
        self.__tile_y = int(self.__y / 1000)
        self.__speed = 5000
        self.__last_time = 0
        self.__last_move = 0
        self.__life = 1
        return

    def action(self, event):
        """
        Реакция на надатие кнопок.
        :param event: event
        :return:
        """
        keys = [pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s]
        if event.type == pygame.KEYDOWN:
            for i in range(len(keys)):
                if event.key == keys[i]:
                    self.__n[i] = i+1
                    self.__last_n = i+1
        if event.type == pygame.KEYUP:
            for i in range(len(keys)):
                if event.key == keys[i]:
                    self.__n[i] = 0
        return

    def update(self, t, map, sec):
        self.__last_move = sec * self.__speed
        step = self.__speed*sec
        if step > 200:
            step = 0
            self.__last_move = 0
        for n in self.__n:
            if n > 0:
                if n == 1:
                    self.__x -= step
                    self.__last_n = 1
                elif n == 2:
                    self.__y -= step
                    self.__last_n = 2
                elif n == 3:
                    self.__x += step
                    self.__last_n = 3
                elif n == 4:
                    self.__y += step
                    self.__last_n = 4

        for tile in map.get_tiles():
            if tile.is_solid():
                if tile.get_x() + self.__last_move >= self.__x + self.__size >= tile.get_x() and \
                        (tile.get_y() < self.__y + self.__size/2 < tile.get_y() + 1000 or tile.get_y() < self.__y + self.__size < tile.get_y() + 1000):
                    self.__x = tile.get_x() - self.__size - 1
                if tile.get_x() + 1000 >= self.__x >= tile.get_x() + 1000 - self.__last_move and \
                        (tile.get_y() < self.__y + self.__size/2 < tile.get_y() + 1000 or tile.get_y() < self.__y + self.__size < tile.get_y() + 1000):
                    self.__x = tile.get_x() + 1000 + 1

                if tile.get_y() + self.__last_move >= self.__y + self.__size >= tile.get_y() and \
                        (tile.get_x() < self.__x < tile.get_x()+1000 or tile.get_x() < self.__x + self.__size < tile.get_x()+1000):
                    self.__y = tile.get_y() - self.__size - 1
                if tile.get_y() + 1000 >= self.__y + self.__size/2 >= tile.get_y() + 1000 - self.__last_move and \
                        (tile.get_x() < self.__x < tile.get_x()+1000 or tile.get_x() < self.__x + self.__size < tile.get_x()+1000):
                    self.__y = tile.get_y() + 1000 - self.__size/2 + 1

        self.__tile_x = int(self.__x / self.__tile_size)
        self.__tile_y = int(self.__y / self.__tile_size)
        self.__last_time = t
        return

    def get_last_move(self):
        return self.__last_move*1.3

    def get_texture_name(self):
        step = int(self.__last_time*10) % 2
        position = (self.__last_n - 1)*2
        return self.__texture[position + step]

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_speed(self):
        return self.__speed

    def get_size(self):
        return self.__size

    def get_life(self):
        return self.__life

    def take_life(self):
        self.__life -= 1
        return
