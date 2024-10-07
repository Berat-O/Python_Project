import pygame
import sys
import time

from tictactoe import TicTacToe

pygame.init()
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

user = None
game = TicTacToe()  # Instantiate the TicTacToe game
ai_turn = False

# Functions to render static UI components
def draw_text(text, font, color, center):
    rendered_text = font.render(text, True, color)
    rect = rendered_text.get_rect()
    rect.center = center
    screen.blit(rendered_text, rect)

def draw_buttons():
    playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
    playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
    pygame.draw.rect(screen, white, playXButton)
    pygame.draw.rect(screen, white, playOButton)
    draw_text("Play as X", mediumFont, black, playXButton.center)
    draw_text("Play as O", mediumFont, black, playOButton.center)
    return playXButton, playOButton

def draw_board(board):
    tile_size = 80
    tile_origin = (width / 2 - (1.5 * tile_size), height / 2 - (1.5 * tile_size))
    tiles = []
    for i in range(3):
        row = []
        for j in range(3):
            rect = pygame.Rect(
                tile_origin[0] + j * tile_size,
                tile_origin[1] + i * tile_size,
                tile_size, tile_size
            )
            pygame.draw.rect(screen, white, rect, 3)
            if board[i][j] != TicTacToe.EMPTY:
                draw_text(board[i][j], moveFont, white, rect.center)
            row.append(rect)
        tiles.append(row)
    return tiles

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    # Let user choose a player.
    if user is None:
        draw_text("Play Tic-Tac-Toe", largeFont, white, (width / 2, 50))
        playXButton, playOButton = draw_buttons()

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)
                user = TicTacToe.X
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                user = TicTacToe.O

    else:
        # Draw game board
        tiles = draw_board(game.board)

        game_over = game.is_terminal()
        player = game.current_player()

        # Show title
        if game_over:
            winner = game.check_winner()
            if winner is None:
                title = "Game Over: Tie."
            else:
                title = f"Game Over: {winner} wins."
        elif user == player:
            title = f"Play as {user}"
        else:
            title = "Computer thinking..."
        
        draw_text(title, largeFont, white, (width / 2, 30))

        # AI's turn to move
        if user != player and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = game.minimax()
                game.board = game.apply_action(move)
                ai_turn = False
            else:
                ai_turn = True

        # Check for a user move
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if game.board[i][j] == TicTacToe.EMPTY and tiles[i][j].collidepoint(mouse):
                        game.board = game.apply_action((i, j))

        # If game is over, render the Play Again button
        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            pygame.draw.rect(screen, white, againButton)
            draw_text("Play Again", mediumFont, black, againButton.center)

            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    game = TicTacToe()  # Restart game by reinitializing the class instance
                    ai_turn = False

    pygame.display.flip()
