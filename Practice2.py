import pygame
import os
import random
import math
import neat

pygame.init()

SCREEN = pygame.display.set_mode()
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()

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

class doggo:
    X_POSITION = 150
    Y_POSITION = 350
    Y_POSITION_DUCK = 387
    JUMP_VELOCITY = 9.5

    def __init__(self):
        self.run_img = RUN
        self.jump_img = JUMP
        self.duck_img = DUCK
        #self.dead_img = DEAD

        self.doggo_run = True
        self.doggo_jump = False
        self.doggo_duck = False
        #self.doggo_dead = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VELOCITY
        self.image = self.run_img[0]
        self.doggo_rectangle = self.image.get_rect()

        self.doggo_rectangle.x = self.X_POSITION
        self.doggo_rectangle.y = self.Y_POSITION
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def update(self):
        #if death:
        #    self.doggo_dead = True
        #    self.dead()
        #else:
        if self.doggo_run:
            self.run()
        if self.doggo_jump:
            self.jump()
        if self.doggo_duck:
            self.duck()
        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.doggo_rectangle = self.image.get_rect()
        
        self.doggo_rectangle.x = self.X_POSITION
        self.doggo_rectangle.y = self.Y_POSITION
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.doggo_jump:
            self.doggo_rectangle.y -= self.jump_vel * 4
            self.jump_vel -= 1.0
        if self.jump_vel < -self.JUMP_VELOCITY:
            self.doggo_jump = False
            self.doggo_run = True
            self.jump_vel = self.JUMP_VELOCITY

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.doggo_rectangle = self.image.get_rect()
        self.doggo_rectangle.x = self.X_POSITION
        self.doggo_rectangle.y = self.Y_Position_duck
        self.step_index += 1

    #def dead(self):
    #    self.image = self.dead_img
    #    if self.doggo_rectangle.y > self.Y_POSITION:
    #       self.doggo_rectangle.y = self.Y_POSITION


    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.doggo_rectangle.x, self.doggo_rectangle.y))
        #pygame.draw.rect(SCREEN, self.color, (self.doggo_rectangle.x, self.doggo_rectangle.y, self.rect.width, self.rect.height), 2)
        for obstacle in obstacles:
            pygame.draw.line(SCREEN, self.color, (self.doggo_rectangle.x + 90, self.doggo_rectangle.y + 55), obstacle.rect.center, 2)

class obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class obst(obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 5)
        super().__init__(image, self.type)
        self.rect.y = 350

class bat(obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 287
        self.index = 0
    def draw(self, SCREEN):
        if self.index >= 11:
            self.index = 0
        SCREEN.blit(self.image[self.index // 6], self.rect)
        self.index += 1

def remove(index):
    dogs.pop(index)
    ge.pop(index)
    nets.pop(index)

def distance(pos_a, pos_b):
    dx = pos_a[0]-pos_b[0]
    dy = pos_a[1]-pos_b[1]
    return math.sqrt(dx**2+dy**2)

def eval_genomes(genomes, config):
    global game_speed, x_position_track, y_position_track, points, obstacles, x_position_back, y_position_back, dogs, ge, nets
    clock = pygame.time.Clock()
    points = 0
    
    obstacles = []
    dogs = []
    ge = []
    nets = []
    
    x_position_track = 0
    y_position_track = 444
    x_position_back = 0
    y_position_back = 15
    game_speed = 14
    font = pygame.font.Font('Space-Explorer.ttf',35)

    for genome_id, genome in genomes:
        dogs.append(doggo())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    def score():
        global game_speed, points
        points += 1
        if points % 100 == 0:
            game_speed += 1
        text = font.render("POINTS: " + str(points), True, (125, 31, 28))
        text_rectangle = text.get_rect()
        text_rectangle.center = (1200, 40)
        SCREEN.blit(text, text_rectangle)

    def track():
        global x_position_track, y_position_track
        image_width = TRACK.get_width()
        SCREEN.blit(TRACK, (x_position_track, y_position_track))
        SCREEN.blit(TRACK, (image_width + x_position_track, y_position_track))
        if x_position_track <= -image_width:
            #SCREEN.blit(TRACK, (image_width + x_position_track, y_position_track))
            x_position_track = 0
        x_position_track -= game_speed

    def background():
        global x_position_back, y_position_back  
        image_width = BACKGROUND.get_width()                
        SCREEN.blit(BACKGROUND, (x_position_back, y_position_back))
        SCREEN.blit(BACKGROUND, (image_width + x_position_back, y_position_back))
        if x_position_back <= -image_width:
            #SCREEN.blit(BACKGROUND, (image_width + x_position_back, y_position_back))
            x_position_back = 0
        x_position_back -= game_speed

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        SCREEN.fill((255, 228, 225))
        background()
        track()
        score()

        for dog in dogs:
            dog.update()
            dog.draw(SCREEN)

        if len(dogs) == 0:
            break

        if len(obstacles) == 0:
            if random.randint(0, 1) == 0:
                obstacles.append(obst(OBSTACLES))
            elif random.randint(0, 1) == 1:
                obstacles.append(bat(BAT))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            for i, dog in enumerate(dogs):
                if dog.doggo_rectangle.colliderect(obstacle.rect):
                    ge[i].fitness -= 1
                    remove(i)

        for i, dog in enumerate(dogs):
            output = nets[i].activate((dog.doggo_rectangle.y,
                                       distance((dog.doggo_rectangle.x, dog.doggo_rectangle.y),
                                        obstacle.rect.midtop)))
            if output[0] > 0.5 and dog.doggo_rectangle.y == dog.Y_POSITION:
                dog.doggo_run = False
                dog.doggo_jump = True
                dog.doggo_duck = False
                #dog.doggo_dead = False
        clock.tick(30)
        pygame.display.update()

def run(config_path):
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
    run(config_path)