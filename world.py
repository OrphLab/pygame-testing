import pygame
from tile import Tile, Tilesheet

class World:
    def __init__(self, screen) -> None:
        self.all_tiles = Tile.all_tiles
        self.screen = screen
        self.tilesheet = self.tilsheet = Tilesheet("img/tiles/tileset.png",16,16,23,25,self.screen) 
    
    #draws tile to game
    def draw_world(self, player):
        camera = player.camera
        for tile in self.all_tiles:
            type(tile)
            self.screen.blit(tile.image, (tile.rect.x - camera[0], tile.rect.y - camera[1]))
    
    #draws tiles to mapbuilder
    def draw_world_mb(self, surface, offset):
        for tile in self.all_tiles:
            surface.blit(tile.image, (tile.rect.x-offset[0], tile.rect.y-offset[1]))

    #reads worlddata and pupulates all_tiles group
    def read_world_data(self):
        file = "worlddata.txt"
        with open(file, encoding="utf-8") as f:
            for line in f:
                if line.startswith('sprite{') and line.endswith('}\n'):
                    line = line.replace("sprite{", "").replace("}\n", "")
                    parts = line.split("-")
                    if len(parts) == 2:
                        type = parts[0]
                        pos = tuple(map(int, parts[1].strip("()").split(",")))
                        Tile(type, pos, self.screen, self.tilesheet)
                    else:
                        print("read_worlddata error")
        
