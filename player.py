import pygame
from pygame.sprite import Sprite
from pygame.math import Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen, worldmap) -> None:
        super().__init__()
        
        self.pos = pos
        self.image_index:int = 0  #used to pick the right player img from list
        self.frame_counter:int = 0  # used for speed of player animation

        self.direction = 0 #0 = right, 1 = left
        self.r_img: list =[]
        self.l_img: list =[]

        #populates the two player lists, with img, in both directions
        for image in range(1,5):
            player_right = pygame.image.load(f"img/player/player{image}.png")
            player_right = pygame.transform.scale(player_right, Vector2(40,80))
            self.r_img.append(player_right)
            player_left = pygame.transform.flip(player_right, True, False)
            self.l_img.append(player_left)

        self.image = self.r_img[self.image_index]
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.conterx = self.rect.centerx
        self.centery = self.rect.centery
        
        self.velocity_y = 0
        self.jumped = False
        self.jump_counter = 0

        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.worldmap = worldmap

        self.camera =[0,0]
        self.camera_speed = 1
    def update (self):
        

        self.camera[0] = (self.rect.x - self.screen_width //2) * self.camera_speed
        self.camera[1] = (self.rect.y - self.screen_height //2) * self.camera_speed
        print("camera", self.camera[0], self.camera[1])
        movement_x:float = 0
        movement_y:float = 0
        anim_cooldown:int = 5

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            if key[pygame.K_SPACE] and self.jumped == False and self.jump_counter <= 0:
                self.velocity_y -=15
                self.jumped = True
                self.jump_counter += 1  
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_RIGHT]:
            movement_x += 5
            self.frame_counter +=1
            self.direction = 0
        if key[pygame.K_LEFT]:
            movement_x -= 5
            self.frame_counter += 1
            self.direction = 1
        #resets animation when not moving left og right
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
            self.frame_counter = 0
            self.image_index = 0
            self.image = self.r_img[self.frame_counter]
        
        #adds gravity to jump
        self.velocity_y += 1
        if self.velocity_y >15:
            self.velocity_y = 15
        movement_y += self.velocity_y
        
        #picks the right image list, based on direction
        if self.direction == 0:
            self.image = self.r_img[self.image_index]
        if self.direction == 1:
            self.image = self.l_img[self.image_index]
        #handels the player animation
        if self.frame_counter > anim_cooldown:
            self.frame_counter = 0
            self.image_index += 1
            if self.image_index >= len(self.r_img):
                self.image_index = 0
  
        for tile in self.worldmap:
            tilerect = tile.rect
            if tilerect.colliderect(self.rect.x + movement_x, self.rect.y, self.width, self.height):
                movement_x = 0
            if tilerect.colliderect(self.rect.x, self.rect.y + movement_y, self.width, self.height):
                if movement_y < 0:
                    movement_y = tilerect.bottom - self.rect.top
                    self.velocity_y = 0
                if movement_y >= 0 :
                    movement_y = tilerect.top -self.rect.bottom
                    self.velocity_y = 0
                    self.jump_counter = 0

        self.rect.x += movement_x
        self.rect.y += movement_y

        self.screen.blit(self.image, (self.rect.x - int(self.camera[0]), self.rect.y - int(self.camera[1])))
        print("player: ", self.camera[0], self.camera[1])
                         

   

