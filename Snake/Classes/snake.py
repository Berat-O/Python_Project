import pygame


class Snake(pygame.sprite.Sprite):
    def __init__(self, window, size):
        self.snake_positions = [(0, 0), (1, 0), (2, 0), (3, 0)]
        self.size = size
        self.window = window
        self.moving_direction = "right"
        self.increase = False

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.moving_direction != "right":
                self.moving_direction = "left"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.moving_direction != "left":
                self.moving_direction = "right"
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.moving_direction != "down":
                self.moving_direction = "up"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.moving_direction != "up":
                self.moving_direction = "down"

        if not self.increase:
            self.snake_positions.pop(0)

        last_position = self.snake_positions[-1]

        if self.moving_direction == "left":
            self.snake_positions.append((last_position[0] - 1, last_position[1]))
        elif self.moving_direction == "right":
            self.snake_positions.append((last_position[0] + 1, last_position[1]))
        elif self.moving_direction == "up":
            self.snake_positions.append((last_position[0], last_position[1] - 1))
        elif self.moving_direction == "down":
            self.snake_positions.append((last_position[0], last_position[1] + 1))

    def draw(self):
        i = 0
        color = (0, 209, 0)
        for snake_position in self.snake_positions:
            i += 1
            if i % 2 == 0:
                color = (0, 178, 0)
            else:
                color = (0, 209, 0)
            pygame.draw.rect(
                self.window,
                color,
                pygame.Rect(
                    (snake_position[0] * self.size, snake_position[1] * self.size),
                    (self.size, self.size),
                ),
            )

    def reset(self):
        self.moving_direction = "right"
        self.snake_positions = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
        ]
        self.increase = False
