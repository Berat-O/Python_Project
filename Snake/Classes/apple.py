import pygame
import json
import random

data = json.load(open("data.json"))
rows = data["rows"]
cols = data["cols"]


class Apple(pygame.sprite.Sprite):
    def __init__(self, window, size, color):
        super().__init__()
        self.window = window
        self.size = size
        self.color = color
        self.position = random.randint(0, rows - 1), random.randint(0, cols - 1)

    def generate_new_position(self):
        return random.randint(0, rows - 1), random.randint(0, cols - 1)

    def draw(self):
        pygame.draw.rect(
            self.window,
            self.color,
            pygame.Rect(
                (self.position[0] * 30, self.position[1] * 30), (self.size, self.size)
            ),
            width=7,
            border_radius=3,
        )
