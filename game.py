import pygame
from world import World
from player import Player
from builderui import BuilderUI

class Game:
    def __init__(self, size:tuple, type:str = None) -> None:
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = False
        self.world = World(self.screen)
        self.player = Player((250,400), self.screen, self.world.world_tiles)
        self.type = type
        self.map_building_srf = BuilderUI(self.screen)
        self.dragging = False
        self.offset = [0,0]
        self.delta_offset = []
        
    def run(self):
        self.running = True
        
        while self.running:
            events = pygame.event.get()
            self.clock.tick(self.fps)
            self.screen.fill((110,25,255))

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_1:
                        print("one was pressed")
               #TODO rewrite the two for loops into functions
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    for grid_rect in self.map_building_srf.grid_rects:
                        if grid_rect.collidepoint(event.pos):
                            self.dragging = True
                            self.delta_offset = event.pos[0]-grid_rect.x, event.pos[1]-grid_rect.y
                    for tile in self.world.world_tiles:
                        tile_rect = tile.rect
                        if tile.rect.collidepoint(event.pos):
                            self.dragging = True
                            self.delta_offset = event.pos[0]-tile_rect.x, event.pos[1]-tile_rect.y
                if event.type == pygame.MOUSEBUTTONUP:
                    self.dragging = False
                if event.type == pygame.MOUSEMOTION and self.dragging == True:
                    self.offset = event.pos[0]-self.delta_offset[0], event.pos[1]-self.delta_offset[1]

            if self.type == None:
            
                self.player.update()
                self.world.draw_world(self.player)
            
            if self.type == "Building":
                self.map_building_srf.update()
                self.map_building_srf.draw_rect_grid(self.offset)
                self.world.draw_world_mb(self.map_building_srf.mainsrf, self.offset)
                self.map_building_srf.tile_highlight(pygame.mouse.get_pos(), self.offset)
                
            pygame.display.update()

pygame.quit() 

        