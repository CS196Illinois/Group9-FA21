import pygame
import os
from tower import Tower
from pygame import key
from menu import HorizontalMenu
from grid import Array
from grid import Enemy
import time
import random
import config
import bullet
pygame.font.init()

lives_image = pygame.image.load(os.path.join("Project\game_assets\game\lives.png"))
money_image = pygame.image.load(os.path.join("Project\game_assets\game\Star.png"))
side_image = pygame.image.load(os.path.join("Project\game_assets\game\side.png"))
icon_image = pygame.image.load(os.path.join("Project\game_assets\game\icon.png"))
enemy_sprite = pygame.image.load(os.path.join("Project\game_assets\game\enemy.png"))
class Game(): 
    def __init__(self):
        self.width = 600
        self.height = 400
        self.screen = pygame.display.set_mode((self.width , self.height))
        self.enemy = []
        self.tower = []
        self.lives = 10
        self.money = 100
        self.map = pygame.image.load(os.path.join("Project\game_assets\game\Map.png"))
        self.array = Array()
        self.enemy = Enemy()
        self.clicks = []
        self.lifefont = pygame.font.SysFont("comicsans", 30)
        self.menu = HorizontalMenu(self.width - side_image.get_width() + 70, 250, side_image)
        self.menu.add_btn(icon_image, "buy_archer1", 500)
        self.menu.add_btn(icon_image, "buy_archer2", 750)
        self.menu.add_btn(icon_image, "buy_archer3", 1000)
        self.menu.add_btn(icon_image, "buy_archer4", 1000)
        self.clock = pygame.time.Clock()
        self.selected_tower = None
        self.pause = True
        
    def run(self):
        running = True
        clock = pygame.time.Clock()
        keys = set()
        mouse_pos = (0, 0)
        while running:
            clock.tick(500)
            newkeys = set()
            newclicks = set()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # side menu
                    side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                    
                    if side_menu_button:
                        pass
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                # did the user just press the escape key?
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

                # track which keys are currently set
                if event.type == pygame.KEYDOWN:
                    keys.add(event.key)
                    newkeys.add(event.key)
                if event.type == pygame.KEYUP:
                    keys.discard(event.key)

                # track which mouse buttons were pressed
                if event.type == pygame.MOUSEBUTTONUP:
                    newclicks.add(event.button)

                # track the mouse's position
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos
    

            self.draw()

        pygame.quit()

    def draw(self):
        self.screen.blit(self.map, (0,0))
        self.array.draw(self.screen, 25)

        # draw enemy
        self.screen.blit(enemy_sprite,(self.enemy.x, self.enemy.y))
        self.enemy.x = self.enemy.x + self.enemy.xspeed
        self.enemy.y = self.enemy.y + self.enemy.yspeed
       

        # draw lives
        text = self.lifefont.render(str(self.lives), 1, (255,255,255))
        life = pygame.transform.scale(lives_image, (40, 30))
        place = self.width  - life.get_height()
        self.screen.blit(text, ((place - 25), 15))
        self.screen.blit(life, (place, 10))

        #draw money
        moneytext = self.lifefont.render(str(self.money), 1, (255,255,255))
        money = pygame.transform.scale(money_image, (30, 30))
        self.screen.blit(moneytext, ((place - 40), 60))
        self.screen.blit(money, (place + 5, 55))
        
        # draw menu
        self.menu.draw(self.screen)
        self.clock.tick(60)
        pygame.display.update()

        
        if self.selected_tower:
            self.selected_tower.draw(self.screen)
        
        
        for t in self.attack_towers:
            t.draw(self.screen)

       
        self.playPauseButton.draw(self.screen)

        
        self.screen.blit(self.image, self.position)
g = Game()
g.run

