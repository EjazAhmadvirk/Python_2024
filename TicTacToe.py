# Tic Tac Toe Game in Python

# Function to print the board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

# Function to check if a player wins
def check_winner(board, player):
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to check draw
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Main Game Loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("🎮 Welcome to Tic Tac Toe!")
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")
            continue

        if row not in [0,1,2] or col not in [0,1,2]:
            print("❌ Position out of range! Use 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("❌ Cell already taken! Choose another.")
            continue

        # Place move
        board[row][col] = current_player

        # Check winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            break

        # Check draw
        if is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        # Switch turn
        current_player = "O" if current_player == "X" else "X"

# Run game
play_game()
