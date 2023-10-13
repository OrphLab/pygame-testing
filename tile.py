import pygame
from pygame.sprite import Sprite
from player import Player

tile_selection = {
    'lgrass': (1,1),
    'mgrass': (3,1),
    'rgrass': (5,1,), 
    'ltbox' : (3,20),
    'rtbox': (4,20),
    'lbbox' : (3,21),
    'rbbox' : (4,21)  
}
class Tilesheet:
        def __init__(self, filename, twidth, theight, nrow, ncol, screen) -> None:
            
            self.tilesheet = pygame.image.load(filename).convert()
            self.size = (twidth, theight)
            self.rows = nrow
            self.cols = ncol
            self.width = twidth
            self.height = theight
            self.screen = screen

            self.tiletable = []
            for tile_x in range(0, self.cols):
                line =[]
                self.tiletable.append(line)
                for tile_y in range (0, self.rows):
                    rect = (tile_x * self.size[0], 
                            tile_y * self.size[1], 
                            self.width, self.height)
                    line.append(self.tilesheet.subsurface(rect))
        
        def draw_tilesheet(self):
            for x, row in enumerate(self.tiletable):
                for y, tile in enumerate(row):
                    self.screen.blit(tile, (x*30, y*30))
        
class Tile(pygame.sprite.Sprite):
    def __init__(self, type, pos, screen, tilesheet):
        super().__init__()
        self.tilesheet = tilesheet
        self.string_type = type         
        self.type = self.get_image(self.string_type)
        self.image = pygame.transform.scale(self.type, (50,50))
        self.rect = self.image.get_rect(topleft=pos)
        self.screen = screen

    def __str__(self) -> str:
        return "sprite{%s-(%s,%s)}"%(self.string_type, self.rect.x, self.rect.y)
    
    def get_image(self, type):
        if type in tile_selection:
            type_value= tile_selection[type]
            img = self.tilesheet.tiletable[type_value[0]][type_value[1]]
            return img
        else:
            None
    
    def draw_tile(self, tile, tile_x, tile_y, surface):
        print("im here")
        surface.blit(tile, (tile_x, tile_y))

        


 
        
