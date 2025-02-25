import os

def print_board(board):
    """Function to print the Tic-Tac-Toe board with better formatting."""
    os.system("cls" if os.name == "nt" else "clear")  # Clears the screen for a cleaner display
    print("\n   0   1   2 ")
    print("  -----------")
    for i, row in enumerate(board):
        print(f"{i} | {' | '.join(row)} |")
        print("  -----------")

def check_winner(board, player):
    """Check if a player has won."""
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    """Check if the board is full."""
    return all(cell != " " for row in board for cell in row)

def get_valid_input(board, player):
    """Ensures the user enters a valid move."""
    while True:
        try:
            row = int(input(f"\nPlayer {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    return row, col
                else:
                    print("⚠️ That spot is already taken! Try again.")
            else:
                print("⚠️ Invalid input! Enter numbers between 0 and 2.")
        except ValueError:
            print("⚠️ Please enter a valid number (0, 1, or 2).")

def tic_tac_toe():
    """Main function to run the game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("\n🎮 Welcome to Tic-Tac-Toe!")
    print("📌 Player X and Player O take turns placing marks on a 3x3 grid.")
    print("📌 The first player to get 3 in a row (horizontally, vertically, or diagonally) wins.")
    print("📌 Enter row and column numbers (0-2) to place your mark.\n")
    
    while True:
        print_board(board)
        row, col = get_valid_input(board, players[turn % 2])
        board[row][col] = players[turn % 2]

        if check_winner(board, players[turn % 2]):
            print_board(board)
            print(f"🎉 Player {players[turn % 2]} wins! Congratulations! 🏆")
            break

        if is_full(board):
            print_board(board)
            print("🤝 It's a draw! Good game!")
            break

        turn += 1

    print("\nThanks for playing! 🎲")

if __name__ == "__main__":
    tic_tac_toe()
