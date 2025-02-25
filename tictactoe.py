import random

# Map of letters to board positions
LETTER_MAP = {
    "A": (0, 0), "B": (0, 1), "C": (0, 2),
    "D": (1, 0), "E": (1, 1), "F": (1, 2),
    "G": (2, 0), "H": (2, 1), "I": (2, 2)
}
LETTERS = list(LETTER_MAP.keys())

def print_board(board):
    """Prints the Tic-Tac-Toe board using basic print statements."""
    print("\nTic-Tac-Toe Board")
    print("  " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("  --+---+--")
    print("  " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("  --+---+--")
    print("  " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print("\nSelect a letter from the board to place your mark.")

def check_winner(board, player):
    """Check if the player has won."""
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_full(board):
    """Check if the board is full."""
    for row in board:
        for cell in row:
            if cell != "X" and cell != "O":
                return False
    return True

def get_valid_input(board):
    """Ensure the user enters a valid letter."""
    while True:
        move = input("\nEnter a letter (A-I) to place your move: ").strip().upper()
        if move in LETTER_MAP:
            row, col = LETTER_MAP[move]
            if board[row][col] != "X" and board[row][col] != "O":
                return row, col
            else:
                print("⚠️ That spot is already taken! Try again.")
        else:
            print("⚠️ Invalid choice! Choose a letter from A-I.")

def computer_move(board):
    """AI selects a random empty spot."""
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] != "X" and board[r][c] != "O"]
    return random.choice(empty_cells)

def play_round(player_score, computer_score, round_number):
    """Plays a single round of Tic-Tac-Toe."""
    board = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    print("\n🎮 Round", round_number, "- Player X vs. Computer O")

    turn = 0
    while True:
        print_board(board)

        if turn % 2 == 0:  # Player X (User)
            row, col = get_valid_input(board)
        else:  # Player O (Computer)
            print("\n🤖 Computer (O) is making a move...")
            row, col = computer_move(board)

        board[row][col] = "X" if turn % 2 == 0 else "O"

        if check_winner(board, "X"):
            print_board(board)
            print("🎉 Congratulations! You (Player X) win this round! 🏆")
            return player_score + 1, computer_score
        if check_winner(board, "O"):
            print_board(board)
            print("🤖 Computer (O) wins this round! Better luck next time! 🏆")
            return player_score, computer_score + 1

        if is_full(board):
            print_board(board)
            print("🤝 It's a draw! No points awarded!")
            return player_score, computer_score

        turn += 1

def tic_tac_toe():
    """Main function to run 5 rounds and track scores."""
    player_score = 0
    computer_score = 0
    total_rounds = 5

    print("\n🎮 Welcome to Tic-Tac-Toe! Best of 5 Rounds")
    print("📌 You (Player X) vs. Computer (Player O)")
    print("📌 Type a letter from A-I to place your mark.\n")

    for round_number in range(1, total_rounds + 1):
        player_score, computer_score = play_round(player_score, computer_score, round_number)

    print("\n🎉 Final Score:")
    print("🏆 Player X:", player_score, "| 🤖 Computer O:", computer_score)

    if player_score > computer_score:
        print("\n🎊 You win the series! Congratulations! 🏅")
    elif computer_score > player_score:
        print("\n🤖 The computer wins the series! Better luck next time! 🏅")
    else:
        print("\n🤝 It's a tie! Well played! 🏅")

    print("\nThanks for playing! 🎲")

if __name__ == "__main__":
    tic_tac_toe()
