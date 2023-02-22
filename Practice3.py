# This full code is just to make any changes to the original code
# withouth having to affect the original. I mean, it is just a copy
# to make here any crazy changes. So please ignore all this code. 


# Import libraries.
import pygame
import os # Lead us interact and obtain information from the operative system (OS).
import random
import math
import neat

# Initialize pygame.
pygame.init()

# Define global constants.
#SCREEN_HEIGHT = 690
#SCREEN_WIDTH = 1360
#SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Create the screen object.
SCREEN = pygame.display.set_mode()  # Initialize a window or screen for display.
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()

pygame.display.set_caption("DOGGO GAME >:D")

# Load all the images of the game.
START = pygame.image.load(os.path.join("Images/doggo", "start.png"))

RUN = [pygame.image.load(os.path.join("Images/doggo", "run1.png")),
       pygame.image.load(os.path.join("Images/doggo", "run2.png"))]

JUMP = pygame.image.load(os.path.join("Images/doggo", "jump.png"))

DUCK = [pygame.image.load(os.path.join("Images/doggo", "low1.png")),
        pygame.image.load(os.path.join("Images/doggo", "low2.png"))]

DEAD = pygame.image.load(os.path.join("Images/doggo", "dead.png"))

OBSTACLES = [pygame.image.load(os.path.join("Images/obstacles", "1.png")),
             pygame.image.load(os.path.join("Images/obstacles", "2.png")),
             pygame.image.load(os.path.join("Images/obstacles", "3.png")),
             pygame.image.load(os.path.join("Images/obstacles", "4.png")),
             pygame.image.load(os.path.join("Images/obstacles", "5.png")),
             pygame.image.load(os.path.join("Images/obstacles", "6.png"))]

BAT = [pygame.image.load(os.path.join("Images/bat", "bat1.png")),
       pygame.image.load(os.path.join("Images/bat", "bat2.png"))]

GAMEOVER = pygame.image.load(os.path.join("Images/other", "game-over.png"))

RESET = pygame.image.load(os.path.join("Images/other", "reset.png"))

TRACK = pygame.image.load(os.path.join("Images/other", "track.png"))

BACKGROUND = pygame.image.load(os.path.join("Images/other", "back.png"))

#pygame.mixer.init() # To initialize mixer module of pygame.

SHORTFAR = pygame.mixer.Sound('shortfar.wav') # Create a new Sound object from a file or buffer object.

CARTOON = pygame.mixer.Sound('cartoon.wav')

MUSIC = pygame.mixer.music.load('mpb.mp3')    # Load a music file for playback.
#MUSIC = pygame.mixer.music.load('LaLla.mp3')
#MUSIC = pygame.mixer.music.load('HRW.mp3')
#MUSIC = pygame.mixer.music.load('Nia.mp3')

# Class to create the "doggo".
class doggo:
    # X and Y position of our "doggo" on the screen.
    X_POSITION = 150
    Y_POSITION = 350

    # The image of the "doggo" ducking is smaller than the "doggo" running.
    Y_POSITION_DUCK = 387

    # This variable defines the velocity in which "doggo" will jump
    JUMP_VELOCITY = 9.5

# This method will initialize the "doggo" whenever an object of this class is created.
    def __init__(self):
        # Include all of the images of the "doggo".
        self.run_img = RUN
        self.jump_img = JUMP
        self.duck_img = DUCK
        #self.dead_img = DEAD

        self.doggo_run = True
        self.doggo_jump = False
        self.doggo_duck = False
        #self.doggo_dead = False

        self.step_index = 0  # To animate the "doggo".
        self.jump_vel = self.JUMP_VELOCITY  # We initialize the jumping velocity of the "doggo" to the JUMP_Velocity that we just defined before.
        self.image = self.run_img[0]  # To initialize the first image, when our "doggo" is created
        self.doggo_rectangle = self.image.get_rect()  # To get the rectangle of the "doggo" image (hitbox).

        # To set the x and y coord of the rectangle of the "doggo" image to the x and y coord of lines 70-71. 
        self.doggo_rectangle.x = self.X_POSITION
        self.doggo_rectangle.y = self.Y_POSITION
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def update(self):    # Update function, it updates the "doggo" on every while loop iteration.
        #if death:
        #    self.doggo_dead = True
        #    self.dead()
        #else:
        if self.doggo_run:          # This 3-line code block check
            self.run()              # the state for the "doggo", and
        if self.doggo_jump:         # depending on whether the "doggo"
            self.jump()             # is running, jumping or ducking a
        if self.doggo_duck:         # corresponding function will be called.
            self.duck()

        if self.step_index >= 10:   # This will be reset every 10 steps, this will help us to animate
            self.step_index = 0     # the "dogo" further down the line.

        # Statements that help us set the state our "doggo" is in.
        #if UserInput[pygame.K_UP] and not self.doggo_jump and not death:
        # If we press the up key on our keyboard and our "doggo" is not currently jumping 
        # then we want to set the jumping state to True and the others to False.
            #self.doggo_run = False
            #self.doggo_jump = True
            #self.doggo_duck = False
            #self.doggo_dead = False
        #elif UserInput[pygame.K_DOWN] and not self.doggo_jump and not death:
        # If we press the up down on our keyboard and our "doggo" is not currently jumping 
        # then we want to set the ducking state to True and the others to False.
            #self.doggo_run = False
            #self.doggo_jump = False
            #self.doggo_duck = True
            #self.doggo_dead = False
        #elif not (self.doggo_jump or UserInput[pygame.K_DOWN]) and not death:
        # If the "doggo" is not jumping and the UserInput is not down so the "doggo"
        # is not ducking then we want the "doggo" to just run and the others are False.
            #self.doggo_run = True
            #self.doggo_jump = False
            #self.doggo_duck = False
            #self.doggo_dead = False
        #elif death:
        #    self.doggo_run = False
        #    self.doggo_jump = False 
        #    self.doggo_duck = False
        #    self.doggo_dead = True

    def run(self):   # Run function.
        self.image = self.run_img[self.step_index // 5] # This variable called image is set to the corresponding image of the "doggo" running.
                                                        # The variable step_index helps us rotate through the individual images of the "doggo"
                                                        # running in order to make it look like it's being animated.
        self.doggo_rectangle = self.image.get_rect()    # To get the rectangle coord of the "doggo" image.
        
        self.doggo_rectangle.x = self.X_POSITION        # To set the rectangle coord to the position on the
        self.doggo_rectangle.y = self.Y_POSITION        # screen where we want the "doggo" to be displayed.
        self.step_index += 1                            # Increment the step_index by 1.
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
        if self.jump_vel <= -self.JUMP_VELOCITY:  # As soon as the velocity of "doggo" reaches the value of -9.5 we set "doggo" jump to false.
            self.doggo_jump = False
            self.doggo_run = True
            self.doggo_duck = False
            self.jump_vel = self.JUMP_VELOCITY    # Reset the jump velocity of "doggo".

    def duck(self):   # Duck function. It is identical to the run function, but the only difference is the following:
        self.image = self.duck_img[self.step_index // 5] # We change the image of self.run_img for self.duck_img.
        self.doggo_rectangle = self.image.get_rect()
        self.doggo_rectangle.x = self.X_POSITION
        self.doggo_rectangle.y = self.Y_POSITION_DUCK    # We set the y position to Y_position_duck instead of Y_position.
        self.step_index += 1

    #def dead(self):
    #    self.image = self.dead_img
    #    if self.doggo_rectangle.y > self.Y_POSITION:
    #        self.doggo_rectangle.y = self.Y_POSITION


    def draw(self, SCREEN):   # This function blits the image onto the screen.
        SCREEN.blit(self.image, (self.doggo_rectangle.x, self.doggo_rectangle.y))
        pygame.draw.rect(SCREEN, self.color,(self.doggo_rectangle), 2)
        for obstacle in obstacles:
            pygame.draw.line(SCREEN, self.color, (self.doggo_rectangle.x + 90, self.doggo_rectangle.y + 55), obstacle.rect.center, 2)

class obstacle:   # Parent class for all the obstacles.
    def __init__(self, image, type):
        self.image = image
        self.type = type  # Type is going to be an integer value between 0 and 1 and it's going to determine
                          # what type of obstacle image is going to be displayed on our screen.
        self.rect = self.image[self.type].get_rect()  # To get the rectangle coord of the image which we're displaying.
        self.rect.x = SCREEN_WIDTH  # To set the x coord of the obstacle to the screen width. / Whenever an obstacle is
                                    # created, it is just off the edge of the right-hand side of the screen.

    def update(self):  # This will help us move the obstacle across the screen.
        self.rect.x -= game_speed  # We can do this by simply decreasing the x-coord of the rectangle of the image by the game speed.
        if self.rect.x < -self.rect.width: # This if statement is going to help us remove the obstacle
            obstacles.pop()   # as soon as it moves off the screen on the left-hand side.

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)  # Here we're simply going to blit the image onto our screen.

class obst(obstacle):  # This class inherit the class obstacle.
    def __init__(self, image):
        self.type = random.randint(0, 5) # Set the type to a random int between 0 and 5.
        super().__init__(image, self.type) # To initialize the init method of the parent class (class obstacle).
        self.rect.y = 350 # Set the y coord of where we want the obstacles to be displayed.

class bat(obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 287
        self.index = 0
    def draw(self, SCREEN): # For the first five times this draw function is called, the first
        if self.index >= 11: # image of our bat is going to be shown. The next five times it is
            self.index = 0  # called, the second image of our bat is going to be shown and then
        SCREEN.blit(self.image[self.index // 6], self.rect) # on the 11 th iteration we're gonna
        self.index += 1     # reset the index back to zero. It makes the bat look animated.

def remove(index):
    dogs.pop(index)
    ge.pop(index)
    nets.pop(index)

def distance(pos_a, pos_b):
    dx = pos_a[0]-pos_b[0]
    dy = pos_a[1]-pos_b[1]
    return math.sqrt(dx**2+dy**2)

def eval_genomes(genomes, config):
    global game_speed, x_position_track, y_position_track, points, obstacles, x_position_back, y_position_back, dogs, ge, nets # The variable game_speed is to keep track how fast everything on our screen is moving.
    run = True   # Flag to our while loop.
    clock = pygame.time.Clock()   # Setup the clock for a decent framerate
    
    obstacles = []
    dogs = []   # dogs is going to be an instance/object of the class "doggo".
    ge = []
    nets = []
    
    game_speed = 14
    x_position_track = 0
    y_position_track = 444
    x_position_back = 0
    y_position_back = 15
    points = 0
    font = pygame.font.Font('Space-Explorer.ttf',35) # Font used to display the score.
    #obstacles = []
    #death_count = 0

    for genome_id, genome in genomes:
        dogs.append(doggo())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    def score():
        global game_speed, points
        points += 1 # Every single time the function is called, we increment the variable points by 1.
        if points % 100 == 0:  # Check and whenever points is multiple of 100 we increment the game_speed by 1 unit.
            game_speed += 1                              # (210, 105, 30)
        text = font.render("POINTS: " + str(points), True, (125, 31, 28)) # Display the text of our points on the screen.
        text_rectangle = text.get_rect()   # Get the coord of the rectangle within wich the points are displayed.
        text_rectangle.center = (1200, 40) # Set the rectangle center to the top right corner of the screen.
        SCREEN.blit(text, text_rectangle)  # Blit text_rectangle on the screen.

    def track():
        global x_position_track, y_position_track      # Global coord of the track.
        image_width = TRACK.get_width()                # Image width of our track image.
        SCREEN.blit(TRACK, (x_position_track, y_position_track)) # Blit the image onto our screen.
        SCREEN.blit(TRACK, (image_width + x_position_track, y_position_track)) # Behind the previous image we add this another one.
        if x_position_track <= -image_width: # Whenever one track image moves off the screen, another one is created right after.
            SCREEN.blit(TRACK, (image_width + x_position_track, y_position_track))
            x_position_track = 0
        x_position_track -= game_speed # From the x position of our track we subtract the game_speed.

    def background():
        global x_position_back, y_position_back  
        image_width = BACKGROUND.get_width()                
        SCREEN.blit(BACKGROUND, (x_position_back, y_position_back)) # Blit the image onto our screen.
        SCREEN.blit(BACKGROUND, (image_width + x_position_back, y_position_back)) # Behind the previous image we add this another one.
        if x_position_back <= -image_width: # Whenever one back image moves off the screen, another one is created right after.
            SCREEN.blit(BACKGROUND, (image_width + x_position_back, y_position_back))
            x_position_back = 0
        x_position_back -= game_speed # From the x position of our track we subtract the game_speed.

# Everything in pygame runs in a while loop.
    while run:
        for event in pygame.event.get(): # To exit the game safety/ We set the flag in false whenever we press the "X".
            scape = pygame.key.get_pressed()
            if event.type == pygame.QUIT or scape[pygame.K_ESCAPE]:
            #if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
        SCREEN.fill((255, 228, 225)) # Fill the screen with color "pink" on every while loop iteration.
        background()
        track()
        score()
        #UserInput = pygame.key.get_pressed()
        #for dog in dogs:
        #    pygame.draw.rect(SCREEN, (255, 0, 0), dog.doggo_rectangle, 2)
        if len(dogs) == 0:
            break
        if len(obstacles) == 0:   # If the lenght of the obstacles' list is equal to 0,
            if random.randint(0, 1) == 0: # then we want to randomly create either the
                obstacles.append(obst(OBSTACLES)) # obst or the bat by appending one of
            elif random.randint(0, 1) == 1: # these objects to the obstacles' list.
                obstacles.append(bat(BAT))

        for obstacle in obstacles: # We call the draw and update function on every
            obstacle.draw(SCREEN)  # single obstacle on the obstacles' list.
            #pygame.draw.rect(SCREEN, (255, 0, 0), obstacle.rect, 2)
            obstacle.update()
            for i, dog in enumerate(dogs):
                if dog.doggo_rectangle.colliderect(obstacle.rect): # If the rectangle of the doggo image collides with the rectangle of an obstacle
                    ge[i].fitness -= 1
                    remove(i)
                    #dog.update(UserInput, True)
                    #dog.draw(SCREEN)
                    #pygame.draw.rect(SCREEN, (255, 0, 0), dog.doggo_rectangle, 2) # image, we want the hitbox of the doggo to turn red.
                    #pygame.display.update() # Update portions of the screen for software displays.
                    #SHORTFAR.play()
                    #pygame.time.delay(1000) # When we run into an obstacle I first want a small time delay before going to the main menu.
                    #death_count += 1
                    #menu(death_count)

            for i, dog in enumerate(dogs):
                output = nets[i].activate((dog.doggo_rectangle.y, obstacle.rect.y,
                                        distance((dog.doggo_rectangle.x, dog.doggo_rectangle.y),
                                         obstacle.rect.midtop)))
                if output[0] > 0.1 and dog.doggo_rectangle.y == dog.Y_POSITION and obstacle.rect.y==350:
                    dog.doggo_run = False
                    dog.doggo_jump = True
                    dog.doggo_duck = False
                elif output[0] > 0.1 and dog.doggo_rectangle.y == dog.Y_POSITION and obstacle.rect.y==287:
                    dog.doggo_run = False
                    dog.doggo_jump = False
                    dog.doggo_duck = True
                elif output[0] > 0.1 and dog.doggo_rectangle.y == dog.Y_POSITION_DUCK and obstacle.rect.y==350:
                    dog.doggo_run = False
                    dog.doggo_jump = True
                    dog.doggo_duck = False
                #dog.doggo_dead = False
            #dog.update(UserInput)
        # Two functions on the dogs object.
        for dog in dogs:
            dog.update()
            dog.draw(SCREEN) # This function will draw our "doggo" onto the screen.
            # # This function will update the "doggo" on every while loop iteration.

        clock.tick(30)   # Set the timing of the game.
        pygame.display.update()   # Update portions of the screen for software displays.

# Setup the NEAT
def run_neat(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)
    pop.run(eval_genomes, 50)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run_neat(config_path)


#def menu(death_count):
#    global points
#    run = True
#    while run:
#        pygame.mixer.music.play(-1)
#        SCREEN.fill((255, 228, 225))
#        font = pygame.font.Font('Space-Explorer.ttf',30)
#        font_exit = pygame.font.Font('Space-Explorer.ttf',20)
#        text_exit = font_exit.render("PRESS ESCAPE TO EXIT", True, (164, 50, 50))
#        text_rect = text_exit.get_rect()
#        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 300)
#        SCREEN.blit(text_exit, text_rect)
        
#        if death_count == 0:
#            text = font.render("PRESS SPACE TO START", True, (125, 31, 28))
#            text_rect = text.get_rect()
#            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#            SCREEN.blit(text, text_rect)
#            SCREEN.blit(START, (SCREEN_WIDTH // 2 - 33, SCREEN_HEIGHT // 2 - 140))
#        else:
#            text = font.render("PRESS SPACE TO RESTART", True, (125, 31, 28))
#            score = font.render("YOUR SCORE: " + str(points), True, (125, 31, 28))
#            score_rect = score.get_rect()
#            score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 140)
#            SCREEN.blit(score, score_rect)
#            text_rect = text.get_rect()
#            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 180)
#            SCREEN.blit(text, text_rect)
#            SCREEN.blit(GAMEOVER, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 335))
#        pygame.display.update() # Update portions of the screen for software displays.
#        for event in pygame.event.get():
#            space = pygame.key.get_pressed() # get_pressed returns the state of all the keyboard keys as a bolean.
#            if event.type == pygame.QUIT or space[pygame.K_ESCAPE]:
#                run = False
#            elif space[pygame.K_SPACE] == True:
#                CARTOON.play()
#                #main()
#    pygame.quit()
#    exit()

#menu(death_count=0)