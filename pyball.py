import pygame, sys, time
from random import *


class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        global points, score_text
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]
            points += 1
            score_text = font.render(str(points), 1, (0, 0, 0))

class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100, 20])
        image_surface.fill([0, 0, 0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

# initialize the screen
pygame.init()
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()

# initialize the ball and paddle
ball_speed = [10, 5]
my_ball = MyBallClass('wackyball.bmp', ball_speed, [50, 50])
ball_group = pygame.sprite.Group(my_ball)
paddle = MyPaddleClass([270, 400])

# initialize the score
points = 0
lives = 0
done = True
begin = True
font = pygame.font.Font(None, 50)
score_text = font.render(str(points), 1, (0, 0, 0))
textpos = [10, 10]

while 1:
    if begin:
        # message
        screen.fill([255, 255, 255])
        ft0_font = pygame.font.Font(None, 50)
        ft0_surf = font.render("Press 's' to start!", 1, (0, 0, 0))
        screen.blit(ft0_surf, [screen.get_width()/2 - ft0_surf.get_width()/2, 200])
        pygame.display.flip()
    else:
        clock.tick(60)
        screen.fill([255, 255, 255])

    # keyevents
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s or\
                event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            done = False
            begin = False
            lives = 3
            points = 0
            my_ball.rect.topleft = [choice([50, 300, 600]), 50]
            score_text = font.render(0, 1, (0, 0, 0))
            screen.blit(score_text, textpos)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            print 'Good bye'
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]

    # bound the ball
    if pygame.sprite.spritecollide(paddle, ball_group, False):
        my_ball.speed[1] = -my_ball.speed[1]
    my_ball.move()

    # show lives left
    if not done:
        screen.blit(my_ball.image, my_ball.rect)
        screen.blit(paddle.image, paddle.rect)
        screen.blit(score_text, textpos)
        for i in range(lives):
            width = screen.get_width()
            screen.blit(my_ball.image, [width-40*i, 20])
        pygame.display.flip()

    # when you lost one life
    if my_ball.rect.top >= screen.get_rect().bottom and not done:
        lives -= 1
        if lives == 0:
            final_text1 = "Game Over, press 'r' to restart. "
            final_text2 = "Your final score is: " + str(points)
            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = font.render(final_text1, 1, (0, 0, 0))
            ft2_font = pygame.font.Font(None, 50)
            ft2_surf = font.render(final_text2, 1, (0, 0, 0))
            screen.blit(ft1_surf, [screen.get_width()/2 - ft1_surf.get_width()/2, 100])
            screen.blit(ft2_surf, [screen.get_width()/2 - ft2_surf.get_width()/2, 200])
            pygame.display.flip()
            done = True
        else:
            ft3_font = pygame.font.Font(None, 50)
            ft3_surf = font.render('Oops, try again!', 1, (0, 0, 0))
            screen.blit(ft3_surf, [screen.get_width()/2 - ft3_surf.get_width()/2, 200])
            pygame.display.flip()
            time.sleep(2)
            my_ball.rect.topleft = [choice([50, 300, 600]), 50]
