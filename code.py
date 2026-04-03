Grid = [["." for _ in range(3)] for _ in range(3)]

def Display():
    for row in range(3):
        for column in range(3):
            print(Grid[row][column], end = " ")
        print()    
def Check():
    Invalid = False
    if Grid[row][column] != ".":
        Invalid = True
    return Invalid
    
symbol = "x"
Invalid = False

while 1 == 1:
    while True:
        row = int(input("row"))
        column = int(input("column"))
        if Check() == False:
            Grid[row][column] = symbol
            break
        print("please enter valid values")
    Display()
    if symbol == "x":
        symbol = "o"  #turn switcher
    else:
        symbol = "x"
    if input() == "yes":
        break #exit loop
