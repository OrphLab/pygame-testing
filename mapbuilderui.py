import pygame
import tile
from tile import Tile
class MapBuilderUI:
    def __init__(self, screen:tuple, tilesheet) -> None:
        self.mainsrf = pygame.Surface((1200,600))
        self.tile_selection_srf = pygame.Surface((285, 600))
        self.tile_size = (50,50)
        self.pos = (0,0)
        self.col = (0,255,0)
        self.screen = screen
        self.grid_rects =[]
        self.left_arrow = pygame.rect.Rect(500,610,50,50)
        self.right_arrow = pygame.rect.Rect(550,610,50,50)
        self.up_arrow = pygame.rect.Rect(600,610,50,50)
        self.down_arrow = pygame.rect.Rect(650,610,50,50)
        self.tilesheet = tilesheet
        
    def drawmainsrf(self):
        self.screen.blit(self.mainsrf, (5,5))
        self.mainsrf.fill((0,0,0))
    
    def drawspritesrf(self):
        self.screen.blit(self.tile_selection_srf, (1210,5))
        self.tile_selection_srf.fill((0,255,0))
    
    def draw_rect_grid(self, offset):
        grid_width = 1900
        grid_height = 1900
    
        for x in range(0, grid_width, 50):
            for y in range(0,grid_height, 50):
                rect = pygame.Rect(x-offset[0],y-offset[1], 50,50)
                pygame.draw.rect(self.mainsrf, (0,10,0), rect, 2)
                self.grid_rects.append(rect)

    def map_arrows(self):

        pygame.draw.rect(self.screen, (255,0,0), self.left_arrow)
        pygame.draw.rect(self.screen, (0,255,0), self.right_arrow)
        pygame.draw.rect(self.screen, (0,255,255), self.up_arrow)
        pygame.draw.rect(self.screen, (0,0,255), self.down_arrow)

    def move_map(self, offset,event):
        if self.left_arrow.collidepoint(event.pos):
            offset[0] -= 50
            print("left")
        elif self.right_arrow.collidepoint(event.pos):
            offset[0] += 50
            print("right")
        elif self.up_arrow.collidepoint(event.pos):
            offset[1] -= 50
        elif self.down_arrow.collidepoint(event.pos):
            offset[1] += 50
        return offset


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
    
    def draw_tile_selection(self, tile_size, surface, tile_list):
        tile_width, tile_height = tile_size[0], tile_size[1]
        spacing = 10
        surface_width, surface_height = surface.get_size()
        tile_list = tile_list
        starting_x, starting_y = 15,15

        for tile_type in tile_list:
            tile = Tile(tile_type,(starting_x, starting_y), surface, self.tilesheet, use = "map_buidling")
            surface.blit(tile.image, tile.rect)
            starting_x += tile_width+spacing

            if starting_x + tile_width > surface_width:
                starting_x = 15
                starting_y += tile_height + spacing
    
    def update(self):
        self.drawmainsrf()
        self.drawspritesrf()
        self.map_arrows()
        self.draw_tile_selection(self.tile_size, self.tile_selection_srf, tile.tile_selection)