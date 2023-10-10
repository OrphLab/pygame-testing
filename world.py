import pygame
from tile import Tile, Tilesheet
from player import Player

class World:
    def __init__(self, screen) -> None:
        self.tilsheet = Tilesheet("img/tiles/tileset.png",16,16,23,25,screen)  
        self.screen = screen
        self.world_tiles = self.read_worlddata() 


    def draw_world(self, player):
        camera = player.camera
        for tile in self.world_tiles:
            self.screen.blit(tile.image, (tile.rect.x - camera[0], tile.rect.y - camera[1]))
        print("world: ", camera[0], camera[1])
        
#        self.tilsheet.draw_tilesheet()

    def read_worlddata(self) -> list:
        world_data = pygame.sprite.Group()
        file = "worlddata.txt"
        with open(file, encoding="utf-8") as f:
            for line in f:
                if line.startswith('sprite{') and line.endswith('}\n'):
                    line = line.replace("sprite{", "").replace("}\n", "")
                    parts = line.split("-")
                    if len(parts) == 2:
                        type = parts[0]
                        pos = tuple(map(int, parts[1].strip("()").split(",")))
                        tile = Tile(type, pos, self.screen, self.tilsheet)
                        world_data.add(tile)
                    else:
                        print("read_worlddata error")
        return world_data


