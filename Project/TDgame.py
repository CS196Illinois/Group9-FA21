import pygame
import os

#Constants
TILES_HORIZONTAL = 100
TILES_VERTICAL = 70
TILE_SIZE = 10
SCREEN_WIDTH = TILES_HORIZONTAL * TILE_SIZE
SCREEN_HEIGHT = TILES_VERTICAL * TILE_SIZE
TITLE = "Tower Defense Game"

# Basic game class, later I create an instance of the class to start a game.
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load('Map.png')
        self.bg = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    def main(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        pass

    def draw(self):
        self.surface.blit(self.bg, (0,0))
        pygame.display.update()

# Grid design ideas

        


# Creates a game instance, need this to run.
if __name__ == "__main__":
    mygame = Game()
    mygame.main()

    