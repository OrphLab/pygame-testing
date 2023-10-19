import pygame
from utills import Utills
from player import Player
from mapbuilderui import MapBuilderUI
from tile import Tile, Tilesheet

class Game:
    def __init__(self, size:tuple, type:str = None) -> None:
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.type = type
        self.running = False
        self.tilesheet = Tilesheet("img/tiles/tileset.png",16,16,23,25,self.screen) 
        self.player = Player((250,400), self.screen, Tile.all_tiles)
        self.map_builder_ui = MapBuilderUI(self.screen, self.tilesheet)
        self.utills = Utills()
        self.offset = [100,100]
        self.delta_offset = [] #mouse motion
        self.dragging = False   #mouse motion

        self.tilesheet.draw_tile_list()
        self.utills.read_world_data(self.screen, self.tilesheet)

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
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.offset = self.map_builder_ui.move_map(self.offset, event)

            if self.type == None:
            
                self.player.update()
                self.utills.draw_world(self.player, self.screen)
            
            if self.type == "Building":
                self.map_builder_ui.update()
                self.map_builder_ui.draw_rect_grid(self.offset)
                self.utills.draw_world_mb(self.map_builder_ui.mainsrf, self.offset)
                self.map_builder_ui.tile_highlight(pygame.mouse.get_pos(), self.offset)
                
            pygame.display.update()

pygame.quit() 