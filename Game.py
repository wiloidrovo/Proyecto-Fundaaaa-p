# Import libraries.
import pygame
import os # Lead us interact and obtain information from the operative system (OS).
import random

# Initialize pygame.
pygame.init()

# Define global constants.
SCREEN_HEIGHT = 620
SCREEN_WIDTH = 1200
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

CLOUD = pygame.image.load(os.path.join("Images/other", "cloud.png"))

GAMEOVER = pygame.image.load(os.path.join("Images/other", "game-over.png"))

RESET = pygame.image.load(os.path.join("Images/other", "reset.png"))

TRACK = pygame.image.load(os.path.join("Images/other", "track.png"))

# Class to create the "doggo".
class doggo:
    # X and Y position of our "doggo" on the screen.
    X_Position = 150
    Y_Position = 350

    # The image of the "doggo" ducking is smaller than the "doggo" running.
    Y_Position_duck = 380

    # This variable defines the velocity in which "doggo" will jump
    JUMP_Velocity = 9.5

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
        self.jump_vel = self.JUMP_Velocity  # We initialize the jumping velocity of the "doggo" to the JUMP_Velocity that we just defined before.
        self.image = self.run_img[0]   # To initialize the first image, when our "doggo" is created
        self.doggo_rectangle = self.image.get_rect()   # To get the rectangle of the "doggo" image (hitbox).

        # To set the x and y coord of the rectangle of the "doggo" image to the x and y coord of lines 44-45. 
        self.doggo_rectangle.x = self.X_Position
        self.doggo_rectangle.y = self.Y_Position

    def update(self, UserInput):    # Update function, it updates the "doggo" on every while loop iteration.
        if self.doggo_run:          # This 3-line code block check
            self.run()              # the state for the "doggo", and
        if self.doggo_jump:         # depending on whether the "doggo"
            self.jump()             # is running, jumping or ducking a
        if self.doggo_duck:         # corresponding function will be called.
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

    def run(self):   # Run function.
        self.image = self.run_img[self.step_index // 5]  # This variable called image is set to the corresponding image of the "doggo" running.
                                                         # The variable step_index helps us rotate through the individual images of the "doggo"
                                                         # running in order to make it look like it's being animated.
        self.doggo_rectangle = self.image.get_rect()     # To get the rectangle coord of the "doggo" image.
        
        self.doggo_rectangle.x = self.X_Position         # To set the rectangle coord to the position on the
        self.doggo_rectangle.y = self.Y_Position         # screen where we want the "doggo" to be displayed.
        self.step_index += 1                             # Increment the step_index by 1.
                                                         # When the step_index is between the values 0 and 5 the first image of our "doggo" is displayed
                                                         # and when the step_index is between the values 5 and 10 the second image of our "doggo" is displayed.
                                                         # and beyond the value of 10 the step_index is reset.

    def jump(self):
        self.image = self.jump_img
        if self.doggo_jump:   # If the state of the "doggo" is set to jumping
            self.doggo_rectangle.y -= self.jump_vel * 4 # We decrease the y position of our "doggo".
            self.jump_vel -= 1.0  # At the same time we decrease the velocity at which "doggo" is jumping.
            # Remember, when "doggo" leaves the floor for the jump, its velocity is 9.5 pixel/while loop iteration. At the top of the jump its
            # velocity is 0 and then when "doggo" moves down again and reaches the same position at the beggining, its velocity will be 9.5 again,
            # but now the velocity vector points down, so now it is -9.5.
        if self.jump_vel < -self.JUMP_Velocity:  # As soon as the velocity of "doggo" reaches the value of -9.5 we set "doggo" jump to false.
            self.doggo_jump = False
            self.jump_vel = self.JUMP_Velocity    # Reset the jump velocity of "doggo".


    def duck(self):   # Duck function. It is identical to the run function, but the only difference is the following:
        self.image = self.duck_img[self.step_index // 5] # We change the image of self.run_img for self.duck_img.
        self.doggo_rectangle = self.image.get_rect()
        self.doggo_rectangle.x = self.X_Position
        self.doggo_rectangle.y = self.Y_Position_duck    # We set the y position to Y_position_duck instead of Y_position.
        self.step_index += 1

    def draw(self, SCREEN):   # This function blits the image onto the screen.
        SCREEN.blit(self.image, (self.doggo_rectangle.x, self.doggo_rectangle.y))

class cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(1, 3)  # Specify the coord of the cloud when it is created.
        self.y = random.randint(40, 80)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):   # We make the cloud move from the right hand side of the screen to the left.
        self.x -= game_speed
        # Whenever the cloud moves out of the screen we reset the coord of the cloud so that it apears again
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(1, 3)
            self.y = random.randint(40, 80)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))   # We just blit the image onto our screen.

def main():
    global game_speed   # This variable is to keep track how fast everything on our screen is moving.
    run = True   # Flag to our while loop.
    clock = pygame.time.Clock()   # Clock to time our game.
    player = doggo()   # Player is going to be an instance of the class "doggo".
    Cloud = cloud()
    game_speed = 15

# Everything in pygame runs in a while loop.
    while run:
        for event in pygame.event.get(): # To exit the game safety/ We will set the flag in false whenever
                                         # we press the "X" in the corner of the window.
            if event.type == pygame.QUIT:
                run = False
        SCREEN.fill((255, 228, 225)) # Fill the screen with color white on every while loop iteration.
        UserInput = pygame.key.get_pressed()

        # Two functions on the player object.
        player.draw(SCREEN) # This function will draw our "doggo" onto the screen.
        player.update(UserInput) # This function will update the "doggo" on every while loop iteration.

        Cloud.draw(SCREEN)
        Cloud.update()

        clock.tick(30)   # Set the timing of the game.
        pygame.display.update()   # Update the display.

main()