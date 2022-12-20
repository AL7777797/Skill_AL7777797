def start():
    while True:
        enter_game = input("Готовы начать игру? \nВведите 'Да' или 'Нет'\n")
        if enter_game == "Да":
            print("Начнем!")
            break
        elif enter_game == "Нет":
            print("Ну и пожалуйста, ну и не нужно, ну и не очень-то мне нужно!")
        else:
            print("Я вас не понял.")

print("Приветствую!")
start()

gamer_1 = input("Игрок №1, введите свое имя: ")
gamer_2 = input("Игрок №2, введите свое имя: ")

print("...........................")
print(f"В первые мгновения зарождения вселенной появились два бога: {gamer_1} и {gamer_2}.\
 \nДолго спорили, кто из них главнее.\
  \nЧтоб решить этот спор решили они сыграть в игру... ")

fild_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def fild():
    print("...........................")
    print("Ваше игровое поле")
    print("    ", *fild_list[0], *fild_list[1], *fild_list[2])
    print("    ", *fild_list[3], *fild_list[4], *fild_list[5])
    print("    ", *fild_list[6], *fild_list[7], *fild_list[8])

fild()

def game_move_x():
    another_move = input("................\nВыберете ячейку: ")
    counter = 0
    for i in fild_list:
        if another_move == i:
            fild_list[int(i)-1] = "X"
        counter += 1
    return fild_list

def game_move_y():
    another_move = input("................\nВыберете ячейку: ")
    counter = 0
    for i in fild_list:
        if another_move == i:
            fild_list[int(i)-1] = "O"
        counter += 1
    return fild_list

def victory_x():
    if fild_list[0] == "X" and fild_list[1] == "X" and fild_list[2] == "X" \
            or (fild_list[2] == "X" and fild_list[5] == "X" and fild_list[8] == "X") \
            or (fild_list[2] == "X" and fild_list[4] == "X" and fild_list[6] == "X") \
            or (fild_list[6] == "X" and fild_list[7] == "X" and fild_list[8] == "X") \
            or (fild_list[1] == "X" and fild_list[4] == "X" and fild_list[7] == "X") \
            or (fild_list[0] == "X" and fild_list[3] == "X" and fild_list[6] == "X") \
            or (fild_list[0] == "X" and fild_list[4] == "X" and fild_list[8] == "X") \
            or (fild_list[3] == "X" and fild_list[4] == "X" and fild_list[5] == "X") \
            or (fild_list[6] == "X" and fild_list[7] == "X" and fild_list[8] == "X"):
        return True
    else:
        return False

def victory_y():
    if fild_list[0] == "O" and fild_list[1] == "X" and fild_list[2] == "X" \
            or (fild_list[2] == "O" and fild_list[5] == "O" and fild_list[8] == "O") \
            or (fild_list[6] == "O" and fild_list[7] == "O" and fild_list[8] == "O") \
            or (fild_list[2] == "O" and fild_list[4] == "O" and fild_list[6] == "O") \
            or (fild_list[1] == "O" and fild_list[4] == "O" and fild_list[7] == "O") \
            or (fild_list[0] == "O" and fild_list[3] == "O" and fild_list[6] == "O") \
            or (fild_list[0] == "O" and fild_list[4] == "O" and fild_list[8] == "O") \
            or (fild_list[3] == "O" and fild_list[4] == "O" and fild_list[5] == "O") \
            or (fild_list[6] == "O" and fild_list[7] == "O" and fild_list[8] == "O"):
        return True
    else:
        return False

count = 0
while True:
    if count == 9:
        print("Ничья! Бога - нет!\nКонец игры!")
        break
    elif victory_x() == True:
        print(f"Ура! Победа! Победа! Ура! Теперь {gamer_1} - главный бог!\nКонец игры!")
        break
    elif victory_y() == True:
        print(f"Ура! Победа! Победа! Ура! Теперь {gamer_2} - главный бог!\nКонец игры!")
        break
    else:
        if count % 2 == 0:
            print(f"Ходит {gamer_1}.")
            print(f"{count + 1}-й ход.")
            game_move_x()
            fild()
            count += 1
        else:
            print(f"Ходит {gamer_2}.")
            print(f"{count + 1}-й ход.")
            game_move_y()
            fild()
            count += 1

