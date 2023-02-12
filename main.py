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

    def genList(self):
        self.list = [100 / self.bars * (i + 1) for i in range(self.bars)]
        random.shuffle(self.list)
        self.bar_spacing = self.width / self.bars
        self.bar_width = ceil(self.bar_spacing)
        self.bar_height = (self.height - self.top_pad) // 100

    def changeTick(self, up):
        if up and self.tick < 256:
            self.tick *= 2
        elif not up and self.tick > 4:
            self.tick //= 2

    def changeBars(self, up):
        if up and self.bars < 256:
            self.bars *= 2
        elif not up and self.bars > 4:
            self.bars //= 2
        self.genList()

    def setAlgo(self, key=False):
        self.algorithms = {
            pygame.K_b: ("Bubble Sort", self.bubbleSort),
            pygame.K_i: ("Insertion Sort", self.insertionSort),
            pygame.K_m: ("Merge Sort", self.mergeSort),
            pygame.K_q: ("Quick Sort", self.quickSort),
            pygame.K_s: ("Selection Sort", self.selectionSort),
        }
        if not key:
            key = list(self.algorithms.keys())[0]
        self.algo_name = self.algorithms[key][0]
        self.algo = self.algorithms[key][1]
