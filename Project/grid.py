import pygame
from pygame.locals import *
import os


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
tower1 = pygame.image.load(os.path.join("game_assets", "game", "tank.png"))
tower2 = pygame.image.load(os.path.join("game_assets", "game", "tank2.png"))
tower3 = pygame.image.load(os.path.join("game_assets", "game", "tank3.png"))
class Array:
    def __init__(self):
       self.rows = 16
       self.cols = 24
       self.tower = Tower()
       self.towerPosition = [[]]
       
       path = None
       ground = None
       #change 0 and 1 to change layout of grid. 1 mean a sprite is being drawn, 0 is just empty though i may make a road block to put it there soon
       #sprite resolution can be scaled until finalalized. adjust map row and column accordingly to match new resolution
       self.maze =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
       
                    

    def draw(self, window):
         x = 0
         y = 0
         width = 25

         for row in self.maze:
             for col in row:
                 if col == 1:
                     pygame.draw.rect(window, GREEN,(x, y, width, width), 2)
                 if col == 0:
                     pygame.draw.rect(window, RED,(x, y, width, width), 2)
                 if col == 2:
                     self.tower.draw(window, x, y)

                 x = x + width
             y = y + width
             x = 0

    def setValue(self, value):
        x, y = pygame.mouse.get_pos()
                    
        arrayPosX = x//25
        arrayPosY = y//25
        print(arrayPosX, arrayPosY)
        print(self.maze) 
    

        self.maze[arrayPosY][arrayPosX] = value
        self.towerPosition.append([arrayPosX * 25, arrayPosY * 25])

    def getPosition(self):
        return self.towerPosition;

        
#________________________________________________________________________________________________________________________________________________________________________________________________________________
import os
class Enemy:
    x = None
    y = None
    xspeed = 0
    yspeed = 0
    health = None
    money = None
    speedIncrease = None
             


    def __init__(self, positionX, positionY):
        self.x = positionX
        self.y = positionY

    def setValue(self, h, m, s):
        self.health = h
        self.money = m
        self.speedIncrease = s


    def draw(self, image, surface):
        surface.blit(image, (self.x, self.y))
      
        

    def path(self):
        #self.x = self.x + (self.xspeed * self.speedIncrease)
        #self.y = self.y + (self.yspeed * self.speedIncrease)
        if self.x >= 25 and self.y >= 200:
            self.xspeed = 1
            self.yspeed = 0
            
            
        if self.x >= 100 and self.y >= 200:
            self.xspeed = 0
            self.yspeed = -1

        if self.x >= 100  and self.y <=100:
            self.xspeed = 1
            self.yspeed = 0

        if self.x >= 200 and self.y >= 100:
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

    def takeDamage(self, value):
        self.enemy -= value;
#________________________________________________________________________________________________________________________________________________________________________________________________________________

class Tower:
    def __init__(self):
        self.width = 50
        self.cost = [0, 0, 0]
        self.price = [0, 0, 0]
        self.selected = False
        self.menu = False
        self.level = 0
        self.tower_image = [tower1, tower2, tower3]

    def draw(self, screen, x, y):
        image =  self.tower_image[self.level]
        screen.blit(image, (x, y))
    
    def click(self, X, Y):
        if X <= self.x + self.length and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False
        

    def sell(self):
        pass

    def upgrade(self):
        pass

    def move(self):
        pass



