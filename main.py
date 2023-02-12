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

    # Visualization
    def update(self):
        self.window.fill((0, 0, 0))
        play_pause = "Pause" if self.sorting else "Play"
        titles1 = [
            f"ARROWS - {self.bars} Bars  {self.tick} Tick",
            f"SPACE - {play_pause}",
            "R - Reset",
        ]
        for i, title in enumerate(titles1):
            self.window.blit(
                pygame.font.Font(None, self.font_size).render(
                    title,
                    1,
                    (255, 255, 255),
                ),
                (self.width // 3, 10 + self.font_size * i),
            )

        titles2 = [
            "A - Ascending",
            "D - Descending",
        ]
        for i, title in enumerate(titles2):
            color = 255, 255, 255
            if title[0] == "A" and self.ascending:
                color = 0, 255, 255
            if title[0] == "D" and not self.ascending:
                color = 0, 255, 255

            self.window.blit(
                pygame.font.Font(None, self.font_size).render(
                    title,
                    1,
                    color,
                ),
                (self.width // 3 * 2, 10 + self.font_size * i),
            )

        algorithms = [
            f"{name[0]} - {name}" for name in (x for x, _ in self.algorithms.values())
        ]
        for i, algo in enumerate(algorithms):
            color = 255, 255, 255
            if algo[0] == self.algo_name[0]:
                color = 255, 0, 255

            self.window.blit(
                pygame.font.Font(None, self.font_size).render(
                    algo,
                    1,
                    color,
                ),
                (10, 10 + self.font_size * i),
            )

        self.drawList()

    def drawList(self, clear_bg=False):
        if clear_bg:
            pygame.draw.rect(
                self.window,
                (0, 0, 0),
                (
                    0,
                    self.top_pad,
                    self.width,
                    self.height,
                ),
            )
        for i, val in enumerate(self.list):
            x = i * self.bar_spacing
            y = self.height - val * self.bar_height
            color = (
                val * 2.55,
                (100 - val) * 2.55,
                255,
            )
            pygame.draw.rect(
                self.window,
                color,
                (x, y, self.bar_width, self.height),
            )
        pygame.display.update()
