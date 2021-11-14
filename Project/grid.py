from pygame.locals import *
import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE= (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Array:
    def __init__(self):
       self.M = 24
       self.N = 16
       path = None
       ground = None
       #change 0 and 1 to change layout of grid. 1 mean a sprite is being drawn, 0 is just empty though i may make a road block to put it there soon
       #sprite resolution can be scaled until finalalized. adjust map row and column accordingly to match new resolution
       self.maze = [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,1,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,1,1,0,0,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,
                     1,1,1,0,0,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,
                     0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]

    def draw(self, window, width):
         x = 0
         y = 0

         for i in range(0, self.M * self.N):
             if self.maze[ x + (y*self.M) ] == 1:
                 
                path = pygame.draw.rect(window,TURQUOISE,(x*width, y*width, width, width),2)
                
                

             if self.maze[ x + (y*self.M) ] == 0:
                ground = pygame.draw.rect(window, RED, (x*width, y*width, width, width,),2)

             x = x + 1
             if x > self.M-1:
                   x = 0
                   y = y+1

class Enemy:
    x = 25
    y = 200
    xspeed = 0
    yspeed = 0


    def draw(self, image, surface):
        surface.blit(image, (self.x, self.y))
      
        
    def getPosition(pos, rows, width):
        gap = width // rows
        y, x = pos

        row = y // gap
        col = x // gap

        return row, col

    def path(self):
        if self.x >= 25 and self.y >= 200:
            self.xspeed = 1
            self.yspeed = 0
            
            
        if self.x >= 100 and self.y >= 200:
            self.xspeed = 0
            self.yspeed = -1

        if self.x >= 100  and self.y <=100:
            self.xspeed = 1
            self.yspeed = 0

        if self.x >= 200 and self.y >=100:
            self.xspeed = 0
            self.yspeed = 1

        if self.x >= 200 and self.y >= 250:
            self.xspeed = 1
            self.yspeed = 0

        if self.x >= 375 and self.y <= 250:
            self.xspeed = 0
            self.yspeed = -1

        if self.x >= 375 and self.y <= 175:
            self.xspeed = 1;
            self.yspeed = 0;
        
        

