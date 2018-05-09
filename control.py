from generate import maze, show
import numpy as np
import time


# ham xac dinh toa do ben trai
def left():
    if all(direction == [-1, 0]):
        return np.array([0, -1])
    if all(direction == [0, -1]):
        return np.array([1, 0])
    if all(direction == [1, 0]):
        return np.array([0, 1])
    if all(direction == [0, 1]):
        return np.array([-1, 0])


# ham xac dinh toa do ben phai
def right():
    if all(direction == [-1, 0]):
        return np.array([0, 1])
    if all(direction == [0, 1]):
        return np.array([1, 0])
    if all(direction == [1, 0]):
        return np.array([0, -1])
    if all(direction == [0, -1]):
        return np.array([-1, 0])


# ham xac dinh toa do phia sau
def back():
    if all(direction == [-1, 0]):
        return np.array([1, 0])
    if all(direction == [1, 0]):
        return np.array([-1, 0])
    if all(direction == [0, -1]):
        return np.array([0, 1])
    if all(direction == [0, 1]):
        return np.array([0, -1])


# ham de tao ra con duong di nguoc lai dua tren con duong da co
def come_back(road):
    way = 'll'+road[::-1]
    # for i in road[::-1]:
    #     if i == 'f':
    #         way += 'f';
    #     if i == 'l':
    #         way += 'r'
    #     if i == 'r':
    #         way += 'l'
    return  'll'+road[::-1]


# cap nhat gia tri maze cho tmp_maze
def update_maze_to_tmp_maze():
    global tmp_maze
    tmp_maze[pos[0]][pos[1]] = '0'
    if pos[0] + direction[0] != 0 and pos[0] + direction[0] != 10 and pos[1] + direction[1] != 0 and pos[1] + direction[1] != 10:
        tmp_maze[pos[0] + direction[0] * 2][pos[1] + direction[1] * 2] = 0
    if pos[0] + left()[0] != 0 and pos[0] + left()[0] != 10 and pos[1] + left()[1] != 0 and pos[1] + left()[1] != 10:
        tmp_maze[pos[0] + left()[0] * 2][pos[1] + left()[1] * 2] = 0
    if pos[0] + right()[0] != 0 and pos[0] + right()[0] != 10 and pos[1] + right()[1] != 0 and pos[1] + right()[1] != 10:
        tmp_maze[pos[0] + right()[0] * 2][pos[1] + right()[1] * 2] = 0
    if pos[0] + back()[0] != 0 and pos[0] + back()[0] != 10 and pos[1] + back()[1] != 0 and pos[1] + back()[1] != 10:
        tmp_maze[pos[0] + back()[0] * 2][pos[1] + back()[1] * 2] = 0


# cap nhat gia tri moi cho tmp_maze
def update_tmp_maze():
    global tmp_maze
    tmp_maze[pos[0]][pos[1]] = 2
    # show(tmp_maze)
    print(pos,end=' ')
    if pos[0] + direction[0] != 0 and pos[0] + direction[0] != 10 and pos[1] + direction[1] != 0 and pos[1] + direction[1] != 10:
        tmp_maze[pos[0] + direction[0] * 2][pos[1] + direction[1] * 2] = 5
    if pos[0] + left()[0] != 0 and pos[0] + left()[0] != 10 and pos[1] + left()[1] != 0 and pos[1] + left()[1] != 10:
        tmp_maze[pos[0] + left()[0] * 2][pos[1] + left()[1] * 2] = 6
    if pos[0] + right()[0] != 0 and pos[0] + right()[0] != 10 and pos[1] + right()[1] != 0 and pos[1] + right()[1] != 10:
        tmp_maze[pos[0] + right()[0] * 2][pos[1] + right()[1] * 2] = 7
    if pos[0] + back()[0] != 0 and pos[0] + back()[0] != 10 and pos[1] + back()[1] != 0 and pos[1] + back()[1] != 10:
        tmp_maze[pos[0] + back()[0] * 2][pos[1] + back()[1] * 2] = 8

# ham check phia truoc, trai, phai co phai duong khong
def check_wall():
    return np.array([maze[pos[0] + direction[0]][pos[1] + direction[1]], maze[pos[0] + left()[0]][pos[1] + left()[1]],
                     maze[pos[0] + right()[0]][pos[1] + right()[1]]]) == -1


# phia truoc, ben trai, ben phai

# ham check phia truoc, trai, phai co phai loi ra khong
def check_out():
    return np.array([maze[pos[0] + direction[0]][pos[1] + direction[1]], maze[pos[0] + left()[0]][pos[1] + left()[1]],
                     maze[pos[0] + right()[0]][pos[1] + right()[1]]]) == 3


# phia truoc, ben trai, ben phai

# ham thuc hien viec di chuyen
def process(way):
    global pos, direction, tmp_maze
    for i in way:
        update_maze_to_tmp_maze()
        if i == 'f':
            pos += direction * 2
        if i == 'l':
            direction = left()
        if i == 'r':
            direction = right()
        update_tmp_maze()
        print(i)
        # print('\n' * 10)
        # show(tmp_maze)


# dieu khien robot chay
def go(road):
    global pos
    process(road)
    f, l, r = check_out()
    if f:
        road += 'f'
        return True, road
    if l:
        road += name[1] + 'f'
        return True, road
    if r:
        road += name[2] + 'f'
        return True, road
    wall = check_wall()
    for i in np.random.choice(3, 3, False):
        if not wall[i]:
            t1, t2 = go(name[i] + 'f')
            if t1 == True:
                return True, road + t2
    process(come_back(road))
    return False, None


global pos, direction, tmp_maze
pos = np.argwhere(maze == 2)[0]
end = np.argwhere(maze == 3)[0]
treasure = np.argwhere(maze == 4)
name = ['', 'l', 'r', 'rr']
direction = np.array([-1, 0])
tmp_maze = maze
show(maze)
wall = np.append(check_wall(), maze[pos[0] + back()[0]][pos[1] + back()[1]] == -1)

if any(check_out()):
    exit()

for i in np.random.choice(4, 4, False):
    if not wall[i]:
        tmp = name[i] + 'f'
        t1, t2 = go(tmp)
        if t1 == True:
            print(t2)
            break

# tmp_maze=maze
# for i in t2:
#     process(i)
#     print('\n' * 10)
#     show(tmp_maze)


