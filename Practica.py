# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window.
SCREEN = pygame.display.set_mode((500, 500))

# Run until the user asks to quit.
run = True
while run:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Fill the background with color black.
    SCREEN.fill((0, 0, 0))

# End of the program.
pygame.quit()