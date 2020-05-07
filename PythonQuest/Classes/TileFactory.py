from Tiles.Floor import Floor
from Tiles.Wall import Wall
from Tiles.WallSolid import WallSolid
from Tiles.Water import Water
from Tiles.WaterWall import WaterWall


class TileFactory:
    @staticmethod
    def create_tile(code, x, y, map):
        if code == 0:
            return Water(x, y)
        elif code == 1:
            return Floor(x, y)
        elif code == 2:
            map.get_tiles().append(Wall(x, y - 1))
            return WallSolid(x, y)
        elif code == 3:
            return WaterWall(x, y)

        return None
