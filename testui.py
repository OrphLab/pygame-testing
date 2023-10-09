import pygame

class MainSurface:
    def __init__(self, screen) -> None:
        self.mainsrf = pygame.Surface((1200,600))
        self.spritesrf = pygame.Surface((285, 600))
        self.size = (500,500)
        self.pos = (0,0)
        self.col = (0,255,0)
        self.screen = screen
        
        

    def drawmainsrf(self):
        self.screen.blit(self.mainsrf, (5,5))
        self.mainsrf.fill((255,0,0))
        self.drawrect()
    
    def drawspritesrf(self):
        self.screen.blit(self.spritesrf, (1210,5))
        self.spritesrf.fill((0,255,0))
    
    def drawrect(self):
        pygame.draw.rect(self.mainsrf, (10,122,255), pygame.Rect((1150,35), (100,100)))
        
