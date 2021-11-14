from grid import Enemy
from .tower import Tower
import pygame
import os

class Archertower(Tower):
    def __init__(self, x, y):
        super().__init__(self. x, y)
        self.tower_imgs = []
        self.archer_imgs = []
        self.archer_count = 0
        self.range = 30
        self.withinrange =  False

    # need to load image to the position on grid system
    # need to load archer image 

    def draw(self, screen):
        super.draw(screen)

    def changerange(self, r):
        self.range = r

    def attack(self, enemy) :
        x = enemy.x
        y = enemy.y
        
    

class Arrow:
    def __init__(self, x, y):
        pass
        
    
   
        
        



