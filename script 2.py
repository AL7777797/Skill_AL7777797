fild_list = ["X", "X", "X", "4", "5", "6", "7", "8", "9"]

print(fild_list[0], fild_list[1], fild_list[2])

def victory_x():
    if fild_list[0] and fild_list[1] and fild_list[2] \
     or fild_list[2] and fild_list[5] and fild_list[8] \
     or fild_list[6] and fild_list[7] and fild_list[8] \
      or fild_list[0] and fild_list[3] and fild_list[6] \
      or fild_list[0] and fild_list[4] and fild_list[8] \
       or fild_list[3] and fild_list[4] and fild_list[5] \
        or fild_list[6] and fild_list[7] and fild_list[8] == "X":
        print(f"Ура! Победа! Победа! Ура!\n{gamer_1} победил!")
    return True

def victory_y():
    if fild_list[0] and fild_list[1] and fild_list[2] \
     or fild_list[2] and fild_list[5] and fild_list[8] \
     or fild_list[6] and fild_list[7] and fild_list[8] \
      or fild_list[0] and fild_list[3] and fild_list[6] \
      or fild_list[0] and fild_list[4] and fild_list[8] \
       or fild_list[3] and fild_list[4] and fild_list[5] \
        or fild_list[6] and fild_list[7] and fild_list[8] == "O":
        print(f"Ура! Победа! Победа! Ура!\n{gamer_2} победил!")
    return False

victory_x()
