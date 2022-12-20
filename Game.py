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

#BACKGROUND = pygame.image.load(os.path.join("Images/bg", ".png"))

# Class to create the "doggo".
class doggo:
    # X and Y position of our "doggo" on the screen.
    X_position = 80
    Y_Position = 310
# This method will initialize the "doggo" whenever an object of this class is created.
    def __init__(self):
        # Include all of the images of the "doggo".
        self.run_img = RUN
        self.jump_img = JUMP
        self.duck_img = DUCK

        self.doggo_run = True
        self.doggo_jump = False
        self.doggo_duck = False

        self.step_index = 0   # To animate the "doggo".
        self.image = self.run_img[0]   # To initialize the first image, when our "doggo" is created
        self.doggo_rectangle = self.image.get_rect()   # To get the rectangle of the "doggo" image (hitbox).

        # To set the x and y coord of the rectangle of the "doggo" image to the x and y coord of lines 38-39. 
        self.doggo_rectangle.x = self.X_position
        self.doggo_rectangle.y = self.Y_Position

    def update(self, UserInput):   # Update function, it updates the "doggo" on every while loop iteration.
        if self.doggo_run:    # This 3-line code block check
            self.run()        # the state for the "doggo", and
        if self.doggo_jump:   # depending on whether the "doggo"
            self.jump()       # is running, jumping or ducking a
        if self.doggo_duck:   # corresponding function will be called.
            self.duck()

        if self.step_index >= 10:   # This will be reset every 10 steps, this will help us to animate
            self.step_index = 0     # the "dogo" further down the line.

        # Statements that help us set the state our "doggo" is in.
        if UserInput[pygame.K_UP] and not self.doggo_jump:
        # If we press the up key on our keyboard and our "doggo" is not currently jumping 
        # then we want to set the jumping state to True and the others to False.
            self.doggo_run = False
            self.doggo_jump = True
            self.doggo_duck = False
        elif UserInput[pygame.K_DOWN] and not self.doggo_jump:
        # If we press the up down on our keyboard and our "doggo" is not currently jumping 
        # then we want to set the ducking state to True and the others to False.
            self.doggo_run = False
            self.doggo_jump = False
            self.doggo_duck = True
        elif not (self.doggo_jump or UserInput[pygame.K_DOWN]):
        # If the "doggo" is not jumping and the UserInput is not down so the "doggo"
        # is not ducking then we want the "doggo" to just run and the others are False.
            self.doggo_run = True  # (Probar poner UserInput[pygame.K_UP] en vez de self.doggo_jump en la linea anterior)
            self.doggo_jump = False
            self.doggo_duck = False

    def run(self):

#    def jump(self):

#    def duck(self):

# Everything in pygame runs in a while loop.
def main():
    run = True   # Flag to our while loop.
    clock = pygame.time.Clock()   # Clock to time our game.
    player = doggo()   # Player is going to be an instance of the class "doggo"

    while run:
        for event in pygame.event.get(): # To exit the game safety/ We will set the flag in false whenever
                                         # we press the "X" in the corner of the window.
            if event.type == pygame.QUIT:
                run = False
        SCREEN.fill((255, 255, 255)) # Fill the screen with color white on every while loop iteration.
        UserInput = pygame.key.get_pressed()

        # Two functions on the player object.
        player.draw(SCREEN) # This function will draw our "doggo" onto the screen.
        player.update(UserInput) # This function will update the "doggo" on every while loop iteration.

        clock.tick(30)   # Set the timing of the game.
        pygame.display.update()   # Update the display.









main()