import pygame
import sys
import time

import tictactoe as ttt

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (30, 41, 59)

# Fonts
mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)


class Button:
    def __init__(self, x, y, width, height, text, font, default_color, hover_color, text_default, text_hover):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.default_color = default_color
        self.hover_color = hover_color
        self.text_default = text_default
        self.text_hover = text_hover

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        hovering = self.rect.collidepoint(mouse)
        color = self.hover_color if hovering else self.default_color
        text_color = self.text_hover if hovering else self.text_default
        pygame.draw.rect(screen, color, self.rect)
        label = self.font.render(self.text, True, text_color)
        label_rect = label.get_rect(center=self.rect.center)
        screen.blit(label, label_rect)
        return hovering


class TicTacToeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.user = None
        self.board = ttt.initial_state()
        self.ai_turn = False
        self.running = True

    def reset(self):
        self.user = None
        self.board = ttt.initial_state()
        self.ai_turn = False

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(BLACK)

            if self.user is None:
                self.draw_start_menu()
            else:
                self.draw_game()

            pygame.display.flip()
        pygame.quit()
        sys.exit()

    def draw_start_menu(self):
        title = largeFont.render("Play Tic-Tac-Toe", True, WHITE)
        title_rect = title.get_rect(center=(WIDTH / 2, 50))
        self.screen.blit(title, title_rect)

        play_x_btn = Button(WIDTH / 8, HEIGHT / 2, WIDTH / 4, 50, "Play as X", mediumFont, WHITE, DARK_BLUE, BLACK, WHITE)
        play_o_btn = Button(5 * WIDTH / 8, HEIGHT / 2, WIDTH / 4, 50, "Play as O", mediumFont, WHITE, DARK_BLUE, BLACK, WHITE)

        click, _, _ = pygame.mouse.get_pressed()

        if play_x_btn.draw(self.screen) and click:
            time.sleep(0.2)
            self.user = ttt.X
        elif play_o_btn.draw(self.screen) and click:
            time.sleep(0.2)
            self.user = ttt.O

    def draw_game(self):
        tile_size = 80
        origin = (WIDTH / 2 - (1.5 * tile_size), HEIGHT / 2 - (1.5 * tile_size))
        tiles = []

        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(origin[0] + j * tile_size, origin[1] + i * tile_size, tile_size, tile_size)
                pygame.draw.rect(self.screen, WHITE, rect, 3)
                if self.board[i][j] != ttt.EMPTY:
                    label = moveFont.render(self.board[i][j], True, WHITE)
                    label_rect = label.get_rect(center=rect.center)
                    self.screen.blit(label, label_rect)
                row.append(rect)
            tiles.append(row)

        game_over = ttt.terminal(self.board)
        turn_player = ttt.player(self.board)

        if game_over:
            win = ttt.winner(self.board)
            title_text = f"Game Over: {win} wins." if win else "Game Over: Tie."
        elif self.user == turn_player:
            title_text = f"Play as {self.user}"
        else:
            title_text = "Computer thinking..."

        title = largeFont.render(title_text, True, WHITE)
        title_rect = title.get_rect(center=(WIDTH / 2, 30))
        self.screen.blit(title, title_rect)

        if self.user != turn_player and not game_over:
            if self.ai_turn:
                time.sleep(0.5)
                move = ttt.minimax(self.board)
                self.board = ttt.result(self.board, move)
                self.ai_turn = False
            else:
                self.ai_turn = True

        click, _, _ = pygame.mouse.get_pressed()
        if click and self.user == turn_player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse):
                        self.board = ttt.result(self.board, (i, j))

        if game_over:
            again_btn = Button(WIDTH / 3, HEIGHT - 65, WIDTH / 3, 50, "Play Again", mediumFont,
                               WHITE, DARK_BLUE, BLACK, WHITE)
            if again_btn.draw(self.screen) and click:
                time.sleep(0.2)
                self.reset()


if __name__ == "__main__":
    TicTacToeGame().run()
