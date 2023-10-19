
from tile import Tile
import pygame

class Utills:

    #draws tile to game
    def draw_world(self, player, screen):
        camera = player.camera
        for tile in Tile.all_tiles:
            screen.blit(tile.image, (tile.rect.x - camera[0], tile.rect.y - camera[1]))
    
    #draws tiles to mapbuilder
    def draw_world_mb(self,surface, offset):
        for tile in Tile.all_tiles:
            tile.draw_tile(tile, surface, offset)

    #reads worlddata and pupulates all_tiles group
    def read_world_data(self, screen, tilesheet):
        file = "worlddata.txt"
        with open(file, encoding="utf-8") as f:
            for line in f:
                if line.startswith('sprite{') and line.endswith('}\n'):
                    line = line.replace("sprite{", "").replace("}\n", "")
                    parts = line.split("-")
                    if len(parts) == 2:
                        type = parts[0]
                        pos = tuple(map(int, parts[1].strip("()").split(",")))
                        Tile(type, pos, screen, tilesheet)
                    else:
                        print("read_worlddata error")

#not used, for mose motion
    # def mouse_move_map(self):
    #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
    #         for grid_rect in self.map_builder_ui.grid_rects:
    #             if grid_rect.collidepoint(event.pos):
    #                 self.dragging = True
    #                 self.delta_offset = event.pos[0]-grid_rect.x, event.pos[1]-grid_rect.y
    #         for tile in Tile.all_tiles:
    #             tile_rect = tile.rect
    #             if tile.rect.collidepoint(event.pos):
    #                 self.dragging = True
    #                 self.delta_offset = event.pos[0]-tile_rect.x, event.pos[1]-tile_rect.y
    #     if event.type == pygame.MOUSEBUTTONUP:
    #         self.dragging = False
    #     if event.type == pygame.MOUSEMOTION and self.dragging == True:
    #         self.offset = event.pos[0]-self.delta_offset[0], event.pos[1]-self.delta_offset[1]
        
