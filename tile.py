import pygame
from pygame.sprite import Sprite
from player import Player

#available tiles
tile_selection = {
    'lgrass': (1,1),
    'mgrass': (3,1),
    'rgrass': (5,1,), 
    'ltbox' : (3,20),
    'rtbox': (4,20),
    'lbbox' : (3,21),
    'rbbox' : (4,21), 
    'rocksindirt' : (17,18),
    'dirtwall1': (7,1),
    'dirtwall2': (1,3),
    'dirtwallcolor': (3,3),
    'dirtwall3' : (5,3),
    'dirtwall4': (1,4),
    'dirtwall5': (3,4),
    'dirtwall6': (5,4),
    'rocksindir1' : (5,6),
    'rocksindirt2' : (7,6),
    'rocksindirt3' : (18,17),
    'toplgrass' : (15,14),
    'topmgrass' : (17,14),
    'toprgrass' : (17,14)
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

            self.tiletable = [] #stores 2D table of tiles
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
        
"""_summary_
type = name of the tile in tile_selection list
"""
class Tile(pygame.sprite.Sprite):
    all_tiles = pygame.sprite.Group() # active game tiles
    def __init__(self, type, pos, screen, tilesheet, use=None):
        super().__init__()
        self.tilesheet = tilesheet
        self.string_type = type         
        self.type = self.get_image(self.string_type)
        self.image = pygame.transform.scale(self.type, (50,50))
        self.rect = self.image.get_rect(topleft=pos)
        self.screen = screen
        if use == None:
            Tile.all_tiles.add(self)

    def __str__(self) -> str:
        return "sprite{%s-(%s,%s)}"%(self.string_type, self.rect.x, self.rect.y)
    
    
        """
        checks it type is in the tile_selection list and returns the corresponding tuple, 
        for the name, and gets the img from the tilesheets tiletable list.
        """
    def get_image(self, type):
            if type in tile_selection:
                type_value= tile_selection[type]
                img = self.tilesheet.tiletable[type_value[0]][type_value[1]]
                return img
            else:
                None

    def draw_tile(self, tile, surface, offset):
        surface.blit(tile.image, (tile.rect.x-offset[0], tile.rect.y-offset[1]))
    

    def get_image_mp(type):
        if type in tile_selection:
            type_value= tile_selection[type]
            img = self.tilesheet.tiletable[type_value[0]][type_value[1]]
            return img
        else:
            None
         
              
    


 
        
