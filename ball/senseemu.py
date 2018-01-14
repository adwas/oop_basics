#!/usr/bin/env python3

from typing import List
import pygame
from scene import Scene, Stage


class SenseHatScene(Scene):
    ''' Scene which emulates SenseHAt LED matrix '''
    LED_GRID_COLOR: List[int] = [255, 255, 255]
    LED_DEFAULT_COLOR: List[int] = [220, 220, 220]  # light gray

    def __init__(self, stage: Stage):
        super().__init__(stage, self)
        self.led_centers: List[int] = []

        self.led_matrix: List[int] = [self.LED_DEFAULT_COLOR] * 64

    def _draw_grid(self):
        scr_width: int = self.stage.width
        scr_height: int = self.stage.height
        cell_width: int = scr_width / 8

        for idx in range(8):
            pos: int = cell_width * idx
            pygame.draw.line(self.stage.surface, self.LED_GRID_COLOR,
                             (pos, 0), (pos, scr_height))

        cell_hight: int = scr_height / 8
        for idx in range(8):
            pos = cell_hight * idx
            pygame.draw.line(self.stage.surface, self.LED_GRID_COLOR,
                             (0, pos), (scr_width, pos))

    def _draw_led_matrix(self):
        scr_width: int = self.stage.width
        cell_size: int = int(scr_width / 8)
        cell_offset: int = int(cell_size / 2)
        led_radius: int = cell_offset - 5
        crd_x: int = 0
        crd_y: int = 1

        for idx in range(len(self.led_matrix)):
            crd_y = int(idx / 8)
            crd_x = idx % 8
            color = self.led_matrix[idx]
            p_x = crd_x * cell_size + cell_offset
            p_y = crd_y * cell_size + cell_offset
            pygame.draw.circle(self.stage.surface, color,
                               (p_x, p_y), led_radius)

    def render(self):
        self._draw_grid()
        self._draw_led_matrix()

    # Implement Sense Hat methods starts here

    def set_pixels(self, pixel_list):
        """
        Accepts a list containing 64 smaller lists of [R,G,B] pixels and
        updates the LED matrix. R,G,B elements must intergers between 0
        and 255
        """

        if len(pixel_list) != 64:
            raise ValueError('Pixel lists must have 64 elements')

        for index, pix in enumerate(pixel_list):
            if len(pix) != 3:
                raise ValueError(
                    'Pixel at index %d is invalid. Pixels must contain 3 elements: Red, Green and Blue' % index)

            for element in pix:
                if element > 255 or element < 0:
                    raise ValueError(
                        'Pixel at index %d is invalid. Pixel elements must be between 0 and 255' % index)

        self.led_matrix = pixel_list

    def clear(self, *args):
        """
        Clears the LED matrix with a single colour, default is black / off
        e.g. ap.clear()
        or
        ap.clear(r, g, b)
        or
        colour = (r, g, b)
        ap.clear(colour)
        """
        if len(args) == 0:
            colour = self.LED_DEFAULT_COLOR
        elif len(args) == 1:
            colour = args[0]
        elif len(args) == 3:
            colour = args
        else:
            raise ValueError(
                'Pixel arguments must be given as (r, g, b) or r, g, b')

        self.led_matrix = [colour] * 64

    def set_pixel(self, x, y, *args):
        """
        Updates the single [R,G,B] pixel specified by x and y on the LED matrix
        Top left = 0,0 Bottom right = 7,7
        e.g. ap.set_pixel(x, y, r, g, b)
        or
        pixel = (r, g, b)
        ap.set_pixel(x, y, pixel)
        """

        pixel_error = 'Pixel arguments must be given as (r, g, b) or r, g, b'

        if len(args) == 1:
            pixel = args[0]
            if len(pixel) != 3:
                raise ValueError(pixel_error)
        elif len(args) == 3:
            pixel = args
        else:
            raise ValueError(pixel_error)

        if x > 7 or x < 0:
            raise ValueError('X position must be between 0 and 7')

        if y > 7 or y < 0:
            raise ValueError('Y position must be between 0 and 7')

        for element in pixel:
            if element > 255 or element < 0:
                raise ValueError('Pixel elements must be between 0 and 255')

        self.led_matrix[x * 8 + y] = pixel


class SenseHatEmulator:
    ''' Emulator of SenseHat Simple usage:
        emulator = SenseHatEmulator()
        emulator.start()

        # Below line replaces two of 
        # from sense_hat import SenseHat
        # sense = SenseHat()
        sense = emulator.sense_object()
    '''

    def __init__(self):
        from disp_stage import DisplayStage
        self.stage: Stage = DisplayStage(800, 800)
        self.sense: Scene = SenseHatScene(self.stage)

    def sense_object(self) -> Scene:
        ''' Returns Scene which emulates SenseHat. '''
        return self.sense

    def start(self):
        ''' Starts emulator in separate thread. '''
        from game import Game
        game = Game('SenseHat LED Matrix emulator', self.sense, self.stage)
        # run game loop in separate thread game.run()
        import threading
        game_thread = threading.Thread(target=game.run)
        game_thread.start()


def main():
    ''' Simple demonstratin '''
    emulator = SenseHatEmulator()
    emulator.start()

    # from sense_hat import SenseHat
    # sense = SenseHat()
    sense = emulator.sense_object()

    X = [255, 0, 0]  # Red
    O = [255, 255, 255]  # White
    Y = [255, 255, 0]  # yellow

    question_mark = [
        O, O, O, X, X, O, O, O,
        O, O, X, O, O, X, O, O,
        O, O, O, O, O, X, O, O,
        O, O, O, O, X, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, X, O, O, O, O
    ]
    sense.set_pixels(question_mark)

    sense.set_pixel(3, 0, Y)
    sense.set_pixel(0, 3, Y)
    sense.set_pixel(0, 0, Y)
    sense.set_pixel(7, 7, Y)


if __name__ == '__main__':
    main()
