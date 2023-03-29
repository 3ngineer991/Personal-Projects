import time

maze = [['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
        ['#', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
        ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', '#', '#', ' ', '#', '#', '#', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#']]


def sleep(secs):
    curr_time = time.time()
    while curr_time + secs >= time.time():
        continue


def print_board():
    for i in range(70):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for i in maze:
        for j in i:
            print(j, end=" ")
        print()


def show_posi(indexa, indexb):
    temp = maze[indexa][indexb]
    maze[indexa][indexb] = '*'
    print_board()
    maze[indexa][indexb] = temp


def maze_algor(direction, indexa, indexb):
    show_posi(indexa, indexb)
    sleep(0.4)
    if len(maze) - 1 == indexa:
        maze[indexa][indexb] = '*'
        return True
    if len(maze[indexa]) - 1 == indexb or indexb == 0:
        maze[indexa][indexb] = '*'
        return True

    # direction = down
    if direction % 4 == 2:
        # check forward
        if maze[indexa + 1][indexb] == ' ':
            if maze_algor(direction, indexa + 1, indexb):
                maze[indexa][indexb] = '*'
                return True
        # check right
        if maze[indexa][indexb - 1] == ' ':
            if maze_algor(direction + 1, indexa, indexb - 1):
                maze[indexa][indexb] = '*'
                return True
        # check left
        if maze[indexa][indexb + 1] == ' ':
            if maze_algor(direction - 1, indexa, indexb + 1):
                maze[indexa][indexb] = '*'
                return True
        else:
            return False
    # direction = right
    elif direction % 4 == 1:
        # check forward
        if maze[indexa][indexb + 1] == ' ':
            if maze_algor(direction, indexa, indexb + 1):
                maze[indexa][indexb] = '*'
                return True
        # check right
        if maze[indexa + 1][indexb] == ' ':
            if maze_algor(direction + 1, indexa + 1, indexb):
                maze[indexa][indexb] = '*'
                return True
        # check left
        if maze[indexa - 1][indexb] == ' ':
            if maze_algor(direction - 1, indexa - 1, indexb):
                maze[indexa][indexb] = '*'
                return True
        else:
            return False
    # direction = up
    elif direction % 4 == 0:
        # check forward
        if maze[indexa - 1][indexb] == ' ':
            if maze_algor(direction, indexa - 1, indexb):
                maze[indexa][indexb] = '*'
                return True
        # check right
        if maze[indexa][indexb + 1] == ' ':
            if maze_algor(direction + 1, indexa, indexb + 1):
                maze[indexa][indexb] = '*'
                return True
        # check left
        if maze[indexa][indexb - 1] == ' ':
            if maze_algor(direction - 1, indexa, indexb - 1):
                maze[indexa][indexb] = '*'
                return True
        else:
            return False
    # direction = left
    elif direction % 4 == 3:
        # check forward
        if maze[indexa][indexb - 1] == ' ':
            if maze_algor(direction, indexa, indexb - 1):
                maze[indexa][indexb] = '*'
                return True
        # check right
        if maze[indexa - 1][indexb] == ' ':
            if maze_algor(direction + 1, indexa - 1, indexb):
                maze[indexa][indexb] = '*'
                return True
        # check left
        if maze[indexa + 1][indexb] == ' ':
            if maze_algor(direction - 1, indexa + 1, indexb):
                maze[indexa][indexb] = '*'
                return True
        else:
            return False


if not maze_algor(2, 0, 1):
    print("No Exit")

print_board()
