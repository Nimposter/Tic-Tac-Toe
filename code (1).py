Grid = [["." for _ in range(3)] for _ in range(3)]

def Display():
    for row in range(3):
        for column in range(3):
            print(Grid[row][column], end = " ")
        print()    
def Check(row, column):
    Invalid = False
    if Grid[row][column] != ".":
        Invalid = True
    return Invalid
def Full():
    Var1 = True
    for row in range(3):
        for column in range(3):
            if Grid[row][column] == ".":
                Var1 = False
    return Var1
def Win():
    for row in range(3):
        if Grid[row][0] == Grid[row][1] == Grid[row][2] != ".":
            return True
    for column in range(3):
        if Grid[0][column] == Grid[1][column] == Grid[2][column] != ".":
            return True
    if Grid[0][0] == Grid[1][1] == Grid[2][2] != "." or Grid[2][0] == Grid[1][1] == Grid[0][2] != ".":
        return True

    
symbol = "x"
Invalid = False

while True:
    while True:
        row = int(input("row"))
        column = int(input("column"))
        if Check(row,column) == False:
            Grid[row][column] = symbol
            break
        print("please enter valid values")
    Display()
    if Win() == True:
        print("\n" , symbol , "wins")
        break
    elif Full() == True:
        print("Draw")    
        break
    if symbol == "x":
        symbol = "o"  #turn switcher
    else:
        symbol = "x"
