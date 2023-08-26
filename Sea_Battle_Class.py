import copy
class Deck:
    destroed_ships = []
    def __init__(self, Owner = "", ship_list = [], oq_position = [], field = [], turn_position = []):
        self.Owner = Owner
        self.ship_list = ship_list.copy()
        self.oq_position = oq_position.copy()
        #self.battle_field = field[:]#.copy()
        self.battle_field = copy.deepcopy(field)
        self.enemy_field = copy.deepcopy(field)
        self.turn_position = turn_position.copy()
    def get_owner(self):
        return self.Owner
    def set_destroed_ships(self):
        self.destroed_ships.pop(-1)
    def add_ship(self, Ship):
        self.ship_list.append(Ship)
    def print_emty_field(self):
        print(f"Игровое поле:")
        print("   | 1 | 2 | 3 | 4 | 5 | 6 | ")
        print(" 1 | 0 | 0 | 0 | 0 | 0 | 0 | ")
        print(" 2 | 0 | 0 | 0 | 0 | 0 | 0 | ")
        print(" 3 | 0 | 0 | 0 | 0 | 0 | 0 | ")
        print(" 4 | 0 | 0 | 0 | 0 | 0 | 0 | ")
        print(" 5 | 0 | 0 | 0 | 0 | 0 | 0 | ")
        print(" 6 | 0 | 0 | 0 | 0 | 0 | 0 | ")
    def add_oq_position(self, position, number_of_deck, direction, position_type):
        i = 0
        oq_position = []
        if position_type == 0:# выставляем позиции вокруг кораблей
            oq_position = self.oq_position
        else:
            oq_position = self.turn_position #Выставляем позиции вокруг убитого корабля
        for pos in position:
            var = str(pos)
            x = var[0]
            y = var[1]
            if direction == 1: #вертикальное положение
                if (x == "1"):
                    i = 0
                    while i < number_of_deck:
                        oq_position.append(position[i])
                        if (x == "1" and y == "1"):
                            oq_position.append(position[i] + 10)
                            oq_position.append(position[i] + 1)
                            oq_position.append(position[i] + 11)
                        else:
                            oq_position.append(position[i] + 1)
                            oq_position.append(position[i] - 1)
                            oq_position.append(position[i] + 10)
                            oq_position.append(position[i] + 11)
                            oq_position.append(position[i] + 9)
                        i += 1
                else:
                    oq_position.append(pos)
                    oq_position.append(pos - 10)
                    oq_position.append(pos + 10)
                    oq_position.append(pos - 1)
                    oq_position.append(pos - 11)  # доюавление двух координат по углам
                    oq_position.append(pos + 9)
                    oq_position.append(pos + 1)
                    oq_position.append(pos - 9)  # доюавление двух координат по углам
                    oq_position.append(pos + 11)
            elif direction == 2: # горизонтальное расположение
                if (x == "1"):
                    while i < number_of_deck:
                        oq_position.append(position[i])
                        if (x == "1" and y == "1"):
                            oq_position.append(position[i] + 10)
                            oq_position.append(position[i] + 1)
                            oq_position.append(position[i] + 11)
                            #if (x == "1" and y != "1"):
                        oq_position.append(position[i] + 1)
                        oq_position.append(position[i] - 1)
                        i+=1
                else:
                    oq_position.append(pos)
                    oq_position.append(pos - 11)
                    oq_position.append(pos - 10)
                    oq_position.append(pos - 9)
                    oq_position.append(pos + 11)
                    oq_position.append(pos + 10)
                    oq_position.append(pos + 9)
            else:
                if (x == "1"):
                    oq_position.append(pos)
                    if (x == "1" and y == "1"):
                        oq_position.append(pos + 10)
                        oq_position.append(pos + 11)
                        oq_position.append(pos + 1)
                    else:
                        oq_position.append(pos - 1)
                        oq_position.append(pos + 1)
                        oq_position.append(pos + 9)
                        oq_position.append(pos + 10)
                        oq_position.append(pos + 11)
                else:
                    oq_position.append(pos)
                    oq_position.append(pos - 1)
                    oq_position.append(pos + 1)
                    oq_position.append(pos - 10)
                    oq_position.append(pos + 10)
                    oq_position.append(pos - 11)
                    oq_position.append(pos + 11)
                    oq_position.append(pos - 9)
                    oq_position.append(pos + 9)
                    oq_position.append(pos - 9)
        #print(position)
        #print(self.oq_position)
        if position_type == 0:# выставляем позиции вокруг кораблей
            self.oq_position = list(set(self.oq_position))
        else:
            self.turn_position = list(set(self.turn_position))

    def set_ships(self, destroed_ships, miss):
        if destroed_ships:
            for point in destroed_ships:
                point = str(point)
                y = int(point[1]) - 1
                x = int(point[0]) - 1
                # print(f"Координата y = {y}")
                # print(f"Координата x = {x}")
                for i, value in enumerate(self.enemy_field):  # получаем индекс и значение в одну переменную, получается
                    # множество, первый элемент которого индекс, а второй список значений по этому индексу
                    if y == i:  # выделяем индекс для координаты по у
                        for j, val in enumerate(value):
                            if x == j:  # получаем индекс для сравнения координаты по х
                                lst = self.enemy_field[y]
                                if miss == 1:
                                    lst[x] = "X"
                                else:
                                    lst[x] == "*"
                                break
            if self.Owner == "Player":
                print("        Ваше поле                     Поле оппонента")
                print("  | 1 | 2 | 3 | 4 | 5 | 6       | 1 | 2 | 3 | 4 | 5 | 6 |")
                x = 1
                for i in self.battle_field:
                    y = self.enemy_field[x - 1]
                    print(
                        f"{x} | {i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} | {i[5]}        {x} | {y[0]} | {y[1]} | {y[2]} | {y[3]} | {y[4]} | {y[5]} | ")
                    x += 1
        else:
            for ship in self.ship_list:
                if(ship.Type == "Threedeck"):
                    #print(f"Позиция трехпалубного {ship.pos}")
                    for point in ship.pos:

                        point = str(point)
                        y = int(point[1]) - 1
                        x = int(point[0]) - 1
                        #print(f"Координата y = {y}")
                        #print(f"Координата x = {x}")
                        for i, value in enumerate(self.battle_field):#получаем индекс и значение в одну переменную, получается
                            # множество, первый элемент которого индекс, а второй список значений по этому индексу
                            if y == i: # выделяем индекс для координаты по у
                                for j, val in enumerate(value):
                                    if x == j: # получаем индекс для сравнения координаты по х
                                        lst = self.battle_field[y]
                                        lst[x] = "■"
                                        break
                if (ship.Type == "Twodeck"):
                   # print(f"Позиция двухпалубного{ship.pos}")
                    for point in ship.pos:

                        point = str(point)
                        y = int(point[1]) - 1
                        x = int(point[0]) - 1
                       # print(f"Координата x = {x + 1}")
                        #print(f"Координата y = {y + 1}")
                        for i, value in enumerate(self.battle_field):  # получаем индекс и значение в одну переменную, получается
                            # множество, первый элемент которого индекс, а второй список значений по этому индексу
                            if y == i:  # выделяем индекс для координаты по у
                                for j, val in enumerate(value):
                                    if x == j:  # получаем индекс для сравнения координаты по х
                                        lst = self.battle_field[y]
                                        lst[x] = "■"
                                        break
                if(ship.Type == "Onedeck"):
                    for point in ship.pos:

                        point = str(point)
                        y = int(point[1]) - 1
                        x = int(point[0]) - 1
                        #print(f"Координата x = {x+1}")
                        #print(f"Координата y = {y+1}")
                        for i, value in enumerate(self.battle_field):#получаем индекс и значение в одну переменную, получается
                            # множество, первый элемент которого индекс, а второй список значений по этому индексу
                            if y == i: # выделяем индекс для координаты по у
                                for j, val in enumerate(value):
                                    if x == j: # получаем индекс для сравнения координаты по х
                                        lst = self.battle_field[y]
                                        lst[x] = "■"
                                        break
            if self.Owner == "Player":
                print("  | 1 | 2 | 3 | 4 | 5 | 6")
                x = 1
                for i in self.battle_field:

                    print(f"{x} | {i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} | {i[5]}")
                    x += 1

    def set_oq(self, position_type):
        if position_type == 0:
            for point in self.oq_position:
                p = str(point)
                y = int(p[1]) - 1
                x = int(p[0]) - 1
                #print(f"Занятая Координата x = {x} y = {y}")
                #print(f"Занятая Координата ")
                for i, value in enumerate(self.battle_field):  # получаем индекс и значение в одну переменную, получается
                    # множество, первый элемент которого индекс, а второй список значений по этому индексу
                    if y == i:  # выделяем индекс для координаты по у
                        for j, val in enumerate(value):
                            if x == j:  # получаем индекс для сравнения координаты по х
                                lst = self.battle_field[y]
                                lst[x] = "*"
        else:
            for point in self.turn_position:
                p = str(point)
                y = int(p[1]) - 1
                x = int(p[0]) - 1
                #print(f"Занятая Координата x = {x} y = {y}")
                #print(f"Занятая Координата ")
                for i, value in enumerate(self.enemy_field):  # получаем индекс и значение в одну переменную, получается
                    # множество, первый элемент которого индекс, а второй список значений по этому индексу
                    if y == i:  # выделяем индекс для координаты по у
                        for j, val in enumerate(value):
                            if x == j:  # получаем индекс для сравнения координаты по х
                                lst = self.enemy_field[y]
                                lst[x] = "*"
                                #break
    def start_battle(self,field):
        self.battle_field = copy.deepcopy(field)
        for ship in self.ship_list:
            for point in ship.pos:
                point = str(point)
                y = int(point[1]) - 1
                x = int(point[0]) - 1
                # print(f"Координата y = {y}")
                # print(f"Координата x = {x}")
                for i, value in enumerate(
                        self.battle_field):  # получаем индекс и значение в одну переменную, получается
                    # множество, первый элемент которого индекс, а второй список значений по этому индексу
                    if y == i:  # выделяем индекс для координаты по у
                        for j, val in enumerate(value):
                            if x == j:  # получаем индекс для сравнения координаты по х
                                lst = self.battle_field[y]
                                lst[x] = "■"
        print("        Ваше поле                      Поле оппонента")
        print("  | 1 | 2 | 3 | 4 | 5 | 6        | 1 | 2 | 3 | 4 | 5 | 6 |")
        x = 1
        for i in self.battle_field:
            y = self.enemy_field[x -1]
            print(
                f"{x} | {i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} | {i[5]}      {x} | {y[0]} | {y[1]} | {y[2]} | {y[3]} | {y[4]} | {y[5]} | ")
            x += 1
    def get_enemy_field(self, enemy_field):
        self.enemy_field = copy.deepcopy(enemy_field)

    def move(self, point, ship_list):
        self.destroed_ships.clear()
        stop = False
        ship_index = 0
        point_index = 0
        destroed_ship = []
        self.turn_position.append(point)
        for ship in ship_list:
            if stop:
                break
            for points in ship.pos:
                if stop:
                    break
                if point == points:
                    var = str(point)
                    y = int(var[1]) - 1
                    x = int(var[0]) - 1
                    # print(f"Координата x = {x+1}")
                    # print(f"Координата y = {y+1}")
                    for i, value in enumerate(self.enemy_field):  # получаем индекс и значение в одну переменную, получается
                        # множество, первый элемент которого индекс, а второй список значений по этому индексу
                        if y == i:  # выделяем индекс для координаты по у
                            for j, val in enumerate(value):
                                if x == j:  # получаем индекс для сравнения координаты по х
                                    lst = self.enemy_field[y]
                                    lst[x] = "X"
                                    stop = True
                                    break
                else:
                    var = str(point)
                    y = int(var[1]) - 1
                    x = int(var[0]) - 1
                    # print(f"Координата x = {x+1}")
                    # print(f"Координата y = {y+1}")
                    for i, value in enumerate(self.enemy_field):  # получаем индекс и значение в переменные, получается
                        # первый элемент индекс, а второй список значений по этому индексу
                        if y == i:  # выделяем индекс для координаты по у
                            for j, val in enumerate(value):
                                if x == j:  # получаем индекс для сравнения координаты по х
                                    lst = self.enemy_field[y]
                                    lst[x] = "*"
                if not stop:
                    point_index += 1
            if not stop:
                point_index = 0
                ship_index += 1
        if not stop:
            print("Мимо!")
        else:
            Type = ship_list[ship_index].Type
            #print(Type)
            if (Type == "Threedeck"):
                #print(f"Координта корабля: {ship_list[ship_index].pos[0]}")
                #print(f"Координта корабля: {ship_list[ship_index].pos[1]}")
               # print(f"Координта корабля: {ship_list[ship_index].pos[2]}")
                if ship_list[ship_index].pos[0] in self.turn_position and ship_list[ship_index].pos[1] in self.turn_position and ship_list[ship_index].pos[2] in self.turn_position:
                    self.destroed_ships.append(ship_list[ship_index].pos[0])
                    self.destroed_ships.append(ship_list[ship_index].pos[1])
                    self.destroed_ships.append(ship_list[ship_index].pos[2])
                    self.destroed_ships.append(ship_list[ship_index].direction)
                    self.turn_position.remove(ship_list[ship_index].pos[0])
                    self.turn_position.remove(ship_list[ship_index].pos[1])
                    self.turn_position.remove(ship_list[ship_index].pos[2])
                    ship_list.pop(ship_index)
                    return True
                else:
                    return True
            elif (Type == "Twodeck"):
                #print(f"Координта корабля: {ship_list[ship_index].pos[0]}")
                #print(f"Координта корабля: {ship_list[ship_index].pos[1]}")

                if ship_list[ship_index].pos[0] in self.turn_position and ship_list[ship_index].pos[1] in self.turn_position:
                    self.destroed_ships.append(ship_list[ship_index].pos[0])
                    self.destroed_ships.append(ship_list[ship_index].pos[1])
                    self.destroed_ships.append(ship_list[ship_index].direction)
                    self.turn_position.remove(ship_list[ship_index].pos[0])
                    self.turn_position.remove(ship_list[ship_index].pos[1])
                    ship_list.pop(ship_index)
                    return True
                else:
                    return True
            elif (Type == "Onedeck"):
                #print(f"Координта корабля: {ship_list[ship_index].pos[0]}")
                if ship_list[ship_index].pos[point_index] in self.turn_position:
                    self.destroed_ships.append(ship_list[ship_index].pos[point_index])
                    self.destroed_ships.append(ship_list[ship_index].direction)
                    self.turn_position.remove(ship_list[ship_index].pos[point_index])
                    ship_list[ship_index].pos.pop(point_index)
                    if len(ship_list[ship_index].pos) == 0:
                        ship_list.pop(ship_index)
                    return True

        return False
    def comp_show(self,Player_field, enemy_field, all_point, good_point):
        player_field = Player_field
        #print(player_field)
        #print(enemy_field)
        for point in all_point:
            point = str(point)
            y = int(point[1]) - 1
            x = int(point[0]) - 1
            # print(f"Координата y = {y}")
            # print(f"Координата x = {x}")
            for i, value in enumerate(player_field):  # получаем индекс и значение в одну переменную, получается
                # множество, первый элемент которого индекс, а второй список значений по этому индексу
                if y == i:  # выделяем индекс для координаты по у
                    for j, val in enumerate(value):
                        if x == j:  # получаем индекс для сравнения координаты по х
                            lst = player_field[y]
                            lst[x] = "*"

        if good_point:
            for point in good_point:
                point = str(point)
                y = int(point[1]) - 1
                x = int(point[0]) - 1
                # print(f"Координата y = {y}")
                # print(f"Координата x = {x}")
                for i, value in enumerate(player_field):  # получаем индекс и значение в одну переменную, получается
                    # множество, первый элемент которого индекс, а второй список значений по этому индексу
                    if y == i:  # выделяем индекс для координаты по у
                        for j, val in enumerate(value):
                            if x == j:  # получаем индекс для сравнения координаты по х
                                lst = player_field[y]
                                lst[x] = "X"

        print("        Ваше поле                        Поле оппонента")
        print("  | 1 | 2 | 3 | 4 | 5 | 6          | 1 | 2 | 3 | 4 | 5 | 6 |")
        x = 1
        for i in player_field:
            y = enemy_field[x - 1]
            print(f"{x} | {i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} | {i[5]} |      {x} | {y[0]} | {y[1]} | {y[2]} | {y[3]} | {y[4]} | {y[5]} | ")
            x += 1

    def player_show(self,Player_field, enemy_field, all_point, good_point):
        player_field = enemy_field
        #print(player_field)
        #print(enemy_field)
        for point in all_point:
            point = str(point)
            y = int(point[1]) - 1
            x = int(point[0]) - 1
            # print(f"Координата y = {y}")
            # print(f"Координата x = {x}")
            for i, value in enumerate(player_field):  # получаем индекс и значение в одну переменную, получается
                # множество, первый элемент которого индекс, а второй список значений по этому индексу
                if y == i:  # выделяем индекс для координаты по у
                    for j, val in enumerate(value):
                        if x == j:  # получаем индекс для сравнения координаты по х
                            lst = player_field[y]
                            lst[x] = "*"

        if good_point:
            for point in good_point:
                point = str(point)
                y = int(point[1]) - 1
                x = int(point[0]) - 1
                # print(f"Координата y = {y}")
                # print(f"Координата x = {x}")
                for i, value in enumerate(player_field):  # получаем индекс и значение в одну переменную, получается
                    # множество, первый элемент которого индекс, а второй список значений по этому индексу
                    if y == i:  # выделяем индекс для координаты по у
                        for j, val in enumerate(value):
                            if x == j:  # получаем индекс для сравнения координаты по х
                                lst = player_field[y]
                                lst[x] = "X"

        print("        Ваше поле                        Поле оппонента")
        print("  | 1 | 2 | 3 | 4 | 5 | 6          | 1 | 2 | 3 | 4 | 5 | 6 |")
        x = 1
        for i in Player_field:
            y = enemy_field[x - 1]
            print(f"{x} | {i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} | {i[5]} |      {x} | {y[0]} | {y[1]} | {y[2]} | {y[3]} | {y[4]} | {y[5]} | ")
            x += 1
    def __del__(self):
        self.Owner = ""
        self.ship_list.clear()
        self.oq_position.clear()
        # self.battle_field = field[:]#.copy()
        self.battle_field.clear()
        self.enemy_field.clear()
        self.turn_position.clear()
class Ship:
    def __init__(self, Type = "", position = [], direction = 0):
        self.Type = Type
        self.pos = position.copy()
        self.direction = direction
    def __del__(self):
        self.Type = ""
        self.pos.clear()
        self.direction = 0
    # def dest_player_ship(self, field):
        # for point in self.turn_position:
        #     p = str(point)
        #     y = int(p[1]) - 1
        #     x = int(p[0]) - 1
        #     # print(f"Занятая Координата x = {x} y = {y}")
        #     # print(f"Занятая Координата ")
        #     for i, value in enumerate(self.enemy_field):  # получаем индекс и значение в одну переменную, получается
        #         # множество, первый элемент которого индекс, а второй список значений по этому индексу
        #         if y == i:  # выделяем индекс для координаты по у
        #             for j, val in enumerate(value):
        #                 if x == j:  # получаем индекс для сравнения координаты по х
        #                     lst = self.enemy_field[y]
        #                     lst[x] = "*"
        #                     lst = field
        #                     lst[x] = "*"