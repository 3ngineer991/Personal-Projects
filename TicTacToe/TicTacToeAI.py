# check board for available spaces
# check memory for best spots (if scenario does not exist in memory create it)
# randomly select one of the best spots
# if turn results in loss remove last play from best spots list

import null as null
from random import randint

memory = [[], [], [], [], [], [], [], [], []]
turns = []
file = null


# loads file into list
def initiate():
    global memory
    global file
    file = open("brain.csv", "r+")

    for i in range(9):
        temp_brain = file.readline().split(",")
        temp_brain[-1] = temp_brain[-1].removesuffix("\n")
        for j in range(len(temp_brain)):
            if temp_brain[j] != "":
                memory[i].append(temp_brain[j])


# loads list into file
def clean_up():
    global memory
    global file
    global turns

    file.seek(0)
    file.truncate()
    for i in range(8):
        for j in range(len(memory[i])):
            file.write(memory[i][j] + ("" if len(memory[i]) - 1 == j else ","))
        file.write("\n")
    memory = [[], [], [], [], [], [], [], [], []]
    turns = []

    file.close()


# returns a playable space (returns -1 if there are no good options)
def take_turn(board, turn_number):
    global memory
    global turns
    # converts board from list to string
    board_string = ""
    for i in board:
        board_string += i
    # finds a match from memory
    is_match = True
    # if it throws IndexError then a match was not found
    try:
        match = 0
        temp = memory[turn_number - 1][match].replace("*", " ")
        temp = temp.replace("#", " ")
        while board_string != temp:
            match += 1
            temp = memory[turn_number - 1][match].replace("*", " ")
            temp = temp.replace("#", " ")
    except IndexError:
        is_match = False
        match = -1
    # creates new scenario if none were found
    if not is_match:
        memory[turn_number - 1].append(board_string.replace(" ", "*"))
        print("new scenario created")

    # select best spot to play
    # adds the playable spaces to a list
    spaces = []
    game_state = memory[turn_number - 1][match]
    for i in range(9):
        if game_state[i] == "*":
            spaces.append(i)
    # if there are no spaces available bot gives up
    if not spaces:
        return -1
    # randomly selects a space
    index = randint(0, len(spaces) - 1)
    # returns the index that should be played also adds to the
    # turns list for punishment system
    turns.append(str(spaces[index]) + " " + str(match))
    return spaces[index]


# if move results in loss use this to prevent the same mistake
def punish():
    global turns
    global memory

    board = int(turns[-1].split(" ")[1])
    index = int(turns[-1][0])
    turn_number = 2 * len(turns)

    temp = ""
    for i in range(9):
        if i != index:
            temp += memory[turn_number - 1][board][i]
        else:
            temp += "#"

    memory[turn_number - 1][board] = temp


# if move results in win use this to prevent the bot from making a bad move this turn
def reward():
    global turns
    global memory

    board = int(turns[-1].split(" ")[1])
    index = int(turns[-1][0])
    turn_number = 2 * len(turns)

    temp = ""
    for i in range(9):
        if i != index and memory[turn_number - 1][board][i] == "*":
            temp += "#"
        else:
            temp += memory[turn_number - 1][board][i]

    memory[turn_number - 1][board] = temp
