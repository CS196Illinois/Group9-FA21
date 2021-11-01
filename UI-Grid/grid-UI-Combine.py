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

class Array:
    def __init__(self):
       self.M = 24
       self.N = 16
       path = None
       ground = None
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

    def draw(self, window, width):
         x = 0
         y = 0

         for i in range(0, self.M * self.N):
             if self.maze[ x + (y*self.M) ] == 1:
                 
                path = pygame.draw.rect(window,RED,(x*width, y*width, width, width),2)
                

             if self.maze[ x + (y*self.M) ] == 0:
                ground = pygame.draw.rect(window, GREEN, (x*width, y*width, width, width,),2)

             x = x + 1
             if x > self.M-1:
                   x = 0
                   y = y+1
        

class Main:
    width = 600
    height = 400

    def __init__(self):
        self._running = True
        self.windowSurface = None
        self.bgSurf = None
        
        self.array = Array()
        
        self.clock = pygame.time.Clock()
        
    def on_init(self):
        self.running = True
        self.windowSurface = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
        self.bgSurf = pygame.image.load("map.png").convert()

         
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass

    def on_render(self):
        self.windowSurface.fill((0,0,0))
        self.windowSurface.blit(self.bgSurf, (0, 0))
        self.array.draw(self.windowSurface, 25)

        self.clock.tick(60)
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
    theApp = Main()
    theApp.on_execute()


        

               
                
               

       
