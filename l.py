board = [["*" for i in range(3) ]for i in range(3)]

def printBoard(board):
    for indexy, i in enumerate(board):
        for indexx, j in enumerate(i):
            print("", (indexx+1)+(indexy)*3 if j == "*" else j, end=' ')

            if indexx < 2:
                print("|", end="")

        print()        
        if indexy < 2:
            print("-"*11)

def playerInput(turn):
    val = int(input(f"as {'X' if turn % 2 == 1 else 'O'}, input your number: ")) - 1
    y = val//3
    x = val-y*3
    return (x, y)

def findWinner(board):
    for c in ['X', 'O']:
        for  i in board:
            if i == [c,c,c]:
                return c
            
        for x in range(3):
            if board[0][x] == board[1][x] == board[2][x] == c:
                return c
        
        if board[0][0] == board[1][1] == board[2][2] == c:
            return c

        if board[2][0] == board[1][1] == board[0][2] == c:
            return c
    return 0
                


def game():
    turn=0
    winner=0
    while turn<9 and winner==0:
        printBoard(board)

        x, y = playerInput(turn)
        if turn%2 == 0:
            board[y][x] = 'O'
        else:
            board[y][x] = 'X'
        turn += 1
        winner = findWinner(board)
        
    printBoard(board)
    print("winner is: ", winner)
game()
