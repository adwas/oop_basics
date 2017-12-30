# pylint: disable=C0111

import pygame

from scene import Scene

COLOR_WHITE = (255, 255, 255)


class ColisionItem:
    def __init__(self, rect=pygame.Rect(0, 0, 0, 0)):
        self.wrapping_rect = rect


class Ball(ColisionItem):

    def __init__(self, center_x, center_y):
                        #(left, top, width, height)
        super().__init__(pygame.Rect(0, 0, 40, 40))
        self.wrapping_rect.center = (center_x, center_y)
        self.ball_move = [-1, -3]

    @property
    def center(self):
        # center is delegated to wrapping_rect.center
        return self.wrapping_rect.center

    @center.setter
    def center(self, value):
        self.wrapping_rect.center = value

    def y_axis_reflection(self):
        self._axis_reflection(0)

    def x_axis_reflection(self):
        self._axis_reflection(1)

    def _axis_reflection(self, idx):
        self.ball_move[idx] = self.ball_move[idx] * -1

    def draw(self, stage):
        pygame.draw.circle(stage.surface, COLOR_WHITE, self.center, int(
            self.wrapping_rect.height / 2))

    def move(self):
        self.wrapping_rect = self.wrapping_rect.move(self.ball_move)


class Wall(ColisionItem):

    def __init__(self, left, top, width, height, reflection):
        super().__init__(pygame.Rect(left, top, width, height))
        self.reflection = reflection


class Paddle(ColisionItem):

    def __init__(self, stage, reflection):
        super().__init__(pygame.Rect(stage.width / 2, stage.height - 20, 60, 20))
        self.reflection = reflection
        self.paddle_move = 0
        self.stage = stage

    def draw(self, stage):
        pygame.draw.rect(stage.surface, COLOR_WHITE, self.wrapping_rect)

    def move(self):
        self.wrapping_rect = self.wrapping_rect.move([self.paddle_move, 0])
        if self.wrapping_rect.x <= 0:
            self.wrapping_rect.x = 0
        elif self.wrapping_rect.x >= self.stage.width - self.wrapping_rect.width:
            self.wrapping_rect.x = self.stage.width - self.wrapping_rect.width
        self.paddle_move = Paddle._maxmove(self.paddle_move * 1.5, 15)
    def turn_left(self):
        self.paddle_move = -1

    def turn_right(self):
        self.paddle_move = 1

    def stop_move(self):
        self.paddle_move = 0

    @staticmethod
    def _maxmove(value, maxvalue):
        if value < -1 * maxvalue:
            return -1 * maxvalue
        if value > maxvalue:
            return maxvalue
        return value


class BouncedBallScene(Scene):

    def __init__(self, stage):
        super().__init__(stage, self)
        # ball position to center of the screen
        self.ball = Ball(center_x=stage.width / 2, center_y=stage.height / 2)

        self.left_wall = Wall(left=0, top=0, width=1,
                              height=stage.height, reflection=self.ball.y_axis_reflection)
        self.top_wall = Wall(left=0, top=0, width=stage.width,
                             height=1, reflection=self.ball.x_axis_reflection)
        self.right_wall = Wall(left=stage.width, top=0,
                               width=1, height=stage.height, reflection=self.ball.y_axis_reflection)
        self.bottom_wall = Wall(left=0, top=stage.height, width=stage.width,
                                height=1, reflection=self.game_over)

        self.paddle = Paddle(stage, reflection=self.ball.x_axis_reflection)
        self.collision_items = [self.paddle, self.bottom_wall,
                                self.left_wall, self.top_wall, self.right_wall]

    def update(self, time_step):
        self.ball.move()
        self.paddle.move()

        # Handle colisions with ball
        idx = self.ball.wrapping_rect.collidelist(
            [x.wrapping_rect for x in self.collision_items])
        if idx != -1:
            self.collision_items[idx].reflection()

    def game_over(self):
        self.next_scene = None

    def render(self):
        self.ball.draw(self.stage)
        self.paddle.draw(self.stage)

    def process(self, event):
        from pygame.constants import KEYDOWN, K_ESCAPE, K_LEFT, K_RIGHT, KEYUP
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.game_over()
            if event.key == K_LEFT:
                self.paddle.turn_left()
            if event.key == K_RIGHT:
                self.paddle.turn_right()
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                self.paddle.stop_move()
