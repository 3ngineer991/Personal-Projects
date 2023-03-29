game_board = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " "]

turn_rotation = 'x'
turn_number = 1


def turn(player):
    while True:
        while True:
            try:
                space = input("Player " + player + "'s turn (to play type in 2 numbers for example to play 2 across "
                              "and 3 down you would type 2 3)")

                temp = space.split(" ")

                play = (int(temp[0]) * 3 - 1) - (3 - int(temp[1]))
                break
            except:
                print("incorrect format")

        if game_board[play] == ' ':
            game_board[play] = player
            return
        else:
            print("Space has already been played")


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


if __name__ == "__main__":

    print("Welcome to Tic Tac Toe\nrequires two players")

    while True:
        print("|" + str(game_board[0]) + " " + str(game_board[1]) + " " + str(game_board[2]) + "|\n|" +
              str(game_board[3]) + " " + str(game_board[4]) + " " + str(game_board[5]) + "|\n|" +
              str(game_board[6]) + " " + str(game_board[7]) + " " + str(game_board[8]) + "|")
        turn(turn_rotation)
        if check(game_board):
            print("|" + str(game_board[0]) + " " + str(game_board[1]) + " " + str(game_board[2]) + "|\n|" +
                  str(game_board[3]) + " " + str(game_board[4]) + " " + str(game_board[5]) + "|\n|" +
                  str(game_board[6]) + " " + str(game_board[7]) + " " + str(game_board[8]) + "|")
            print(turn_rotation + "'s wins!")
            break

        turn_rotation = 'o' if turn_rotation == 'x' else 'x'

        if turn_number == 9:
            print("Ya both lost")
            break

        turn_number += 1
