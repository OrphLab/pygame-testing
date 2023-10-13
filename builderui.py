import pygame

class BuilderUI:
    def __init__(self, screen:tuple) -> None:
        self.mainsrf = pygame.Surface((1200,600))
        self.mainsrf_rect = self.mainsrf.get_rect()
        self.spritesrf = pygame.Surface((285, 600))
        self.tile_size = (50,50)
        self.pos = (0,0)
        self.col = (0,255,0)
        self.screen = screen
        self.grid_rects =[]
        
    def drawmainsrf(self):
        self.screen.blit(self.mainsrf, (5,5))
        self.mainsrf.fill((0,0,0))
    
    def drawspritesrf(self):
        self.screen.blit(self.spritesrf, (1210,5))
        self.spritesrf.fill((0,255,0))
    
    def draw_rect_grid(self, offset):
        grid_width = 1900
        grid_height = 1900

        for x in range(0, grid_width, 50):
            for y in range(0,grid_height, 50):
                rect = pygame.Rect(x-offset[0],y-offset[1], 50,50)
                pygame.draw.rect(self.mainsrf, (0,10,0), rect, 2)
                self.grid_rects.append(rect)
    
    def draw_grid(self, offset) -> None:
        for x in range(0,1995,50):
            pygame.draw.line(self.mainsrf, (0,255,0), (1-offset[0],x), (1900,x), 2)
            pygame.draw.line(self.mainsrf, (0,255,0), (x,1-offset[1]), (x, 1900), 2)
    
    def tile_highlight(self, mouse, offset):
        mouse_x, mouse_y = mouse
        tile_x = mouse_x - offset[0] //self.tile_size[0]
        tile_y = mouse_y -offset[1] //self.tile_size[1]
        tile_rect = pygame.Rect(tile_x*self.tile_size[0], tile_y*self.tile_size[1], self.tile_size[0], self.tile_size[1])
        pygame.draw.rect(self.mainsrf,(255,255,0), tile_rect, 2)
    
    def update(self):
        self.drawmainsrf()
        self.drawspritesrf()