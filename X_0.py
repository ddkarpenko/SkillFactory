import random
field = ["-","-","-",
         "-","-","-",
         "-","-","-"]
End = [[0,1,2],
       [3,4,5],
       [6,7,8],
       [0,3,6],
       [1,4,7],
       [2,5,8],
       [0,4,8],
       [2,4,6]]

Victrory = False
def print_field(symbol,move):
    if field[move-1] != "X" and field[move-1] != "O":
        field[move-1] = symbol
    else:
        print("Field occupied!")
        return False
    print("  1 2 3")
    print(f"1 {field[0]} {field[1]} {field[2]}")
    print(f"3 {field[3]} {field[4]} {field[5]}")
    print(f"4 {field[6]} {field[7]} {field[8]}\n")
    return True
Play_Type = int(input("Play with comp (0)/ Play with man (1)"))
def chek_res():
    count = 0
    for i in End:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            print ("Player one Wins!")
            return True
        elif field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            print ("Player two Wins!")
            return True
    for i in field:
        if i != "-":
            count+=1
            if count == 9:
                print("DRAW! No one wins!")
                return True
    return False
if(Play_Type == 0):
    while(not Victrory):
        move = int(input("Player one, make you move (1-9): "))
        symbol = "X"
        if move not in range(1,10):
            move = int(input("Wrong move, choose field from 1 to 9: "))
        else:
            print_field(symbol, move)
            if chek_res() == True:
                break

        move = random.randint(1,9)
        symbol = "O"
        while (print_field(symbol, move) != True):
            move = random.randint(1, 9)
        if chek_res() == True:
            break
else:
    while(not Victrory):
        move = int(input("Player one, make you move (1-9): "))
        symbol = "X"
        if move not in range(1,10):
            move = int(input("Wrong move, choose field from 1 to 9: "))
        else:
            print_field(symbol, move)
            if chek_res() == True:
                break
        move = int(input("Player two, make you move (1-9): "))
        symbol = "O"
        if move not in range(1,10):
            move = int(input("Wrong move, choose field from 1 to 9: "))
        else:
            print_field(symbol, move)
            if chek_res() == True:
                break