from queue import Queue

import TicTacToe
import time
import keyboard


class Format:
    end = '\033[0m'
    underline = '\033[4m'


game_state = True


highlight = 4


def sleep(secs):
    curr_time = time.time()
    while curr_time + secs >= time.time():
        continue


def print_board(board, location):
    for i in range(50):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Welcome to noughts and Crosses")
    if location == -1:
        for j in range(2):
            print(" " + Format.underline + board[j * 3] + "|" + board[j * 3 + 1] + "|" + board[j * 3 + 2] + Format.end)
        print(" " + board[6] + "|" + board[7] + "|" + board[8])
    elif location == 0:

        print("[" + Format.underline + board[0] + "]" + board[1] + "|" + board[2] + Format.end)
        print(" " + Format.underline + board[3] + "|" + board[4] + "|" + board[5] + Format.end)
        print(" " + board[6] + "|" + board[7] + "|" + board[8])

    elif location == 1:

        print(" " + Format.underline + board[0] + "[" + board[1] + "]" + board[2] + Format.end)
        print(" " + Format.underline + board[3] + "|" + board[4] + "|" + board[5] + Format.end)
        print(" " + board[6] + "|" + board[7] + "|" + board[8])
    elif location == 2:

        print(" " + Format.underline + board[0] + "|" + board[1] + "[" + board[2] + Format.end + "]")
        print(" " + Format.underline + board[3] + "|" + board[4] + "|" + board[5] + Format.end)
        print(" " + board[6] + "|" + board[7] + "|" + board[8])

    elif location == 3:

        print(" " + Format.underline + board[0] + "|" + board[1] + "|" + board[2] + Format.end)
        print("[" + Format.underline + board[3] + "]" + board[4] + "|" + board[5] + Format.end)
        print(" " + board[6] + "|" + board[7] + "|" + board[8])

    elif location == 4:

        print(" " + Format.underline + board[0] + "|" + board[1] + "|" + board[2] + Format.end)
        print(" " + Format.underline + board[3] + "[" + board[4] + "]" + board[5] + Format.end)
        print(" " + board[6] + "|" + board[7] + "|" + board[8])

    elif location == 5:

        print(" " + Format.underline + board[0] + "|" + board[1] + "|" + board[2] + Format.end)
        print(" " + Format.underline + board[3] + "|" + board[4] + "[" + board[5] + Format.end + "]")
        print(" " + board[6] + "|" + board[7] + "|" + board[8])

    elif location == 6:

        print(" " + Format.underline + board[0] + "|" + board[1] + "|" + board[2] + Format.end)
        print(" " + Format.underline + board[3] + "|" + board[4] + "|" + board[5] + Format.end)
        print("[" + board[6] + "]" + board[7] + "|" + board[8])

    elif location == 7:

        print(" " + Format.underline + board[0] + "|" + board[1] + "|" + board[2] + Format.end)
        print(" " + Format.underline + board[3] + "|" + board[4] + "|" + board[5] + Format.end)
        print(" " + board[6] + "[" + board[7] + "]" + board[8])

    elif location == 8:

        print(" " + Format.underline + board[0] + "|" + board[1] + "|" + board[2] + Format.end)
        print(" " + Format.underline + board[3] + "|" + board[4] + "|" + board[5] + Format.end)
        print(" " + board[6] + "|" + board[7] + "[" + board[8] + "]")


def change_turn(location):
    global game_state
    # checks if the spot is playable
    if TicTacToe.game_board[location] != " ":
        return
    # plays
    TicTacToe.game_board[location] = TicTacToe.turn_rotation
    # checks for game over
    if TicTacToe.check(TicTacToe.game_board) or TicTacToe.turn_number == 9:
        game_state = False
        return

    # changes the turn
    if TicTacToe.turn_rotation == "x":
        TicTacToe.turn_rotation = "o"
    else:
        TicTacToe.turn_rotation = "x"
    TicTacToe.turn_number += 1


# sets up a function to get the name of the keys pressed and put them in a queue
def on_keypress(e):
    keys_queue.put(e.name)


keys_queue = Queue()
keyboard.on_press(on_keypress)
print_board(TicTacToe.game_board, highlight)

# starts game
while game_state:
    temp = keys_queue.get()
    sleep(0.2)
    if temp == "esc":
        game_state = False
    elif temp == "space":
        change_turn(highlight)
    elif temp == "d" and highlight < 8:
        highlight += 1
    elif temp == "a" and highlight > 0:
        highlight -= 1
    elif temp == "w" and highlight > 2:
        highlight -= 3
    elif temp == "s" and highlight < 6:
        highlight += 3
    print_board(TicTacToe.game_board, highlight)

# checks to see why the game ended
print_board(TicTacToe.game_board, highlight)
if TicTacToe.check(TicTacToe.game_board):
    print(TicTacToe.turn_rotation + "'s won!")
else:
    print("Tie!")
