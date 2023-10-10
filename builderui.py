import pygame

class BuilderUI:
    def __init__(self, screen:tuple) -> None:
        self.mainsrf = pygame.Surface((1200,600))
        self.spritesrf = pygame.Surface((285, 600))
        self.tile_size = (50,50)
        self.pos = (0,0)
        self.col = (0,255,0)
        self.screen = screen
        
    def drawmainsrf(self):
        self.screen.blit(self.mainsrf, (5,5))
        self.mainsrf.fill((0,0,0))
        self.drawrect()
    
    def drawspritesrf(self):
        self.screen.blit(self.spritesrf, (1210,5))
        self.spritesrf.fill((0,255,0))
    
    def drawrect(self):
        pygame.draw.rect(self.mainsrf, (10,122,255), pygame.Rect((50,50), (50,50)))
        
    def draw_grid(self) -> None:
        for x in range(0,1995,50):
            pygame.draw.line(self.mainsrf, (0,255,0), (1,x), (1900,x), 2)
            pygame.draw.line(self.mainsrf, (0,255,0), (x,1), (x, 1900), 2)
    
    def tile_highlight(self, mouse):
        mouse_x, mouse_y = mouse
        
        tile_x = mouse_x //self.tile_size[0]
        tile_y = mouse_y //self.tile_size[1]

        tile_rect = pygame.Rect(tile_x*self.tile_size[0], tile_y*self.tile_size[1], self.tile_size[0], self.tile_size[1])
        pygame.draw.rect(self.mainsrf,(255,255,0), tile_rect, 2)
        
    
    def ui_update(self):
        self.drawmainsrf()
        self.drawspritesrf()
        self.draw_grid()