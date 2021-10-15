# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycha

import pygame
from pygame.locals import *



def game():

    # initialize pygame
    pygame.init()

    # create screen
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tower defense")

    # fill the background with color
    color = (255, 255, 255)
    screen.fill(color)

    # input a block
    start = pygame.image.load(r"C:\Users\szsdw\PycharmProjects\pygame\imageresources\start.jpg").convert()
    screen.blit(start, (600, 100))
    screen.blit(start, (600, 180))
    screen.blit(start, (600, 260))

    img = pygame.image.load(r"C:\Users\szsdw\PycharmProjects\pygame\imageresources\cursor.jpg").convert()
    # loop
    running = False
    right_clicking = True
    left_clicking = True

    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True
        b1, b2, b3 = pygame.mouse.get_pressed()
        if b1:
            button = "Left button"
        elif b2:
            button = "Middle button"
        elif b3:
            button = "Right button"
        pygame.mouse.set_visible(False)
        mx, my = pygame.mouse.get_pos()

        screen.blit(img, (mx, my))

        pygame.display.update()


if __name__ == "__main__":
    game()
