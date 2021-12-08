from config import *
import rectangle
import math
import time
from grid import Enemy
class Bullet(rectangle.Rectangle):
    def __init__(self, position, width=BULLET_DEFAULT_WIDTH, height=BULLET_DEFAULT_HEIGHT, image=BULLET_DEFAULT_IMAGE, dmg=TOWER_DEFAULT_DAMAGE, speed=BULLET_DEFAULT_SPEED):
        rectangle.Rectangle.__init__(self, KIND_BULLET, position, width, height, image)
        self.dmg = dmg
        self.speed = speed
        self.enemy = None

        self.last_frame = time.time()
        self.dt = 0

    def get_damage(self):
        return self.dmg

    def set_enemy(self, Enemy):
       
        self.enemy = Enemy

    #
    def move(self):
        if self.enemy is None:
            return

        dest = self.enemy.get_center()
        curr = self.get_center()
        
        direction = (dest[0]-curr[0], dest[1]-curr[1])
        x = direction[0]**2
        y = direction[1]**2

        mag = math.sqrt(float(x) + float(y))
        normalized = (direction[0]/mag, direction[1]/mag)

        dist = min(self.speed*self.dt, math.sqrt(x+y))
        self.position = (self.position[0] + dist*normalized[0], self.position[1] + dist*normalized[1])

    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        t = time.time()
        self.dt = t - self.last_frame
        self.last_frame = t

        
        self.move()

        actions = []

       
        if self.enemy is None or self.enemy.is_dead():
            actions.append((B_DONE, self))
        elif self.collide(self.enemy) or self.enemy.collide(self):
            self.enemy.hit(self.get_damage())
            if self.enemy.is_dead():
                actions.append((B_KILL, self.enemy.get_value()))
            actions.append((B_DONE, self))
        return actions
