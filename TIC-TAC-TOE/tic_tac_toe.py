import random
import math

# These variables are now handled locally within play_game()
# ref = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ib = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def printboard(ref, ib):
    for i in range(3):
        for j in range(3):
            if ib[i][j] != " ":
                cell = f" {ib[i][j]} "
            else:
                cell = f" {ref[i][j]} "
            
            if j == 2:
                print(cell)
            else:
                print(cell, end="|")
        
        if i < 2:
            print("---+---+---")

def chkWin(ib):
    # Check rows, columns, and diagonals for a win
    win_comb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    flat_ib = [item for sublist in ib for item in sublist]

    for combo in win_comb:
        if flat_ib[combo[0]] == flat_ib[combo[1]] == flat_ib[combo[2]] != " ":
            if flat_ib[combo[0]] == "*":
                return 1 # Human wins
            else:
                return 2 # Computer wins
    
    if " " not in flat_ib:
        return 0 # Tie
    
    return -1 # Game not over

def minimax(board, is_maximizing):
    score = chkWin(board)

    if score == 1:
        return -10
    elif score == 2:
        return 10
    elif score == 0:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "o"
                    current_score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(best_score, current_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "*"
                    current_score = minimax(board, True)
                    board[i][j] = " "
                    best_score = min(best_score, current_score)
        return best_score

def findBestMove(ib):
    best_score = -math.inf
    best_move = None
    
    for i in range(3):
        for j in range(3):
            if ib[i][j] == " ":
                ib[i][j] = "o"
                score = minimax(ib, False)
                ib[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def play_game():
    ref = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ib = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = 1
    
    print("This is the board positions")

    while True:
        printboard(ref, ib)

        game_status = chkWin(ib)
        if game_status != -1:
            printboard(ref, ib)
            if game_status == 1:
                print("u won!")
            elif game_status == 2:
                print("computer won!")
            else:
                print("It's a tie!")
            break

        if player == 1:
            try:
                x = int(input("Enter your pos: "))
                # New validation to check if the number is in the valid range
                if x < 1 or x > 9:
                    print("Invalid position. Please enter a number between 1 and 9.")
                    continue

                found = False
                for i, row in enumerate(ref):
                    if x in row:
                        j = row.index(x)
                        if ib[i][j] == " ":
                            ib[i][j] = "*"
                            found = True
                            player = 2
                            break
                        else:
                            print("This position is already taken.")
                            found = True
                if not found:
                    print("Invalid position entered.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
        else:
            print("Computer's turn")
            move = findBestMove(ib)
            if move:
                i, j = move
                ib[i][j] = "o"
                player = 1
            
play_game()