from _typeshed import Self
from menu import PlayPauseButton
import pygame
pygame.font.init()

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

lives_img = pygame.image.load("").convert
money_img = pygame.image.load("").convert()
stop_img = pygame.image.load("").convert_alpha()
begin_img = pygame.image.loag("").convert_alpha()
class Game():
    def __init__(self):

        self.width = 1000
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = []
        self.towers = []
        self.lives = 10
        self.life_font = pygame.font.Sysfont ("cosmicsans", 60)
    
        self.money = 100
        self.pause = False
        self.playPauseButton = PlayPauseButton(begin_img, stop_img, 10, self.height - 85)
    def run(self):
        self.running = False

   
    
    def run(self):
        self.running = False
        while not running:

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = True
                elif event.type == QUIT:
                    running = True
                # track which mouse buttons were pressed
                if event.type == pygame.MOUSEBUTTONUP:
                    newclicks.add(e.button)

                # track the mouse's position
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos    

    def draw(self):
        #draw life
        text = self.life_font.render(str(self.lives), 1, (0, 0, 0))
        life = pygame.transform.scale(lives_img, (25, 25)) 
        start = self.width - life.get_width() - 10,

        self.win.blit(text, (start - text.get_width() - 10, 10))
        self.win.blit(life, (start, 10))
        




        # draw pauseBotton
        self.playPauseButton.draw(self.win)

a = Game()
