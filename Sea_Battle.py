import sys

from Sea_Battle_Class import Deck
from Sea_Battle_Class import Ship
import random
i = 0
point = 0
Threedeck_points = [11,21,31,41,12,22,32,42,13,23,33,43,14,24,34,44]
Twodeck_points = [11,21,31,41,12,22,32,42,13,23,33,43,14,24,34,44,15,25,35,45,51,52,53,54,55]
Onedeck_points = [11,21,31,41,12,22,32,42,13,23,33,43,14,24,34,44,15,25,35,45,51,52,53,54,55,16,26,36,46,56,66,61,62,63,64,65]

All_Done = False
var = ""
destroed_ship = []
tern_position = []
oq_position = []  # для занятых позиций
position = []
Ship_list = []
field = [
                ["0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0"]
                ]
#РАСПОЛОГАЕМ ЧУЖИЕ КОРАБЛИ
while not All_Done:
    Comp_Deck = Deck("Comp",Ship_list,oq_position,field,tern_position)
    #Трехпалуюный
    direction = random.randint(1,2)
    #вертикальное
    if direction == 1:
        position.append(random.choice(Threedeck_points))
        position.append(position[0] + 1)
        position.append(position[0] + 2)
    else:#горизонтальное
        position.append(random.choice(Threedeck_points))
        position.append(position[0] + 10)
        position.append(position[0] + 20)
    Comp_Deck.add_oq_position(position, 3, direction,0)
    Comp_Threedeck = Ship("Threedeck", position, direction)
    Comp_Deck.add_ship(Comp_Threedeck)# добавляем созданный корабль в лист
    Comp_Deck.set_oq(0)#добавляем занятые точки на поле
    Comp_Deck.set_ships(destroed_ship,0)#добавляем корабль на поле
    position.clear()
    #Двухпалубные
    i = 0

    while i < 2:
        direction = random.randint(1, 2)
        Correct = False
        # вертикальное
        if direction == 1:
            while (Correct == False):
                position.append(random.choice(Twodeck_points))
                position.append(position[0] + 1)
                if (position[0] not in Comp_Deck.oq_position and position[1] not in Comp_Deck.oq_position):
                    Comp_Deck.add_oq_position(position, 2, direction,0)
                    Correct = True
                else:
                    position.clear()
        else:
            while (Correct == False):
                position.append(random.choice(Twodeck_points))
                position.append(position[0] + 10)
                if (position[0] not in Comp_Deck.oq_position and position[1] not in Comp_Deck.oq_position):
                    Comp_Deck.add_oq_position(position, 2, direction,0)
                    Correct = True
                else:
                    position.clear()
        if i == 0:
            Comp_First_Twodeck = Ship("Twodeck", position, direction)
            Comp_Deck.add_ship(Comp_First_Twodeck)  # добавляем созданный корабль в лист
        else:
            Comp_Second_Twodeck = Ship("Twodeck", position, direction)
            Comp_Deck.add_ship(Comp_Second_Twodeck)  # добавляем созданный корабль в лист
        i+=1
        position.clear()
    Comp_Deck.set_oq(0)#добавляем занятые точки на поле
    Comp_Deck.set_ships(destroed_ship,0)#добавляем корабль на поле
    position.clear()
    #ОДНОпалубные
    i = 0
    temp_pos = []
    p = 0
    iterat = 0
    while i < 4:
        Correct = False
        # вертикальное
        while (Correct == False):
            #temp_pos.append(random.choice(Onedeck_points))
            p = random.choice(Onedeck_points)
           # print(f"Позиция {p}")
            if iterat > 500: #иногда расстановка не срабатывает, чтобы убрать зависание, добавлено условие на проверку ALL_DONE
                #print ("Error")
                del Comp_Threedeck
                del Comp_First_Twodeck
                del Comp_Second_Twodeck
                del Comp_Deck
                position.clear()
                break
                #sys.exit()
            #if (temp_pos[i] not in Comp_Deck.oq_position):
            else:
                if (p not in Comp_Deck.oq_position):
                    temp_pos.append(p)
                    Comp_Deck.add_oq_position(temp_pos, 1, 3,0)
                    position.extend(temp_pos)
                    Correct = True
                temp_pos.clear()
            iterat+=1
        if iterat > 500:
            break
        else:
            i+=1
            iterat = 0
    if len(position) == 4:
        All_Done = True
Comp_Onedeck = Ship("Onedeck", position, 3)
Comp_Deck.add_ship(Comp_Onedeck)# добавляем созданный корабль в лист
Comp_Deck.set_oq(0)#добавляем занятые точки на поле
Comp_Deck.set_ships(destroed_ship,0)#добавляем корабль на поле
position.clear()
#РАССТАНОВКА СВОИХ КОРАЮЛЕЙ
Player_Deck = Deck("Player",Ship_list,oq_position,field,tern_position)
Player_Deck.print_emty_field()
# ДОБАВЛЕНИЕ ТРЕХПАЛУБНОГО
try:
    position.append(int(input("ВВедите начальную позицию трехпалубного корабля (XY - 11 / 12 / 22...) ")))
except:
    print("Необходимо ввести числовое значение позиции!")
    position.append(int(input("ВВедите начальную позицию трехпалубного корабля (XY - 11 / 12 / 22...) ")))
if position[0] < 11 or position[0] > 66:
    print("Координата корабля задана некорректно!")
    position.clear()
    position.append(int(input(" Заново введите начальную позицию трехпалубного корабля (XY - 11 / 12 / 22...) ")))
try:
    direction = int(input("Введите положение (вертикальное - 1, горизонтальное - 2)"))
except:
    print("Направление задается числами 1 или 2!")
    direction = int(input("Введите положение (вертикальное - 1, горизонтальное - 2)"))
if direction != 1 and direction != 2:
    print("Положение корабля задано неверно!")
    direction = int(input("Введите положение (вертикальное - 1, горизонтальное - 2)"))
if (direction == 1):
    position.append(position[0] + 1)
    position.append(position[0] + 2)
    var = str(position[2])
    y = int(var[1])
    if y > 6:
        print("Корабль выходит за пределы поля!")
        position.clear()
        position.append(int(input(" Заново введите начальную позицию трехпалубного корабля (XY - 11 / 12 / 22...) ")))
        position.append(position[0] + 1)
        position.append(position[0] + 2)
elif (direction == 2):
    position.append(position[0] + 10)
    position.append(position[0] + 20)
    var = str(position[2])
    x = int(var[0])
    if x > 6:
        print("Корабль выходит за пределы поля!")
        position.clear()
        position.append(int(input(" Заново введите начальную позицию трехпалубного корабля (XY - 11 / 12 / 22...) ")))
        position.append(position[0] + 1)
        position.append(position[0] + 2)
Player_Deck.add_oq_position(position, 3, direction,0)
Threedeck = Ship("Threedeck", position, direction)
#Threedeck.set_position(position)
Player_Deck.add_ship(Threedeck)# добавляем созданный корабль в лист
Player_Deck.set_oq(0)#добавляем занятые точки на поле
Player_Deck.set_ships(destroed_ship,0)#добавляем корабль на поле
position.clear()
i = 0
# ДОБАВЛЕНИЕ ДВУХПАЛУБНОГО
while i < 2:
    try:
        position.append(int(input(f"ВВедите начальную позицию {i+1}го двухпалубного корабля (XY - 11 / 12 / 22...) ")))
    except:
        print("Необходимо ввести числовое значение позиции!")
        position.append(int(input(f"ВВедите начальную позицию {i+1}го двухпалубного корабля (XY - 11 / 12 / 22...) ")))

    if position[0] < 11 or position[0] > 66:
        print("Координата корабля задана некорректно!")
        position.clear()
        position.append(int(input(" Заново введите начальную позицию двухпалубного корабля (XY - 11 / 12 / 22...) ")))
    try:
        direction = int(input("Введите положение (вертикальное - 1, горизонтальное - 2)"))
    except:
        print("Направление задается числами 1 или 2!")
        direction = int(input("Введите положение (вертикальное - 1, горизонтальное - 2)"))
    if direction != 1 and direction != 2:
        print("Положение корабля задано неверно!")
        direction = int(input("Введите положение (вертикальное - 1, горизонтальное - 2)"))
    if (direction == 1):
        position.append(position[point] + 1)
        var = str(position[1])
        y = int(var[1])
        if y > 6:
            print("Корабль выходит за пределы поля!")
            position.clear()
            position.append(
                int(input(" Заново введите начальную позицию двухпалубного корабля (XY - 11 / 12 / 22...) ")))
            position.append(position[0] + 1)
            if position[0] in Player_Deck.oq_position or position[1] in Player_Deck.oq_position:
                position.clear()
                print("Указанные координаты заняты!")
                position.append(int(input(f"Введите координаты {i+1}го двухпалубного корабля (XY - 11 / 12 / 22...)")))
                position.append(position[0] + 1)
            Player_Deck.add_oq_position(position, 2, direction, 0)
        else:
            if position[0] in Player_Deck.oq_position or position[1] in Player_Deck.oq_position:
                position.clear()
                print("Указанные координаты заняты!")
                position.append(int(input(f"Введите координаты {i+1}го двухпалубного корабля (XY - 11 / 12 / 22...)")))
                position.append(position[0] + 1)
            Player_Deck.add_oq_position(position, 2, direction, 0)
    elif (direction == 2):
        position.append(position[point] + 10)
        var = str(position[1])
        x = int(var[0])
        if x > 6:
            print("Корабль выходит за пределы поля!")
            position.clear()
            position.append(
                int(input(" Заново введите начальную позицию двухпалубного корабля (XY - 11 / 12 / 22...) ")))
            position.append(position[0] + 1)
            if position[0] in Player_Deck.oq_position or position[1] in Player_Deck.oq_position:
                position.clear()
                print("Указанные координаты заняты!")
                position.append(int(input(f"Введите координаты {i+1}го двухпалубного корабля (XY - 11 / 12 / 22...)")))
                position.append(position[0] + 1)
            Player_Deck.add_oq_position(position, 2, direction, 0)
        else:
            if position[0] in Player_Deck.oq_position or position[1] in Player_Deck.oq_position:
                position.clear()
                print("Указанные координаты заняты!")
                position.append(int(input(f"Введите координаты {i+1}го двухпалубного корабля (XY - 11 / 12 / 22...)")))
                position.append(position[0] + 1)
            Player_Deck.add_oq_position(position, 2, direction, 0)
    #print(position)
    #point += 2
    if i == 0:
        First_Twodeck = Ship("Twodeck", position, direction)
        Player_Deck.add_ship(First_Twodeck)
    else:
        Second_Twodeck = Ship("Twodeck", position, direction)
        Player_Deck.add_ship(Second_Twodeck)
    position.clear()
    i += 1
point = 0
i = 0


Player_Deck.set_oq(0)#добавляем занятые точки на поле
Player_Deck.set_ships(destroed_ship,0)#добавляем корабль на поле
position.clear()
# ДОБАВЛЕНИЕ ОДНОПАЛУБНОГО
i = 0
while i < 4:
    try:
        position.append(
            int(input(f"ВВедите позицию {i + 1}го однопалубного корабля (XY - 11 / 12 / 22...) ")))
    except:
        print("Необходимо ввести числовое значение позиции!")
        position.append(
            int(input(f"ВВедите позицию {i + 1}го однопалубного корабля (XY - 11 / 12 / 22...) ")))
    var = str(position[i])
    y = int(var[1])
    x = int(var[0])
    if position[i] < 11 or y > 6 or x > 6:
        print("Координата корабля задана некорректно!")
        position.pop(-1)
        position.append(int(input("Заново введите позицию однопалубного корабля (XY - 11 / 12 / 22...) ")))
    if position[i] in Player_Deck.oq_position:
        position.pop(-1)#удалить последний элемент!!!!!
        print("Указанные координаты заняты!")
        position.append(int(input("Заново введите позицию однопалубного корабля (XY - 11 / 12 / 22...) ")))
    Player_Deck.add_oq_position(position, 1, 3,0)
    point += 1
    i += 1

Onedeck = Ship("Onedeck", position, 0)
Player_Deck.add_ship(Onedeck)
Player_Deck.set_oq(0)#добавляем занятые точки на поле
Player_Deck.set_ships(destroed_ship,0)#добавляем корабль на поле
position.clear()


Player_Deck.start_battle(field)
#Player_Deck.get_enemy_field(Comp_Deck.battle_field)
destroed_ship = []
destroy_pos = []
good_player_point = []
good_comp_point = []
Turn = True
Victory = False

while not Victory:
    turn = int(input(f"Выберите координату для атаки (XY - 11 / 12 / 22...) "))
    if turn in Player_Deck.turn_position:
        print(f"Вы уже атаковали координату {turn}!")
        print(Player_Deck.turn_position)
        turn = int(input(f"Выберите координату для атаки (XY - 11 / 12 / 22...) "))
    Turn = True
    while (Turn == True):
        if Player_Deck.move(turn, Comp_Deck.ship_list):
            print("Есть попадание!")
            good_player_point.append(turn)
            Player_Deck.player_show(Player_Deck.battle_field, Player_Deck.enemy_field, Player_Deck.turn_position,good_player_point)
            if(Player_Deck.destroed_ships):
                print("Корабль уничтожен!")
                direction = Player_Deck.destroed_ships[-1]
                #Player_Deck.destroed_ships.pop(-1)
                Player_Deck.set_destroed_ships()
                Player_Deck.add_oq_position(Player_Deck.destroed_ships, len(Player_Deck.destroed_ships), direction, 1)
                Player_Deck.set_oq(1)
                destroy_pos.extend(Player_Deck.destroed_ships)
                Player_Deck.set_ships(destroy_pos,1)
                destroed_ship.clear()
                if len(Comp_Deck.ship_list) == 0:
                    print("Все корабли соперника уничтожены! Вы победили!")
                    Victory = True
                    break
                else:
                    while turn in Player_Deck.turn_position:
                        turn = int(input(f"Выберите координату для атаки (XY - 11 / 12 / 22...) "))
                        if turn in Player_Deck.turn_position:
                            print(f"Вы уже атаковали координату {turn}!")
                            turn = int(input(f"Выберите координату для атаки (XY - 11 / 12 / 22...) "))
                        else:
                            break
            else:
                #Player_Deck.set_ships(destroy_pos, 1)
                while turn in Player_Deck.turn_position:
                    turn = int(input(f"Выберите координату для атаки (XY - 11 / 12 / 22...) "))
                    if turn in Player_Deck.turn_position:
                        print(f"Вы уже атаковали координату {turn}!")
                        turn = int(input(f"Выберите координату для атаки (XY - 11 / 12 / 22...) "))
                    else:
                        break
                if len(Comp_Deck.ship_list) == 0:
                    print("Все корабли соперника уничтожены! Вы победили!")
                    Victory = True
                    break

        else:
            Turn = False
            input("Ваш ход завершен, нажмите Enter!")
            #Player_Deck.set_ships(destroy_pos,0)
        Player_Deck.player_show(Player_Deck.battle_field, Player_Deck.enemy_field, Player_Deck.turn_position, good_player_point)

    if Victory == True:
        break
    Turn = True
    turn = random.choice(Onedeck_points)
    print(f"Ход оппонента: {turn}")
    while Turn:
        if Comp_Deck.move(turn, Player_Deck.ship_list):
            good_comp_point.append(turn)
            print("Попадание в ваш корабль!")
            #Comp_Deck.comp_show(Player_Deck.battle_field, turn, Player_Deck.enemy_field, 1) # Перерисовать поле игрока без звездочек
            if (Comp_Deck.destroed_ships):# Корабль уничтожен
                print("Ваш орабль уничтожен!")
                direction = Comp_Deck.destroed_ships[-1]
                Comp_Deck.set_destroed_ships()# убираем последний элемент в котором задано направление
                Comp_Deck.add_oq_position(Comp_Deck.destroed_ships, len(Comp_Deck.destroed_ships), direction, 1) #выставляем занятые позиции вокруг убитого корабля
                #Comp_Deck.dest_player_ship(Player_Deck.battle_field)
                destroy_pos.extend(Comp_Deck.destroed_ships)
                Comp_Deck.set_ships(destroy_pos,1)
                destroed_ship.clear()
                if len(Player_Deck.ship_list) == 0:
                    print("Все ваши корабли были уничтожены! Вы проиграли!!")
                    Victory = True
                    break
            else: #было попадание, повторный ход
                #Player_Deck.set_ships(destroy_pos, 1)
                if turn == 11:
                    temp_list = [21,12]
                    turn = random.choice(temp_list)
                elif (turn == 21):
                    temp_list = [11,22,32]
                    turn = random.choice(temp_list)
                elif turn == 31:
                    temp_list = [21,32,41]
                    turn = random.choice(temp_list)
                elif turn == 41:
                    temp_list = [31,42,51]
                    turn = random.choice(temp_list)
                elif turn == 51:
                    temp_list = [41,52,61]
                    turn = random.choice(temp_list)
                elif turn == 61:
                    temp_list = [51,62]
                    turn = random.choice(temp_list)
                elif turn == 12:
                    temp_list = [11,22,13]
                    turn = random.choice(temp_list)
                elif turn == 13:
                    temp_list = [12,23,14]
                    turn = random.choice(temp_list)
                elif turn == 14:
                    temp_list = [13,24,15]
                    turn = random.choice(temp_list)
                elif turn == 15:
                    temp_list = [14,25,16]
                    turn = random.choice(temp_list)
                elif turn == 16:
                    temp_list = [15,26,]
                    turn = random.choice(temp_list)
                elif turn == 62:
                    temp_list = [52,61,63]
                    turn = random.choice(temp_list)
                elif turn == 63:
                    temp_list = [53,62,64]
                    turn = random.choice(temp_list)
                elif turn == 64:
                    temp_list = [54,63,65]
                    turn = random.choice(temp_list)
                elif turn == 65:
                    temp_list = [55,64,66]
                    turn = random.choice(temp_list)
                elif turn == 66:
                    temp_list = [56,65]
                    turn = random.choice(temp_list)
                elif turn == 26:
                    temp_list = [16,25,36]
                    turn = random.choice(temp_list)
                elif turn == 36:
                    temp_list = [26,35,46]
                    turn = random.choice(temp_list)
                elif turn == 46:
                    temp_list = [36,45,56]
                    turn = random.choice(temp_list)
                elif turn == 56:
                    temp_list = [46,55,66]
                    turn = random.choice(temp_list)
                else:
                    temp_list = [(turn + 1),(turn - 1), (turn + 10),(turn -10)]
                    turn = random.choice(temp_list)
                if turn not in Onedeck_points:
                    Onedeck_points.remove(turn)  # убираем точку из списка возможных ходов
                continue
                print(f"Ход оппонента: {turn}")
        else:
            Turn = False
        Comp_Deck.turn_position.append(turn)
        Comp_Deck.comp_show(Player_Deck.battle_field, Player_Deck.enemy_field, Comp_Deck.turn_position, good_comp_point)
        input("Оппонент сделал ход, нажмите Enter!")
        if Victory:
            break
            #Player_Deck.set_ships(destroy_pos, 0)