import pygame
pygame.font.init()

lives_image = pygame.image.load(r"C:\Users\szsdw\OneDrive\桌面\学习成果\tower defense game\images\game\lives.png")
money_image = pygame.image.load(r"C:\Users\szsdw\OneDrive\桌面\学习成果\tower defense game\images\game\Star.png")
side_image = pygame.image.load(r"C:\Users\szsdw\OneDrive\桌面\学习成果\tower defense game\images\game\side.png")
icon_image = pygame.image.load(r"C:\Users\szsdw\OneDrive\桌面\学习成果\tower defense game\images\game\icon.png")
class Game():
    def __init__(self):
        self.length = 600
        self.width = 400
        self.screen = pygame.display.set_mode((self.length, self.width))
        self.enemy = []
        self.tower = []
        self.lives = 10
        self.money = 100
        self.map = pygame.image.load(r"C:\Users\szsdw\OneDrive\桌面\学习成果\tower defense game\images\game\Map.png")
        #self.map = pygame.transform.scale(self.screen, (self.length, self.width))
        self.clicks = []
        self.lifefont = pygame.font.SysFont("comicsans", 30)
        
    
    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                position = pygame.mouse.get_pos()

                #if event.type == pygame.MOUSEBUTTONDOWN:
                    #self.clicks.append(position)
                    #print(self.position)


            self.draw()

        pygame.quit()

    def draw(self):
        self.screen.blit(self.map, (0,0)) 
        # draw tower

        # draw enemy

        # draw lives
        text = self.lifefont.render(str(self.lives), 1, (255,255,255))
        life = pygame.transform.scale(lives_image, (40, 30))
        place = self.length - life.get_width()
        self.screen.blit(text, ((place - 25), 15))
        self.screen.blit(life, (place, 10))

        #draw money
        moneytext = self.lifefont.render(str(self.money), 1, (255,255,255))
        money = pygame.transform.scale(money_image, (30, 30))
        self.screen.blit(moneytext, ((place - 40), 60))
        self.screen.blit(money, (place + 5, 55))
        pygame.display.update()

       

g = Game()
g.run()