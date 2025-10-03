import pygame
import math
import json

from Classes.snake import Snake
from Classes.apple import Apple
from Classes.text import Text

pygame.init()
pygame.font.init()
pygame.mixer.init()

data = json.load(open("data.json"))
rows = data["rows"]
cols = data["cols"]

WIDTH, HEIGHT = 30 * rows, 30 * cols
FPS = 10

window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Snake 🐍")

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

snake = Snake(window, 30)
apple = Apple(window, 30, red)

lose_text = Text(window, "You lost! :(", 75, red, 255)
win_text = Text(window, "You won! :D", 75, green, 255)

lose_sound = pygame.mixer.Sound("Assets/lose.wav")
powerup_sound = pygame.mixer.Sound("Assets/powerup.wav")
pygame.mixer.music.load("Assets/bg_music.mp3")
pygame.mixer.music.set_volume(0.3)


bg_color = (1, 5, 36)


def game():
    clock = pygame.time.Clock()
    run = True

    hover_value = 0.0
    pygame.mixer.music.play(-1)

    score = len(snake.snake_positions)
    score_text = Text(window, str(score), 75, (255, 0, 0), 128)
    lose_text_under = Text(window, "Your score is " + str(score), 75, white, 255)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        hover_value += 0.1
        window.fill((bg_color))

        score_text.update_text(str(score))
        lose_text_under.update_text("Your score is " + str(score))

        # Handling apple spawning
        if apple.position in snake.snake_positions:
            snake.increase = True
            apple.position = apple.generate_new_position()
            score += 1

        else:
            snake.increase = False

        apple.draw()

        if snake.increase:
            snake.increase = True
            pygame.mixer.Sound.play(powerup_sound)

        snake.move()
        snake.draw()
        score_text.draw(
            (
                WIDTH // 2 - score_text.text_surface.get_width() // 2,
                (HEIGHT // 2 - score_text.text_surface.get_height() // 2)
                - math.sin(hover_value * 2) * 20,
            )
        )

        if (
            snake.snake_positions[-1] in snake.snake_positions[:-1]
            or snake.snake_positions[-1][0] < 0
            or snake.snake_positions[-1][0] > rows - 1
            or snake.snake_positions[-1][1] < 0
            or snake.snake_positions[-1][1] > cols - 1
        ):
            run = False
            pygame.mixer.Sound.play(lose_sound)
            pygame.mixer.music.stop()
            window.fill((bg_color))
            lose_text.draw(
                (
                    WIDTH // 2 - lose_text.text_surface.get_width() // 2,
                    50,
                )
            )
            lose_text_under.draw(
                (
                    WIDTH // 2 - lose_text_under.text_surface.get_width() // 2,
                    125,
                )
            )
        if len(snake.snake_positions) == rows * cols:
            run = False
            window.fill((bg_color))

            win_text.draw(
                (
                    WIDTH // 2 - win_text.text_surface.get_width() // 2,
                    50,
                )
            )

        pygame.display.flip()
        score_text.text_surface.fill((0, 0, 0, 0))


def main(window=window):
    while True:
        game()
        snake.reset()
        pygame.time.delay(1500)
        pygame.display.flip()


if __name__ == "__main__":
    main(window)
