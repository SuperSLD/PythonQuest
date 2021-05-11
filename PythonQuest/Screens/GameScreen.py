import sys

import pygame

from Classes.Screen import Screen
from MapClasses.LevelManager import LevelManager


class GameScreen(Screen):
    """
    Отрисовка графики отвечающей за игровой процесс.
    """

    def __init__(self, texture_manager, tile_size, length):
        super(GameScreen, self).__init__(texture_manager, tile_size, length)

        self.time = 0

        self.__level_manager = LevelManager(tile_size)
        self.level_list = ["level1", "level2", "level3", "level4", "level5", "level6", "level7", "level8" , "level9"]
        self.level_count = 0
        self.level = self.__level_manager.parse_level(self.level_list[self.level_count])

        self.map = self.level.get_map()
        self.player = self.map.get_player()

        self.elapsed = 0.
        self._WATER = (3, 147, 233)
        self._BLACK = (0, 0, 0)

        print("GameScreen init")
        return

    def draw(self, screen, clock, w, h):
        seconds = self.elapsed / float(1000)
        self.time += seconds
        if self.time > 60 * 10:
            self.time = 0

        if self.map.next_level():
            self.level_count += 1
            print(self.level_count)
            self.level = self.__level_manager.parse_level(self.level_list[self.level_count])
            self.map = self.level.get_map()
            self.player = self.map.get_player()
            self.time = 0

        if self.player.get_life() == 0:
            self.level = self.__level_manager.parse_level(self.level_list[self.level_count])
            self.map = self.level.get_map()
            self.player = self.map.get_player()
            self.time = 0

        if self.level.get_title() is not None:
            screen.fill(self._BLACK)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    break
            title_w = self.level.get_title().get_rect().width/2
            screen.blit(self.level.get_title(), (w/2 - title_w, h/2-20))
            if self.time >= 6:
                self.level.delete_title()
            self.elapsed = clock.tick(60)
        else:
            screen.fill(self._WATER)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    break
                self.player.action(event)

            self.map.update(self.time, seconds, w, h)
            self.map.draw(screen, self._texture_manager, w, h)
            self.level.draw_start_animation(screen, self.time, w, h, self._tile_size, self._texture_manager)
            self.elapsed = clock.tick(60)
