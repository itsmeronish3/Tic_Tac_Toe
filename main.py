from utils import print_board, check_winner, is_board_full
from Ai import best_move

board = [" " for _ in range(9)]

def play_game():
    while True:
        print_board(board)

        # Player move
        move = int(input("Choose position (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move! Try again.")
            continue

        board[move] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("🎉 You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        ai_move = best_move(board)
        board[ai_move] = "O"
        print("AI chose position", ai_move + 1)

        if check_winner(board, "O"):
            print_board(board)
            print("🤖 AI wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()