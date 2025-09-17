import random

ref = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ib = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def printboard():
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

def chkWin():
    win_comb = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    p1_pos = []
    p2_pos = []

    for i in range(3):
        for j in range(3):
            pos_num = i * 3 + j + 1
            if ib[i][j] == "*":
                p1_pos.append(pos_num)
            elif ib[i][j] == "o":
                p2_pos.append(pos_num)

    for combo in win_comb:
        if all(pos in p1_pos for pos in combo):
            return 1
        if all(pos in p2_pos for pos in combo):
            return 2
    
    if not any(" " in row for row in ib):
        return 0
    
    return -1

def play_game():
    player = 1
    
    print("This is the board positions")

    while True:
        printboard()

        game_status = chkWin()
        if game_status != -1:
            printboard()
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
            available_positions = [ref[i][j] for i in range(3) for j in range(3) if ib[i][j] == " "]
            
            if available_positions:
                x = random.choice(available_positions)
                for i, row in enumerate(ref):
                    if x in row:
                        j = row.index(x)
                        ib[i][j] = "o"
                        player = 1
                        break
            
play_game()