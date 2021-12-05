import pygame
import os

pygame.font.init()
star = pygame.transform.scale(pygame.image.load(os.path.join("Project\game_assets\game\Star.png")), (50, 50)) 
star1 = pygame.transform.scale(pygame.image.load(os.path.join("Project\game_assets\game\Star.png")),(20, 20))

class Button:    
    def __init__(self, menu, img, name):
        self.name = name
        self.img = img
        self.x = menu.x - 50
        self.y = menu.y - 110
        self.menu = menu
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.star = pygame.transform.scale(self.screen, (50, 50))
        self.star1 = pygame.transform.scale(self.screen, (20, 20))

    def click(self, X, Y) :

        if X <= self.x + self.width and X >= self.X:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False
    def draw(self, screen):

        screen.blit(self.img, (self.x, self.y))
    def update(self):

        self.x = self.menu.x - 50
        self.x = self.menu.y - 110                    

class VerticalButton(Button) :

    def __init__(self, x, y, img, name, cost):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.cost = cost

class Menu :

    def __init__(self,tower,x,y, img, item_cost) :
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height =img.get_height()
        self.item_cost = item_cost
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font =pygame.font.SysFont("comicsans", 25)
        self.tower = tower
        
    
    def add_btn(self, img, name) :

        self.item += 1
        btn_x = self.x - self.bg.get_height()/2 + 10
        btn_y = self.y - 120 + 10
        self.buttons.append(Button(btn_x, btn_y, img, name))
   
    def get_item_cost(self) :
        return self.item_cost[self.tower.level - 1]    
   
    def draw(self, screen):
        screen.blit(self.bg, (self.x - self.bg.get_width()/2, self.y-120))
        for item in self.buttons:
            item.draw(screen)
            screen.blit(star, (item.x + item, self.width()/2, item.y-9))
            text = self.font.render(str(self.item_cost[self.tower.lever - 1]), 1, (255,255,255))
            screen.blit(text, (item.x +item.width + 30 - text.get_width()/2, item.y + star.get_height() + 5))
    
    def get_clicked(self, X, Y) :

        for btn in self.buttons:
            if btn.click(X,Y) :
                return btn.name
        return None  
    def update(self):
        for btn in self.buttons:
            btn.update()          

class HorizontalMenu(Menu) :

    def __init__(self, x, y, img):
        
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.buttons = []
        self.item = 0
        self.bg = img
        self.font = pygame.font.SysFont("comicsans", 25)
    
    def add_btn(self, img, name, cost):
        self.item += 1
        btn_x = self.x +110 - (self.item - 1)* 100
        btn_y = 340
        self.buttons.append(VerticalButton(btn_x, btn_y, img, name, cost))   
    
    def get_item_cost(self, name):
        for btn in self.buttons:
            if btn.name == name:
                return btn.cost 
        return -1        

     
    def draw(self, screen):
        screen.blit(self.bg, (self.x - 200, self.y+80))
        for item in self.buttons:
            item.draw(screen)
            screen.blit(star1, (item.x + item.width, + item.y + 9))
            text = self.font.render(str(item.cost), 1, (255,255,255))
            screen.blit(text, (item.x + item.width + 30 - text.get_width()/2, item.y + star.get_height() - 8))    


        


class PlayPauseButton(Button) :
     def __init__(self, play_img, pause_img, x, y):
         
         self.img = pause_img
         self.play = play_img
         self.pause = pause_img
         self.paused = True
         self.x = x
         self.y = y
         self.width = self.img.get_width()
         self.height = self.img.get_height()
     
     def draw(self, screen):
         if self.paused:
             screen.blit(self.play, (self.x, self.y))
         else:
             screen.blit(self.pause, (self.x, self.y))   




