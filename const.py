f = open('symbols/quest', 'r')
for quest_str in f:
    break
f.close()

f = open('symbols/forest', 'r')
for forest_str in f:
    break
f.close()

f = open('symbols/corovan', 'r')
for corovan_str in f:
    break
f.close()

f = open('symbols/defen', 'r')
for defen_str in f:
    break
f.close()

f = open('symbols/attack', 'r')
for attack_str in f:
    break
f.close()

f = open('symbols/white', 'r')
for white_str in f:
    break
f.close()

f = open('symbols/red', 'r')
for red_str in f:
    break
f.close()

f = open('symbols/black', 'r')
for black_str in f:
    break
f.close()

f = open('symbols/blue', 'r')
for blue_str in f:
    break
f.close()

f = open('symbols/cave', 'r')
for cave_str in f:
    break
f.close()

report_str = '/report'

battle_hours = [24, 4, 8, 12, 16, 20]
forest_hours = [8, 9, 10, 11, 12, 13, 14, 15, 16]
cave_hours = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
corovan_minutes = [10, 20, 30, 40, 50]
corovan_hours = [4, 5, 6]
PAUSE = 10

attack_dict = {'white': white_str, 'blue': blue_str, 'black': black_str, 'red': red_str}


def get_castle():
    f = open("castle.txt", 'r')
    for attack_str in f:
        break
    f.close()
    return attack_str
