import sys

import pygame

from Classes.Screen import Screen
from MapClasses.LevelManager import LevelManager
from MapClasses.Map import Map
from PlayerClasses.Player import Player


class GameScreen(Screen):
    def __init__(self, texture_manager, tile_size, length):
        super(GameScreen, self).__init__(texture_manager, tile_size, length)

        self.time = 0

        self.__level_manager = LevelManager(tile_size)
        self.level = self.__level_manager.parse_level("level1")

        self.map = self.level.get_map()
        self.player = self.map.get_player()

        self.elapsed = 0.
        self._BLACK = (3, 147, 233)
        print("GameScreen init")
        return

    def draw(self, screen, clock, w, h):
        seconds = self.elapsed / 1000.0
        self.time += seconds
        if self.time > 60 * 10:
            self.time = 0
        screen.fill(self._BLACK)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                break
            self.player.action(event)

        self.map.update(self.time, seconds, w, h)
        self.map.draw(screen, self._texture_manager, w, h)
        self.elapsed = clock.tick(60)
