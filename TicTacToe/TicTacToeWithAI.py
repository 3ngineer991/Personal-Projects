from queue import Queue

import time
import keyboard
import TicTacToeBot


class Format:
    end = '\033[0m'
    underline = '\033[4m'


game_board = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " "]

turn_rotation = 'x'
turn_number = 1
game_state = True
winner = ""
highlight = 4


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


def sleep(secs):
    curr_time = time.time()
    while curr_time + secs >= time.time():
        continue


# prints board with the location of the curser
def print_board(board, location):
    for i in range(50):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Welcome to 1 player Tic Tac Toe")
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


# plays in the given location, checks for a win, bot plays, and checks for a win again
def change_turn(location):
    global game_state
    global turn_number
    global turn_rotation
    global game_board
    global winner
    # checks if the spot is playable
    if game_board[location] != " ":
        return
    # plays
    game_board[location] = turn_rotation
    # checks for game over
    if check(game_board) or turn_number == 9:
        game_state = False
        winner = "x"
        return

    # bot plays
    turn_number += 1
    bot_space = TicTacToeBot.take_turn(game_board, turn_number)
    if bot_space == -1:
        winner = "x"
    game_board[bot_space] = "o"
    if check(game_board):
        game_state = False
        winner = "o"
        return
    turn_number += 1


# sets up a function to get the name of the keys pressed and put them in a queue
def on_keypress(e):
    keys_queue.put(e.name)


keys_queue = Queue()
keyboard.on_press(on_keypress)
print_board(game_board, highlight)

TicTacToeBot.initiate()

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
    print_board(game_board, highlight)

# checks to see why the game ended
print_board(game_board, highlight)
if check(game_board):
    print(winner + "'s won!")
    if winner == "x":
        TicTacToeBot.punish()
    else:
        TicTacToeBot.reward()
else:
    print("Tie!")

TicTacToeBot.clean_up()
