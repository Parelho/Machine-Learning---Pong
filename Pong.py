import pygame
import random

pygame.init()

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)

DIVISION = pygame.Rect(450, 35, 15, 535)
LEFT_RECTANGLE = pygame.Rect(25, 250, 10, 100)
RIGHT_RECTANGLE = pygame.Rect(875, 250, 10, 100)
BALL = pygame.Rect(450, 250, 15, 15)
TOP_DIVISION = pygame.Rect(0, 35, 900, 15)
BOTTOM_DIVISION = pygame.Rect(0, 565, 900, 15)
RIGHT_DIVISION = pygame.Rect(0, 35, 15, 535)
LEFT_DIVISION = pygame.Rect(885, 35, 15, 535)

FPS = 60
VEL = 10



def movement_left(keys_pressed, LEFT_RECTANGLE):
    if keys_pressed[pygame.K_s]:
        if LEFT_RECTANGLE.y > 480:
            VEL - 10
        else:
            LEFT_RECTANGLE.y += VEL
    if keys_pressed[pygame.K_w]:
        if LEFT_RECTANGLE.y < 20:
            VEL - 10
        else:
            LEFT_RECTANGLE.y -= VEL

def movement_right(RIGHT_RECTANGLE):
    RIGHT_RECTANGLE.y = BALL.y - 50



def draw_window():
    WIN.fill(BLACK)

    pygame.draw.rect(WIN, GREY, DIVISION)
    pygame.draw.rect(WIN, WHITE, BALL)
    pygame.draw.rect(WIN, GREY, RIGHT_DIVISION)
    pygame.draw.rect(WIN, GREY, LEFT_DIVISION)
    pygame.draw.rect(WIN, GREY, TOP_DIVISION)
    pygame.draw.rect(WIN, GREY, BOTTOM_DIVISION)
    pygame.draw.rect(WIN, WHITE, LEFT_RECTANGLE)
    pygame.draw.rect(WIN, WHITE, RIGHT_RECTANGLE)

BALL_SPEED = 7.5
change_choices = (-1, 1)
change = random.choice(change_choices)
change_y = 1

font = pygame.font.Font('freesansbold.ttf', 32)
score_1 = 0
score_2 = 0
textx1 = 50
texty1 = 25
textx2 = 750
texty2 = 25

def show_score1(x, y):
    score = font.render("Score:" + str(score_1), True, (WHITE))
    WIN.blit(score, (x, y))

def show_score2(x, y):
    score = font.render("Score:" + str(score_2), True, (WHITE))
    WIN.blit(score, (x, y))

def main():

    global change
    global change_y
    global score_1
    global score_2
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if pygame.Rect.colliderect(BALL, RIGHT_RECTANGLE):
            change = -1
        if pygame.Rect.colliderect(BALL, LEFT_RECTANGLE):
            change = 1
        BALL.x += BALL_SPEED * change

        if BALL.y < 50:
            change_y = 1
        if BALL.y > 550:
            change_y = -1
        BALL.y += (BALL_SPEED/2 + 1) * change_y

        if BALL.x > 920:
            BALL.x = 450
            score_2 += 1
        if BALL.x < -20:
            BALL.x = 450
            score_1 += 1

        keys_pressed = pygame.key.get_pressed()
        movement_left(keys_pressed, LEFT_RECTANGLE)
        movement_right(RIGHT_RECTANGLE)

        draw_window()
        show_score1(textx1, texty1)
        show_score2(textx2, texty2)
        pygame.display.update()
main()