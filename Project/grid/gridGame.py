from pygame.locals import *
import pygame
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
 
class Maze:
    def __init__(self):
       self.M = 24
       self.N = 16
       #change 0 and 1 to change layout of grid. 1 mean a sprite is being drawn, 0 is just empty though i may make a road block to put it there soon
       #sprite resolution can be scaled until finalalized. adjust map row and column accordingly to match new resolution
       self.maze = [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,
                     1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,
                     1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,
                     1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]

    def draw(self,display_surf,image_surf, grass_surf):
       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
           if self.maze[ bx + (by*self.M) ] == 1:
               display_surf.blit(image_surf,( bx * 25 , by * 25))

           if self.maze[ bx + (by*self.M) ] == 0:
               display_surf.blit(grass_surf,( bx * 25 , by * 25))
      
           bx = bx + 1
           if bx > self.M-1:
               bx = 0 
               by = by + 1

class Enemy:
    x = 25
    y = 100
    xspeed = 0
    yspeed = 0


    def draw(self, image, surface):
        surface.blit(image, (self.x, self.y))
      
        
    def getPosition(pos, rows, width):
        gap = width // rows
        y, x = pos

        row = y // gap
        col = x // gap

        return row, col
        
        
        
class App:
 
    windowWidth = 600
    windowHeight = 400
    
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self._grass_surf = None
        self._enemy_block = None
        
        self.maze = Maze()
        self.enemy = Enemy()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        
        pygame.display.set_caption('Example')
        self._running = True
        self._block_surf = pygame.image.load("block.png").convert()
        self._block_surf = pygame.transform.smoothscale(self._block_surf, (25, 25))

        self._enemy_block = pygame.image.load("enemy.png").convert()

        self._grass_surf = pygame.image.load("grass.png").convert()
        self._grass_surf = pygame.transform.smoothscale(self._grass_surf, (25, 25))
        
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
    
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.maze.draw(self._display_surf, self._block_surf, self._grass_surf)
        

        self._display_surf.blit(self._enemy_block,(self.enemy.x,self.enemy.y))
        print(self.enemy.x)

        self.enemy.x = self.enemy.x + self.enemy.xspeed
        self.enemy.y = self.enemy.y + self.enemy.yspeed

        if self.enemy.x >= 25 and self.enemy.y >= 100:
            self.enemy.xspeed = 1
            self.enemy.yspeed = 0
            
            
        if self.enemy.x >= 125 and self.enemy.y >= 100:
            self.enemy.xspeed = 0
            self.enemy.yspeed = 1

        if self.enemy.x >= 125  and self.enemy.y >=200:
            self.enemy.xspeed = 1
            self.enemy.yspeed = 0

        if self.enemy.x >= 300 and self.enemy.y <= 200:
            self.enemy.xspeed = 0
            self.enemy.yspeed = -1

       

        

       
        

        pygame.display.flip()
    
        
       
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
