from random import randint

import TicTacToeBot
from time import sleep

game_board = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " "]

turn_rotation = 'x'
turn_number = 1
giveUp = False


def turn(player):
    global giveUp
    if player == "o":
        location = TicTacToeBot.take_turn(game_board, turn_number)
        if location == -1:
            giveUp = True
            return
        game_board[location] = "o"
    else:
        spaces = []
        for i in range(9):
            if game_board[i] == " ":
                spaces.append(i)
        # randomly selects a space
        index = randint(0, len(spaces) - 1)
        game_board[spaces[index]] = "x"


def check(board):
    # checks diagonal
    if (board[0] == board[8]) & (board[4] == board[8]) & (board[0] != " "):
        return True
    if (board[2] == board[6]) & (board[4] == board[6]) & (board[2] != " "):
        return True

    for i in range(3):
        # checks for win in the horizontal
        if (board[(3 * i) - 3] == board[(3 * i) - 1]) & (board[(3 * i) - 2] == board[(3 * i) - 1]) & (
                board[(3 * i) - 3] != " "):
            return True
        # checks for win in the vertical
        if (board[(i - 1)] == board[(i + 5)]) & (board[(i + 2)] == board[(i + 5)]) & (board[i - 1] != " "):
            return True

    return False


def restart():
    global game_board
    global turn_rotation
    global turn_number
    global giveUp

    game_board = [" ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " "]

    turn_rotation = 'x'
    turn_number = 1
    giveUp = False


if __name__ == "__main__":
    TicTacToeBot.initiate()
    while True:
        print(str(turn_number) + "\n")
        turn(turn_rotation)
        if giveUp:
            print("o's gives up")
            TicTacToeBot.punish()
            print("Punished!")

            TicTacToeBot.clean_up()
            sleep(2)
            TicTacToeBot.initiate()
            restart()
            continue

        print("|" + str(game_board[0]) + " " + str(game_board[1]) + " " + str(game_board[2]) + "|\n|" +
              str(game_board[3]) + " " + str(game_board[4]) + " " + str(game_board[5]) + "|\n|" +
              str(game_board[6]) + " " + str(game_board[7]) + " " + str(game_board[8]) + "|")
        if check(game_board):
            print(turn_rotation + "'s wins!")
            if turn_rotation == "x":
                TicTacToeBot.punish()
                print("Punished!")
            else:
                TicTacToeBot.reward()
                print("Rewarded!")
            TicTacToeBot.clean_up()
            sleep(1)
            TicTacToeBot.initiate()
            restart()
            continue

        turn_rotation = 'o' if turn_rotation == 'x' else 'x'

        if turn_number == 9:
            print("Ya both lost")
            TicTacToeBot.clean_up()
            sleep(1)
            TicTacToeBot.initiate()
            restart()
            continue

        turn_number += 1
