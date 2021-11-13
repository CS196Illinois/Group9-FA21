import pygame
pygame.font.init()
import os
from menu import HorizontalMenu



lives_image = pygame.image.load(os.path.join("game_assets\game\lives.png"))
money_image = pygame.image.load(os.path.join("game_assets\game\Star.png"))
side_image = pygame.image.load(os.path.join("game_assets\game\side.png"))
icon_image = pygame.image.load(os.path.join("game_assets\game\icon.png"))

class Game():
    def __init__(self):
        self.width = 600
        self.height = 400
        self.screen = pygame.display.set_mode((self.width , self.height))
        self.enemy = []
        self.tower = []
        self.lives = 10
        self.money = 100
        self.map = pygame.image.load(os.path.join("game_assets\game\Map.png"))
        self.clicks = []
        self.lifefont = pygame.font.SysFont("comicsans", 30)
        self.menu = HorizontalMenu(self.width - side_image.get_width() + 70, 250, side_image)
        self.menu.add_btn(icon_image, "buy_archer1", 500)
        self.menu.add_btn(icon_image, "buy_archer2", 750)
        self.menu.add_btn(icon_image, "buy_archer3", 1000)
        self.menu.add_btn(icon_image, "buy_archer4", 1000)

    
    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # side menu
                    side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                    
                    if side_menu_button:
                        pass
                    
                    btn_clicked = None
                   


            self.draw()

        pygame.quit()

    def draw(self):
        self.screen.blit(self.map, (0,0)) 

        # draw tower

        # draw enemy

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

        pygame.display.update()
 


g = Game()
g.run()
