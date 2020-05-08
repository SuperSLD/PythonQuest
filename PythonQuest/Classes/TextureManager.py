import pygame

"""
Класс для управления текстурами.
"""


class TextureManager:
    def __init__(self, tile_size):
        self.__texture_list = []
        self.__tile_size = tile_size

        # Объявление текстур блоков размером tile_size.
        self.__texture_list.append(["null", pygame.image.load('res/images/tiles/null.png')])
        self.__texture_list.append(["floor1", pygame.image.load('res/images/tiles/floor1.png')])
        self.__texture_list.append(["floor2", pygame.image.load('res/images/tiles/floor2.png')])
        self.__texture_list.append(["wall1", pygame.image.load('res/images/tiles/wall1.png')])
        self.__texture_list.append(["wall2", pygame.image.load('res/images/tiles/wall2.png')])
        self.__texture_list.append(["wall3", pygame.image.load('res/images/tiles/wall3.png')])
        self.__texture_list.append(["wall_solid", pygame.image.load('res/images/tiles/wall_solid.png')])
        self.__texture_list.append(["wall_solid2", pygame.image.load('res/images/tiles/wall_solid2.png')])
        self.__texture_list.append(["wall_solid3", pygame.image.load('res/images/tiles/wall_solid3.png')])

        self.__texture_list.append(["water", pygame.image.load('res/images/tiles/water.png')])
        self.__texture_list.append(["water2", pygame.image.load('res/images/tiles/water2.png')])
        self.__texture_list.append(["water3", pygame.image.load('res/images/tiles/water3.png')])
        self.__texture_list.append(["water4", pygame.image.load('res/images/tiles/water4.png')])
        self.__texture_list.append(["water5", pygame.image.load('res/images/tiles/water5.png')])
        self.__texture_list.append(["water6", pygame.image.load('res/images/tiles/water6.png')])

        self.__texture_list.append(["water_wall", pygame.image.load('res/images/tiles/water_wall.png')])
        self.__texture_list.append(["water_wall2", pygame.image.load('res/images/tiles/water_wall2.png')])
        self.__texture_list.append(["water_wall3", pygame.image.load('res/images/tiles/water_wall3.png')])
        self.__texture_list.append(["water_wall4", pygame.image.load('res/images/tiles/water_wall4.png')])
        self.__texture_list.append(["water_wall5", pygame.image.load('res/images/tiles/water_wall5.png')])
        self.__texture_list.append(["water_wall6", pygame.image.load('res/images/tiles/water_wall6.png')])

        self.__texture_list.append(["exit_tile", pygame.image.load('res/images/tiles/exit_tile.png')])

        self.__texture_list.append(["start1", pygame.image.load('res/images/start_animation/start1.png')])
        self.__texture_list.append(["start2", pygame.image.load('res/images/start_animation/start2.png')])
        self.__texture_list.append(["start3", pygame.image.load('res/images/start_animation/start3.png')])
        self.__texture_list.append(["start4", pygame.image.load('res/images/start_animation/start4.png')])
        self.__texture_list.append(["start5", pygame.image.load('res/images/start_animation/start5.png')])
        self.__texture_list.append(["start6", pygame.image.load('res/images/start_animation/start6.png')])
        self.__texture_list.append(["start7", pygame.image.load('res/images/start_animation/start7.png')])
        self.__texture_list.append(["start8", pygame.image.load('res/images/start_animation/start8.png')])

        for v in self.__texture_list:
            v[1] = pygame.transform.scale(v[1], (tile_size, tile_size))

        # Объявление прочих текстур.
        self.__texture_list.append(["player11",
                                    pygame.transform.scale(pygame.image.load('res/images/player/user_standart1_1.png'),
                                                           (int(tile_size*0.7), int(tile_size*0.7)))])
        self.__texture_list.append(["player12",
                                    pygame.transform.scale(pygame.image.load('res/images/player/user_standart1_2.png'),
                                                           (int(tile_size*0.7), int(tile_size*0.7)))])
        self.__texture_list.append(["player21",
                                    pygame.transform.scale(pygame.image.load('res/images/player/user_standart2_1.png'),
                                                           (int(tile_size*0.7), int(tile_size*0.7)))])
        self.__texture_list.append(["player22",
                                    pygame.transform.scale(pygame.image.load('res/images/player/user_standart2_2.png'),
                                                           (int(tile_size*0.7), int(tile_size*0.7)))])
        self.__texture_list.append(["player31",
                                    pygame.transform.scale(pygame.image.load('res/images/player/user_standart3_1.png'),
                                                           (int(tile_size*0.7), int(tile_size*0.7)))])
        self.__texture_list.append(["player32",
                                    pygame.transform.scale(pygame.image.load('res/images/player/user_standart3_2.png'),
                                                           (int(tile_size*0.7), int(tile_size*0.7)))])
        self.__texture_list.append(["player41",
                                    pygame.transform.scale(pygame.image.load('res/images/player/user_standart4_1.png'),
                                                           (int(tile_size*0.7), int(tile_size*0.7)))])
        self.__texture_list.append(["player42",
                                    pygame.transform.scale(pygame.image.load('res/images/player/user_standart4_2.png'),
                                                           (int(tile_size*0.7), int(tile_size*0.7)))])
        return

    def get_texture(self, name):
        for v in self.__texture_list:
            if v[0] == name:
                return v[1]
        return self.get_texture("null")
