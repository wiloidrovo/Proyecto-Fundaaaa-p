# Import libraries.
import pygame
import os # Lead us interact and obtain information from the operative system (OS).
          # Its very easy to use and there exists full information about this.

# Initialize pygame.
pygame.init()

# Define global constants.
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load all the images of the game. 
RUNNIG = 
JUMPING = 
DUCKING = 
OBSTACLES = 
BACKGROUND = pygame.image.load(os.path.join("Images/BG", ".png"))

# Everything in pygame runs in a while loop.
def main():
    run = True   # Flag to our while loop.
    clock = pygame.time.Clock()   # Clock to time our game.
    player = cuco()   # Player is going to be an instance of the class "cuco"

    while run:
        for event in pygame.event.get(): # To exit the game safety/ We will set the flag in false whenever
                                         # we press the "X" in the corner of the window.
            if event.type == pygame.QUIT:
                run = False
        SCREEN.fill((255, 255, 255)) # Fill the screen with color white on every while loop iteration.
        UserInput = pygame.key.get_pressed()

        # Two functions on the player object.
        player.draw(SCREEN) # This function will draw our "cuco" onto the screen.
        player.update(UserInput) # This function will update the "cuco" on every while loop iteration.

        clock.tick(30)   # Set the timing of the game.
        pygame.display.update()   # Update the display.









main()