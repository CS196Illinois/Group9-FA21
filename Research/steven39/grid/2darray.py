import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Array")
WHITE = (255, 255, 255)
block = pygame.image.load("block.png").convert()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False;

        WIN.fill((WHITE))
        pygame.display.update()
                    
                        
    pygame.quit()

if __name__ == "__main__":
    main()


class Maze:
    def __init__(self):
       self.R = 10
       self.C = 8
       self.maze = [ 1,1,1,1,1,1,1,1,1,1,
                     1,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,1,
                     1,0,1,1,1,1,1,1,0,1,
                     1,0,1,0,0,0,0,0,0,1,
                     1,0,1,0,1,1,1,1,0,1,
                     1,0,0,0,0,0,0,0,0,1,
                     1,1,1,1,1,1,1,1,1,1,]
    def draw(self,WIN,image_surf):
       bx = 0
       by = 0
       for i in range(0,self.R*self.C):
           if self.maze[ bx + (by*self.R) ] == 1:
               display_surf.blit(image_surf,( bx * 44 , by * 44))
      
           bx = bx + 1
           if bx > self.M-1:
               bx = 0 
               by = by + 1
