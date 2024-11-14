import pygame
import sys
import time
import tictactoe as ttt

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
TILE_SIZE = 80
TILE_ORIGIN = (WIDTH / 2 - 1.5 * TILE_SIZE, HEIGHT / 2 - 1.5 * TILE_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the screen and fonts
screen = pygame.display.set_mode((WIDTH, HEIGHT))
medium_font = pygame.font.Font("OpenSans-Regular.ttf", 28)
large_font = pygame.font.Font("OpenSans-Regular.ttf", 40)
move_font = pygame.font.Font("OpenSans-Regular.ttf", 60)

# Initialize game state
user = None
board = ttt.initial_state()
ai_turn = False

def draw_title(text, y_offset=30):
    """Helper function to draw the title text on the screen."""
    title = large_font.render(text, True, WHITE)
    title_rect = title.get_rect(center=(WIDTH / 2, y_offset))
    screen.blit(title, title_rect)

def draw_buttons():
    """Draw the buttons for selecting player X or O."""
    play_x_button = pygame.Rect(WIDTH / 8, HEIGHT / 2, WIDTH / 4, 50)
    play_o_button = pygame.Rect(5 * (WIDTH / 8), HEIGHT / 2, WIDTH / 4, 50)

    play_x_text = medium_font.render("Play as X", True, BLACK)
    play_o_text = medium_font.render("Play as O", True, BLACK)

    pygame.draw.rect(screen, WHITE, play_x_button)
    pygame.draw.rect(screen, WHITE, play_o_button)
    screen.blit(play_x_text, play_x_text.get_rect(center=play_x_button.center))
    screen.blit(play_o_text, play_o_text.get_rect(center=play_o_button.center))

    return play_x_button, play_o_button

def draw_board():
    """Draw the Tic-Tac-Toe grid and the current game state."""
    tiles = []
    for i in range(3):
        row = []
        for j in range(3):
            rect = pygame.Rect(TILE_ORIGIN[0] + j * TILE_SIZE, TILE_ORIGIN[1] + i * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 3)

            if board[i][j] != ttt.EMPTY:
                move = move_font.render(board[i][j], True, WHITE)
                move_rect = move.get_rect(center=rect.center)
                screen.blit(move, move_rect)
            row.append(rect)
        tiles.append(row)
    return tiles

def handle_game_over():
    """Draw the 'Play Again' button if the game is over."""
    again_button = pygame.Rect(WIDTH / 3, HEIGHT - 65, WIDTH / 3, 50)
    again_text = medium_font.render("Play Again", True, BLACK)
    pygame.draw.rect(screen, WHITE, again_button)
    screen.blit(again_text, again_text.get_rect(center=again_button.center))

    return again_button

def main():
    global user, board, ai_turn

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Handle user selection of X or O
        if user is None:
            draw_title("Play Tic-Tac-Toe", y_offset=50)
            play_x_button, play_o_button = draw_buttons()

            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if play_x_button.collidepoint(mouse):
                    user = ttt.X
                    time.sleep(0.2)
                elif play_o_button.collidepoint(mouse):
                    user = ttt.O
                    time.sleep(0.2)

        else:
            # Draw the game board and handle game states
            tiles = draw_board()
            game_over = ttt.terminal(board)
            current_player = ttt.player(board)

            if game_over:
                winner = ttt.winner(board)
                title = f"Game Over: Tie." if winner is None else f"Game Over: {winner} wins."
            elif user == current_player:
                title = f"Play as {user}"
            else:
                title = "Computer thinking..."

            draw_title(title)

            # Handle AI turn if it is AI's turn
            if user != current_player and not game_over:
                if ai_turn:
                    time.sleep(0.5)
                    move = ttt.minimax(board)
                    board = ttt.result(board, move)
                    ai_turn = False
                else:
                    ai_turn = True

            # Handle user input for their move
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1 and user == current_player and not game_over:
                mouse = pygame.mouse.get_pos()
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse):
                            board = ttt.result(board, (i, j))

            # If the game is over, offer to play again
            if game_over:
                again_button = handle_game_over()
                click, _, _ = pygame.mouse.get_pressed()
                if click == 1:
                    mouse = pygame.mouse.get_pos()
                    if again_button.collidepoint(mouse):
                        time.sleep(0.2)
                        user = None
                        board = ttt.initial_state()
                        ai_turn = False

        pygame.display.flip()

if __name__ == "__main__":
    main()
