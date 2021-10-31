import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location and sets enemy grid path
WIDTH = 25
HEIGHT = 25
enemyPath = [(1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (5, 2), (4, 2), (6, 2), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (2, 9), (2, 10), (2, 11), (1, 11), (1, 12), (1, 13), (1, 14), (2, 14), (3, 14), (4, 14), (5, 14), (5, 15), (5, 16), (5, 17), (4, 17), (3, 17), (2, 17), (2, 18), (2, 19), (2, 20), (3, 20), (4, 20), (5, 20), (6, 20), (7, 20), (8, 20), (9, 19), (8, 19), (9, 18), (9, 17), (9, 16), (9, 15), (9, 14), (8, 14), (8, 13), (8, 12), (8, 11), (7, 11), (6, 11), (5, 11), (5, 10), (5, 9), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8)]
[(1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (5, 2), (4, 2), (6, 2), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (2, 9), (2, 10), (2, 11), (1, 11), (1, 12), (1, 13), (1, 14), (2, 14), (3, 14), (4, 14), (5, 14), (5, 15), (5, 16), (5, 17), (4, 17), (3, 17), (2, 17), (2, 18), (2, 19), (2, 20), (3, 20), (4, 20), (5, 20), (6, 20), (7, 20), (8, 20), (9, 19), (8, 19), (9, 18), (9, 17), (9, 16), (9, 15), (9, 14), (8, 14), (8, 13), (8, 12), (8, 11), (7, 11), (6, 11), (5, 11), (5, 10), (5, 9), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8)]
[(1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (5, 2), (4, 2), (6, 2), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (2, 9), (2, 10), (2, 11), (1, 11), (1, 12), (1, 13), (1, 14), (2, 14), (3, 14), (4, 14), (5, 14), (5, 15), (5, 16), (5, 17), (4, 17), (3, 17), (2, 17), (2, 18), (2, 19), (2, 20), (3, 20), (4, 20), (5, 20), (6, 20), (7, 20), (8, 20), (9, 19), (8, 19), (9, 18), (9, 17), (9, 16), (9, 15), (9, 14), (8, 14), (8, 13), (8, 12), (8, 11), (7, 11), (6, 11), (5, 11), (5, 10), (5, 9), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8)]
[(1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (5, 2), (4, 2), (6, 2), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (2, 9), (2, 10), (2, 11), (1, 11), (1, 12), (1, 13), (1, 14), (2, 14), (3, 14), (4, 14), (5, 14), (5, 15), (5, 16), (5, 17), (4, 17), (3, 17), (2, 17), (2, 18), (2, 19), (2, 20), (3, 20), (4, 20), (5, 20), (6, 20), (7, 20), (8, 20), (9, 19), (8, 19), (9, 18), (9, 17), (9, 16), (9, 15), (9, 14), (8, 14), (8, 13), (8, 12), (8, 11), (7, 11), (6, 11), (5, 11), (5, 10), (5, 9), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8)]
[(1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (5, 2), (4, 2), (6, 2), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (2, 9), (2, 10), (2, 11), (1, 11), (1, 12), (1, 13), (1, 14), (2, 14), (3, 14), (4, 14), (5, 14), (5, 15), (5, 16), (5, 17), (4, 17), (3, 17), (2, 17), (2, 18), (2, 19), (2, 20), (3, 20), (4, 20), (5, 20), (6, 20), (7, 20), (8, 20), (9, 19), (8, 19), (9, 18), (9, 17), (9, 16), (9, 15), (9, 14), (8, 14), (8, 13), (8, 12), (8, 11), (7, 11), (6, 11), (5, 11), (5, 10), (5, 9), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8)]
[(1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (5, 2), (4, 2), (6, 2), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (2, 9), (2, 10), (2, 11), (1, 11), (1, 12), (1, 13), (1, 14), (2, 14), (3, 14), (4, 14), (5, 14), (5, 15), (5, 16), (5, 17), (4, 17), (3, 17), (2, 17), (2, 18), (2, 19), (2, 20), (3, 20), (4, 20), (5, 20), (6, 20), (7, 20), (8, 20), (9, 19), (8, 19), (9, 18), (9, 17), (9, 16), (9, 15), (9, 14), (8, 14), (8, 13), (8, 12), (8, 11), (7, 11), (6, 11), (5, 11), (5, 10), (5, 9), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8)]
[(1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (5, 2), (4, 2), (6, 2), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (2, 9), (2, 10), (2, 11), (1, 11), (1, 12), (1, 13), (1, 14), (2, 14), (3, 14), (4, 14), (5, 14), (5, 15), (5, 16), (5, 17), (4, 17), (3, 17), (2, 17), (2, 18), (2, 19), (2, 20), (3, 20), (4, 20), (5, 20), (6, 20), (7, 20), (8, 20), (9, 19), (8, 19), (9, 18), (9, 17), (9, 16), (9, 15), (9, 14), (8, 14), (8, 13), (8, 12), (8, 11), (7, 11), (6, 11), (5, 11), (5, 10), (5, 9), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8)]
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(12):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(22):
        grid[row].append(0)  # Append a cell


# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [665, 355]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Grid for Tower Defense Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(12):
        for column in range(22):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()