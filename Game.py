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
RUN = [pygame.image.load(os.path.join("Images/doggo", "run1.png")),
          pygame.image.load(os.path.join("Images/doggo", "run2.png"))]

JUMP = pygame.image.load(os.path.join("Images/doggo", "jump.png"))

DUCK = [pygame.image.load(os.path.join("Images/doggo", "low1.png")),
          pygame.image.load(os.path.join("Images/doggo", "low2.png"))]

OBSTACLES = [pygame.image.load(os.path.join("Images/obstacles", "1.png")),
             pygame.image.load(os.path.join("Images/obstacles", "2.png")),
             pygame.image.load(os.path.join("Images/obstacles", "3.png")),
             pygame.image.load(os.path.join("Images/obstacles", "4.png")),
             pygame.image.load(os.path.join("Images/obstacles", "5.png")),
             pygame.image.load(os.path.join("Images/obstacles", "6.png"))]

BAT = [pygame.image.load(os.path.join("Images/bat", "bat1.png")),
       pygame.image.load(os.path.join("Images/bat", "bat2.png"))]
#BACKGROUND = pygame.image.load(os.path.join("Images/BG", ".png"))

# Class to create the "cuco".
class cuco:
    # X and Y position of our "cuco" on the screen.
    X_position = 80
    Y_Position = 310

    #def __init__


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