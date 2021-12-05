import pygame
from .tower import Tower
import os
import math
from menu import Menu


menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("Project\game_assets\game\side.png")).convert_alpha(), (120, 70))



tower_imgs1 = []
archer_imgs1 = []

for x in range(7,10):
    tower_imgs1.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Project\game_assets\game\archertower", str(x) + ".png")).convert_alpha(),
        (90, 90)))


class ArcherTowerLong(Tower):
    def __init__(self, x,y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs1[:]
        self.archer_imgs = archer_imgs1[:]
        self.archer_count = 0
        self.range = 200
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 1
        self.original_damage = self.damage
        self.width = self.height = 90
        self.moving = False
        self.name = "archer"

        self.menu = Menu(self, self.x, self.y, menu_bg, [2000, 5000,"MAX"])


    def draw(self, screen
    ):
        super().draw_radius(screen
        )
        super().draw(screen
        )

        if self.inRange and not self.moving:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs) * 10:
                self.archer_count = 0
        else:
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count // 10]
        if self.left == True:
            add = -25
        else:
            add = -archer.get_width() + 10
        screen
        .blit(archer, ((self.x + add), (self.y - archer.get_height() - 25)))

    def change_range(self, r):
        self.range = r

    def attack(self, enemies):
        money = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            dis = math.sqrt((self.x - enemy.img.get_width()/2 - x)**2 + (self.y -enemy.img.get_height()/2 - y)**2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos)
        enemy_closest = enemy_closest[::-1]
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if self.archer_count == 50:
                if first_enemy.hit(self.damage) == True:
                    money = first_enemy.money * 2
                    enemies.remove(first_enemy)

            if first_enemy.x > self.x and not(self.left):
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)

        return money


tower_imgs = []
archer_imgs = []
# load archer tower images
for x in range(10,13):
    tower_imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Project\game_assets\game\archertower", str(x) + ".png")),
        (90, 90)))


class ArcherTowerShort(ArcherTowerLong):
    def __init__(self, x,y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs[:]
        self.archer_imgs = archer_imgs[:]
        self.archer_count = 0
        self.range = 120
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 2
        self.original_damage = self.damage

        self.menu = Menu(self, self.x, self.y, menu_bg, [2500, 5500, "MAX"])
        self.name = "archer2"



