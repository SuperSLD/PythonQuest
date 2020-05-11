import os
import sys

import pygame

from Classes.TextureManager import TextureManager
from Screens.GameScreen import GameScreen

successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))

win_w = 1280
win_h = 700
tile_size = int(win_h/14)

# screen = pygame.display.set_mode((win_w, win_h), pygame.DOUBLEBUF | pygame.FULLSCREEN)
screen = pygame.display.set_mode((win_w, win_h), pygame.DOUBLEBUF)
clock = pygame.time.Clock()


texture_manager = TextureManager(tile_size)

# Создание игровых окон (не стал разбираться как он  работают в pygame, поэтому сделал свои)
screen_list = []
screen_list.append(GameScreen(texture_manager, tile_size, len(screen_list)))
select_screen = 0

while True:
    for game_screen in screen_list:
        if game_screen.get_id() == select_screen:
            game_screen.draw(screen, clock, win_w, win_h)
    pygame.display.update()

print("Exited the game loop. Game will quit...")
quit()