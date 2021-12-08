import os 
import math
import time
import pygame
bullet_img = pygame.transform.scale(pygame.image.load(os.path.join("Project\game_assets\game\Star.png")),(8, 8))
class Bullet():
    def __init__(self, position, width=8, height=8, image = bullet_img, dmg=10, speed=300):
        self.dmg = dmg
        self.speed = speed
        self.enemy = None

        # frame rate independent data
        self.last_frame = time.time()
        self.dt = 0

    def get_damage(self):
        return self.dmg

    def set_enemy(self, enemy):
        # where enemy is an object
        # that may or may not move,
        # but has a method to
        # retrieve its position and
        # to handle a collision with
        # the bullet
        self.enemy = enemy

    # moves toward the enemy object if it exists
    def move(self):
        if self.enemy is None:
            return

        # move based on center points
        dest = self.enemy.get_center()
        curr = self.get_center()
        
        # calculate the direction to move
        direction = (dest[0]-curr[0], dest[1]-curr[1])
        x = direction[0]**2
        y = direction[1]**2

        # normalize the direction vector
        mag = math.sqrt(float(x) + float(y))
        normalized = (direction[0]/mag, direction[1]/mag)

        # calculate how far to move in the direction
        # choosing to move as far/fast as allowed
        # or to move straight to the enemy if
        # it is closer
        dist = min(self.speed*self.dt, math.sqrt(x+y))
        self.position = (self.position[0] + dist*normalized[0], self.position[1] + dist*normalized[1])

    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        # frame rate independent calculations
        t = time.time()
        self.dt = t - self.last_frame
        self.last_frame = t

        # move
        self.move()

        actions = []

        
        
