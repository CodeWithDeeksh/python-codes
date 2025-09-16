ref = ib = [[1,2,3],[4,5,6],[7,8,9]]  # initial board input
player = 1  # first player chance

def printboard(lst):
    for i in range(len(lst)):             # i = row index
        for j in range(len(lst[i])):      # j = col index
            if ib[i][j] in [" * ", " o "]:
                cell = ib[i][j]           # already played
            else:
                cell = f" {lst[i][j]} "   # position number, padded for uniformity

            if j == 2:                    # last element in row
                print(cell)
            else:
                print(cell, end="|")
        
        if i < 2:                         # divider after row 0 and 1
            print("---+---+---")

printboard(ib)
