import numpy as np


def generate():
    maze = np.zeros((11, 11)) - 2
    # chon bo tuong bao
    maze[0, :] = -1
    maze[10, :] = -1
    maze[:, 0] = -1
    maze[:, 10] = -1

    # chon o co the di
    maze[1:10:2, 1:10:2] = 0

    # chon cac duong noi giua cac o
    maze[1:10:2, 2:9:2] = 1
    maze[2:9:2, 1:10:2] = 1

    tmp = np.random.choice(range(1, 10, 2), (5, 2))
    # chon diem bat dau
    start = tmp[0]
    maze[start[0]][start[1]] = 2

    # chon kho bau:
    treasure = tmp[1:4]
    for x in treasure:
        maze[x[0]][x[1]] = 3
    # chon diem ket thuc
    end = tmp[4]
    door = np.random.randint(2)
    end[door] = np.random.choice([1, 9])
    maze[end[0]][end[1]] = 4

    # chon tuong chan
    a = np.argwhere(maze == 1)
    inwall = np.random.choice(a.shape[0], 10)
    for x in inwall:
        maze[a[x][0]][a[x][1]] = -1

    return maze


def test(maze):
    start = np.argwhere(maze == 9)[0]
    end = np.argwhere(maze == 3)[0]
    if maze[end[0]][end[1] - 1] + maze[end[0]][end[1] + 1] + maze[end[0] + 1][end[1]] + maze[end[0] - 1][end[1]] == -4:
        return False
    if maze[start[0]][start[1] - 1] + maze[start[0]][start[1] + 1] + maze[start[0] + 1][start[1]] + maze[start[0] - 1][
        start[1]] == -4:
        return False
    return True


def show(maze):
    print(' ' + ''.join(str(i)[0] for i in range(11)))
    for i in range(maze.shape[0]):
        print(str(i)[0], end='')
        for j in range(maze.shape[1]):
            if maze[i][j] == -2:
                tmp = ' '
            elif maze[i][j] == -1:
                tmp = 'x'
            elif maze[i][j] == 0:
                tmp = '0'
            elif maze[i][j] == 1:
                if j % 2 == 0:
                    tmp = '-'
                if i % 2 == 0:
                    tmp = '|'
            elif maze[i][j] == 9:
                tmp = 'i'
            elif maze[i][j] == 3:
                tmp = 'o'
            # forward
            elif maze[i][j] == 5:
                tmp = 'f'
            # left
            elif maze[i][j] == 6:
                tmp = 'l'
            # right
            elif maze[i][j] == 7:
                tmp = 'r'
            # back
            elif maze[i][j] == 8:
                tmp = 'b'
            print(tmp, end='')
        print()


while True:
    maze = generate()
    if test(maze):
        break
