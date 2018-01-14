#!/usr/bin/env python3
# pylint: disable=C0111

from scene import Stage
import pygame


class DisplayStage(Stage):

    def __init__(self, width: int=800, height: int=600):
        super().__init__(width, height, refresh_rate=60)
        self.fill_color = 0, 0, 0  # black color

    def init(self):
        self.surface = pygame.display.set_mode((self.width, self.height))

    def clear(self):
        self.surface.fill(self.fill_color)

    def swap(self):
        pygame.display.flip()
