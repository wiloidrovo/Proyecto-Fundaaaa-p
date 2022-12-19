# Import libraries
import pygame
import os # Lead us interact and obtain information from the operative system (OS). 
          # Its very easy to use and there exists full information about this.

# Initialize pygame
pygame.init()

# Define global constants
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load all the images of the game 
RUNNIG = [pygame.image.load(os.path.join("Images/Dino", "DinoRun1.png")), 
          pygame.image.load(os.path.join("Images/Dino", "DinoRun2.png"))]
JUMPING = 
DUCKING = 
OBSTACLES = 
BACKGROUND = pygame.image.load(os.path.join("Images/BG", "Track.png"))

# Everything in pygame runs in a while loop
def main()


#comment test
