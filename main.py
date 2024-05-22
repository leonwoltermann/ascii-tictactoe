from os import system

def createBoard(grid_number):
    return [[0 for x in range(grid_number)] for x in range(grid_number)]

def update(grid: list, player: int, cords: tuple):
    grid[cords[0]][cords[1]] = player
    return grid

def testInput(grid: list, cords: tuple):
    if cords[0] > len(grid) or cords[1] > len(grid):
        return False
    elif cords[0] > 2 and cords[1] > 2:
        return False
    elif grid[cords[0]][cords[1]] != 0:
        return False
    else:
        return True

def testWin(grid: list):
    #rows
    for i in grid:
        if i[0] == 0:
            continue
        elif i[0] == i[1] and i[1] == i[2]:
            return i[0]
    #columns
    for i in range(3):
        if grid[0][i] == 0:
            continue
        elif grid[0][i] == grid[1][i] and grid[1][i] == grid[2][i]:
            return grid[0][i]

    #diagonal
    if grid[0][0] != 0 and grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
        return grid[0][0]
    elif grid[0][2] != 0 and grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
        return grid[0][2]

    return False

def toString(grid: list):
    transl = {0:" ", 1:"X", 2:"O"}
    output_string = ""
    for i in grid:
        temp = f"{transl[i[0]]}|{transl[i[1]]}|{transl[i[2]]}\n"
        output_string += temp 
    return output_string




board = createBoard(3)
run = True
player = 1

while run:

    if player == 1:
        symbol = "X"
    else:
        symbol = "O"


    system("clear")

    print(f"Player {player}'s Turn ({symbol})\n")
    print(toString(board))

    print("\nEnter the coordinates of the place you want to place your symbol")
    line = int(input("Line: "))
    column = int(input("Column: "))
    cords = (line, column)

    check = testInput(board, cords)
    while check == False:
        system("clear")
        print(f"Invalid Input – Player {player}'s Turn ({symbol})\n")
        print(toString(board))
        print("\nEnter the coordinates of the place you want to place your symbol")
        line = int(input("Line: "))
        column = int(input("Column: "))
        cords = (line, column)
        check = testInput(board, cords)

    board = update(board, player, cords)
    system("clear")

    if testWin(board) == 1 or testWin(board) == 2:
        print(f"Game Over – Player {testWin(board)} Wins\n")
        print(toString(board))
        run = False

    
    if player == 1:
        player += 1
    else:
        player -= 1