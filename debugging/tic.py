#!/usr/bin/python3

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.")
            continue

        # Check valid range
        if row not in [0,1,2] or col not in [0,1,2]:
            print("Invalid position. Choose row/column 0, 1, or 2.")
            continue

        # Check if taken
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place marker
        board[row][col] = player

        # Check winner
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        # Check draw
        full = all(board[r][c] != " " for r in range(3) for c in range(3))
        if full:
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


tic_tac_toe()
