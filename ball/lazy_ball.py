#!/usr/bin/env python3

import sys
import pygame

from pygame.constants import KEYDOWN, K_ESCAPE, K_LEFT, K_RIGHT, KEYUP

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

screen = pygame.display.set_mode((800, 600))

ball_move = [-1, -2]

ball = pygame.Rect(400, 300, 40, 40)

paddle = pygame.Rect(390, 575, 60, 20)
paddle_move = [0, 0]


def process_event(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    global paddle_move
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.key == K_LEFT:
            paddle_move = [-1, 0]
        if event.key == K_RIGHT:
            paddle_move = [1, 0]
    if event.type == KEYUP:
        if event.key == K_LEFT or event.key == K_RIGHT:
            paddle_move = [0, 0]
    #print("Event ", event)


def maxmove(x, mx):
    if (x < -1 * mx):
        return -1 * mx
    if (x > mx):
        return mx
    return x


def game_tick():
    global ball, paddle, paddle_move, ball_move

    paddle = paddle.move(paddle_move)
    if paddle.x <= 0:
        paddle.x = 0
    elif paddle.x >= 800 - paddle.width:
        paddle.x = 800 - paddle.width

    ball = ball.move(ball_move)

    # hit left
    if ball.x <= 0:
        ball_move = [[-1, 1][x] * ball_move[x] for x in range(2)]
    # hit top
    if ball.y <= 0:
        ball_move = [[1, -1][x] * ball_move[x] for x in range(2)]
    # hit right
    if ball.x >= 800 - ball.width:
        ball_move = [[-1, 1][x] * ball_move[x] for x in range(2)]
    # hit bottom
    if ball.center[1] >= 600:
        print("You lose")
        pygame.quit()
        sys.exit()

    # hit paddle
    if ball.colliderect(paddle):
        ball_move = [[1.2, -1.2][x] * ball_move[x] for x in range(2)]

    pygame.draw.circle(screen, COLOR_WHITE, ball.center, int(ball.height / 2))
    pygame.draw.rect(screen, COLOR_WHITE, paddle)

    paddle_move = [maxmove(x * 1.5, 15) for x in paddle_move]

    #print("Ball ", ball_move)


def main():
    ''' Run program '''
    print('Starting Game')
    pygame.init()
    pygame.display.set_caption("Hi there")
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            process_event(event)
        screen.fill(COLOR_BLACK)

        game_tick()
        pygame.display.flip()
        clock.tick(36)


if __name__ == '__main__':
    main()
