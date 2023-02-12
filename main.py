import pygame
import random
from math import ceil


class Visualizer:
    pygame.init()

    def __init__(self, size=720):
        self.sorting = False
        self.ascending = True
        self.bars = 64
        self.tick = 64
        self.width = size // 2 * 3
        self.height = size
        self.top_pad = self.height / 4
        self.font_size = self.height // 24
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.setAlgo()
        self.genList()
        self.update()
        self.gen = self.algo()
