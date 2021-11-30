import os
class Tower:
    def __init__(self):
        self.width = 50
        self.cost = [0, 0, 0]
        self.price = [0, 0, 0]
        self.selected = False
        self.menu = False
        self.tower_image = [self.tower1, self.tower2, self.tower3]
        self.level = 1
        self.tower1 = pygame.image.load(os.path.join("game_assets\game\tank1.png"))
        self.tower2 = pygame.image.load(os.path.join("game_assets\game\tank2.png"))
        self.tower3 = pygame.image.load(os.path.join("game_assets\game\tank3.png"))

    def draw(self, screen, x, y):
        image =  self.tower_image[self.level]
        screen.blit(image, (x, y))
    
    def click(self, X, Y):
        if X <= self.x + self.length and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False
        

    def sell(self):
        pass

    def upgrade(self):
        pass

    def move(self):
        pass
