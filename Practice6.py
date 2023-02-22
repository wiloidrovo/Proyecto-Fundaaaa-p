import pygame
import os
import random
import math

pygame.init()

SCREEN = pygame.display.set_mode()
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()

pygame.display.set_caption("DOGGO GAME >:D")

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

#pygame.mixer.init()
SHORTFAR = pygame.mixer.Sound('shortfar.wav')

CARTOON = pygame.mixer.Sound('cartoon.wav')

MUSIC = pygame.mixer.music.load('mpb.mp3')

class doggo:
    X_POSITION = 150
    Y_POSITION = 350
    Y_POSITION_DUCK = 387
    JUMP_VELOCITY = 9.5

    def __init__(self):
        self.run_img = RUN
        self.jump_img = JUMP
        self.duck_img = DUCK
        self.dead_img = DEAD

        self.doggo_run = True
        self.doggo_jump = False
        self.doggo_duck = False
        self.doggo_dead = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VELOCITY
        self.image = self.run_img[0]
        self.doggo_rectangle = self.image.get_rect()
        self.doggo_rectangle.x = self.X_POSITION
        self.doggo_rectangle.y = self.Y_POSITION
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def update(self, death = False):
        if death:
            self.doggo_dead = True
            self.dead()
        else:
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
        if self.jump_vel <= -self.JUMP_VELOCITY:
            self.doggo_jump = False
            self.doggo_run = True
            self.doggo_duck = False
            self.doggo_dead = False
            self.jump_vel = self.JUMP_VELOCITY

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.doggo_rectangle = self.image.get_rect()
        self.doggo_rectangle.x = self.X_POSITION
        self.doggo_rectangle.y = self.Y_POSITION_DUCK
        self.step_index += 1

    def dead(self):
        self.image = self.dead_img
        if self.doggo_rectangle.y > self.Y_POSITION:
            self.doggo_rectangle.y = self.Y_POSITION

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.doggo_rectangle.x, self.doggo_rectangle.y))
        pygame.draw.rect(SCREEN, self.color,(self.doggo_rectangle), 2)
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

def distance(pos_a, pos_b):
    dx = pos_a[0]-pos_b[0]
    dy = pos_a[1]-pos_b[1]
    return math.sqrt(dx**2+dy**2)

def main():
    global game_speed, x_position_track, y_position_track, points, obstacles, x_position_back, y_position_back # The variable game_speed is to keep track how fast everything on our screen is moving.
    run = True
    clock = pygame.time.Clock()
    player = doggo()
    game_speed = 14
    x_position_track = 0
    y_position_track = 444
    x_position_back = 0
    y_position_back = 15
    points = 0
    font = pygame.font.Font('Space-Explorer.ttf', 35)
    obstacles = []
    death_count = 0

    def score():
        global game_speed, points
        points += 1
        if points % 100 == 0:
            game_speed += 1                              # (210, 105, 30)
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
            SCREEN.blit(TRACK, (image_width + x_position_track, y_position_track))
            x_position_track = 0
        x_position_track -= game_speed

    def background():
        global x_position_back, y_position_back  
        image_width = BACKGROUND.get_width()                
        SCREEN.blit(BACKGROUND, (x_position_back, y_position_back))
        SCREEN.blit(BACKGROUND, (image_width + x_position_back, y_position_back))
        if x_position_back <= -image_width:
            SCREEN.blit(BACKGROUND, (image_width + x_position_back, y_position_back))
            x_position_back = 0
        x_position_back -= game_speed
    x = 215
    xx = 256
    xxx = 221
    while run:
        for event in pygame.event.get():
            scape = pygame.key.get_pressed()
            if event.type == pygame.QUIT or scape[pygame.K_ESCAPE]:
                run = False
                pygame.quit()
                exit()
        SCREEN.fill((255, 228, 225))
        background()
        track()
        score()

        if len(obstacles) == 0:
            if random.randint(0, 1) == 0:
                obstacles.append(obst(OBSTACLES))
            elif random.randint(0, 1) == 1:
                obstacles.append(bat(BAT))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            pygame.draw.rect(SCREEN, (255, 0, 0), obstacle.rect, 2)
            obstacle.update()
            dist = distance((player.doggo_rectangle.x, player.doggo_rectangle.y),
                                        obstacle.rect.midtop)
            #x += 10
            #xxx += 10
            if dist < x and player.doggo_rectangle.y == player.Y_POSITION and obstacle.rect.y==350:
            #if dist > player.doggo_rectangle.colliderect(obstacle.rect) and player.doggo_rectangle.y == player.Y_POSITION and obstacle.rect.y==350:
                player.doggo_run = False
                player.doggo_jump = True
                player.doggo_duck = False
                player.doggo_dead = False
            elif dist < xx and player.doggo_rectangle.y == player.Y_POSITION and obstacle.rect.y==287:
                player.doggo_run = False
                player.doggo_jump = False
                player.doggo_duck = True
                player.doggo_dead = False
            elif dist < xxx and player.doggo_rectangle.y == player.Y_POSITION_DUCK and obstacle.rect.y==350:
                player.doggo_run = False
                player.doggo_jump = True
                player.doggo_duck = False
                player.doggo_dead = False

            if player.doggo_rectangle.colliderect(obstacle.rect):
                player.update(True)
                player.draw(SCREEN)
                pygame.display.update()
                SHORTFAR.play()
                pygame.time.delay(1000)
                death_count += 1
                menu(death_count)
        player.draw(SCREEN)
        player.update()
        clock.tick(30)
        pygame.display.update()

def menu(death_count):
    global points
    run = True
    while run:
        pygame.mixer.music.play(-1)
        SCREEN.fill((255, 228, 225))
        font = pygame.font.Font('Space-Explorer.ttf',30)
        font_exit = pygame.font.Font('Space-Explorer.ttf',20)
        text_exit = font_exit.render("PRESS ESCAPE TO EXIT", True, (164, 50, 50))
        text_rect = text_exit.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 300)
        SCREEN.blit(text_exit, text_rect)
        
        if death_count == 0:
            text = font.render("PRESS SPACE TO START", True, (125, 31, 28))
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            SCREEN.blit(text, text_rect)
            SCREEN.blit(START, (SCREEN_WIDTH // 2 - 33, SCREEN_HEIGHT // 2 - 140))
        else:
            text = font.render("PRESS SPACE TO RESTART", True, (125, 31, 28))
            score = font.render("YOUR SCORE: " + str(points), True, (125, 31, 28))
            score_rect = score.get_rect()
            score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 140)
            SCREEN.blit(score, score_rect)
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 180)
            SCREEN.blit(text, text_rect)
            SCREEN.blit(GAMEOVER, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 335))
        pygame.display.update()
        for event in pygame.event.get():
            space = pygame.key.get_pressed()
            if event.type == pygame.QUIT or space[pygame.K_ESCAPE]:
                run = False
            elif space[pygame.K_SPACE] == True:
                CARTOON.play()
                main()
    pygame.quit()
    exit()
menu(death_count=0)