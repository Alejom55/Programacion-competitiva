import time
inicio = time.time()


def calculate_score(list: list):
    score_list = []

    for player in list:
        total_score = 0
        counter = 0
        for roll in player:
            counter += 1
            if roll == "X":
                total_score += calculate_strike(player, counter)
            elif roll == "/":
                total_score += calculate_spare(last_number, player, counter)
            elif roll.isdigit():
                last_number = int(roll)
                total_score += int(roll)
        
        total_score = subtract(total_score, player)
        score_list.append(total_score)
    

        
    return score_list

def calculate_strike(player, counter:int):
    next_roll = player[counter + 1]
    next_next_roll = player[counter + 3]

    if next_roll == "X":
        score = 20
    elif next_next_roll == "/":
        score = 10 + int(next_roll) + calculate_spare(next_roll,player,counter, True)
    else:
        score = 10 + int(next_roll) + int(next_next_roll)
    return score

def calculate_spare(last_number:int , player, counter:int, verify: bool = False):
    next_number = player[counter + 1]
    if verify == True:
        score = 10 - int(last_number)
        
    elif next_number == "X":
        score = 10 - last_number + 10
    else:
        score = 10 - last_number + int(next_number)
    
    return score

def subtract(total: int, player):
    if couples(player) > 10:
        if player[-5] == "X":
            total = total - int(player[-3]) - int(player[-1])
        elif player[-3] == "/":
            total = total - int(player[-1])
    return total

def couples(player):
    score = 0
    counter = 0
    while True:
        if counter >= len(player):
            break
        elif counter == len(player) - 1:
            score += 1
            break

        if player[counter] == "X":
            score += 1
            counter += 2
        elif player[counter].isdigit() and player[counter + 2] == "/":
            score += 1
            counter += 4
        elif player[counter].isdigit() and player[counter + 2].isdigit():
            score += 1
            counter += 4
        elif player[counter].isdigit():
            score += 1
    return score

def show_score(list: list):
    for i in list:
        print(i)

#game_list = ["1 0 1 / 2 2 X 3 3 X 1 / 3 / X 1 2",
#"1 0 1 / 2 2 X 3 3 X 1 / 3 / 1 / X 8 0",
#"1 0 1 / 2 2 X 3 3 X 1 / 3 / 1 / 8 / 9",
#"X 2 3 X X X X X X X X 1 2"
#]

game_list = []

while True:
    inputs = str(input()).strip()
    if inputs == "Game Over":
        break
    elif inputs:
        game_list.append(inputs)


show_score(calculate_score(game_list))

fin = time.time()
print(fin-inicio)