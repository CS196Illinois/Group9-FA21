import pygame
pygame.font.init()
import os
from menu import HorizontalMenu
from grid import Array
from grid import Enemy

lives_image = pygame.image.load(os.path.join("game_assets", "game", "lives.png"))
money_image = pygame.image.load(os.path.join("game_assets", "game", "Star.png"))
side_image = pygame.image.load(os.path.join("game_assets", "game", "side.png"))
icon_image = pygame.image.load(os.path.join("game_assets", "game", "icon.png"))
enemy_sprite = pygame.image.load(os.path.join("game_assets", "game", "enemy.png"))


class Game():
    def __init__(self):
        self.width = 600
        self.height = 400
        self.screen = pygame.display.set_mode((self.width , self.height))
        self.count = 0;

        self.enemy = []
    
        
        self.tower = []
        self.lives = 10
        self.money = 100
        self.map = pygame.image.load(os.path.join("game_assets", "game", "Map.png"))
        self.array = Array()
        self.clicks = []
        self.lifefont = pygame.font.SysFont("comicsans", 30)
        self.menu = HorizontalMenu(self.width - side_image.get_width() + 70, 250, side_image)
        self.menu.add_btn(icon_image, "buy_archer1", 500)
        self.menu.add_btn(icon_image, "buy_archer2", 750)
        self.menu.add_btn(icon_image, "buy_archer3", 1000)
        self.menu.add_btn(icon_image, "buy_archer4", 1000)
        self.clock = pygame.time.Clock()

        self.waveCounter = 0
        self.waveState = 0
        self.interval = 0
        

    
    def run(self):
        running = True
        

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # side menu
                    self.array.setValue(2)

                    print(self.array)

            #if self.lives == 0:
               # running = False

            self.draw()
        

        pygame.quit()
        

    def draw(self):

        self.screen.blit(self.map, (0,0))
        self.array.draw(self.screen)

        # draw tower
        
    
        

        # draw enemy
#track number of enemy
        if self.count < 100:
            self.count = self.count + 1

        if self.count >= 100:
            self.count = 0
# wave spawn
        if (self.count == 99 and self.waveCounter != 10 and self.waveState == 0):     
            self.enemy.append(Enemy(25, 200))
            self.waveCounter += 1

        if (self.count == 99 and self.waveCounter != 15 and self.waveState == 1):
            self.enemy.append(Enemy(25, 200))
            self.waveCounter += 1

        if (self.count == 99 and self.waveCounter != 20 and self.waveState == 2):
            self.enemy.append(Enemy(25, 200))
            self.waveCounter += 1
            
        if self.waveCounter >= 10 and self.waveState == 0 and len(self.enemy) == 0:
            self.waveCounter = 0
            self.waveState = 1

        if self.waveCounter >= 15 and self.waveState == 1 and len(self.enemy) == 0:
            self.waveCounter = 0
            self.waveState = 2

        if self.waveCounter >= 20 and self.waveState == 2 and len(self.enemy) == 0:
            self.waveCounter = 0
            self.waveState = 0

        print(self.waveCounter, self.waveState)
         
#draw each enemy in list
        for enemy in self.enemy:
            if self.waveState == 0:
                enemy.setValue(100, 10, 1)
            if self.waveState == 1:
                enemy.setValue(150, 15, 1.25)
            if self.waveState == 2:
                enemy.setValue(200, 20, 2.5)

            enemy.x = enemy.x + (enemy.xspeed * enemy.speedIncrease)
            enemy.y = enemy.y + (enemy.yspeed * enemy.speedIncrease)
            enemy.draw(enemy_sprite, self.screen)


    
            
#base health mechanism
            if enemy.x >= self.width:
                self.enemy.remove(enemy)
                self.lives -= 1
#enemy death mechanism
            if enemy.health <= 0:
                self.enemy.remove(enemy)
                self.money += enemy.money
#path              
            enemy.path()


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
 


g = Game()
g.run()
