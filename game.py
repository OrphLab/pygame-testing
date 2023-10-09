import pygame
from world import World
from player import Player
from builderui import MainSurface

class Game:
    def __init__(self, size, type = None) -> None:
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = False
        self.world = World(self.screen)
        self.player = Player((250,400), self.screen, self.world.world_tiles)
        self.type = type
        self.mainsrf = MainSurface(self.screen)
        

    def run(self):
        self.running = True
        
        while self.running:
            self.clock.tick(self.fps)
            self.screen.fill((110,25,255))
            player_camera_x  = self.player.camera[0]
            player_camera_y  = self.player.camera[1]
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            if self.type == None:
                self.player.update()
                self.world.draw_world(self.player)
            elif self.type == "Testing":
                self.mainsrf.drawmainsrf()
                self.mainsrf.drawspritesrf()

            pygame.display.update()

pygame.quit() 

        