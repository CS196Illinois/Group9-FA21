class tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 0
        self.height = 0
        self.cost = [0, 0, 0]
        self.price = [0, 0, 0]
        self.selected = False
        self.menu = False
        self.tower_image = []
        self.level = 1

    def draw(self, screen):
        image =  self.tower_image[self.level]
        screen.blit(image, (self.x - image.getlength()/ 2, self.y - image.get_height()/ 2))
    
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
