from generate import maze, show
import numpy as np
import time
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

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
    way = ''
    for i in road[::-1]:
        if i == 'f':
            way += 'b'
        if i == 'l':
            way += 'r'
        if i == 'r':
            way += 'l'
    return  way


# cap nhat gia tri maze cho tmp_maze
def update_maze_to_tmp_maze():
    global tmp_maze
    tmp_maze[pos[0]][pos[1]] = '0'
    if pos[0] + direction[0] != 0 and pos[0] + direction[0] != 10 and pos[1] + direction[1] != 0 and pos[1] + direction[1] != 10:
        tmp_maze[pos[0] + direction[0] * 2][pos[1] + direction[1] * 2] = 0
    # if pos[0] + left()[0] != 0 and pos[0] + left()[0] != 10 and pos[1] + left()[1] != 0 and pos[1] + left()[1] != 10:
    #     tmp_maze[pos[0] + left()[0] * 2][pos[1] + left()[1] * 2] = 0
    # if pos[0] + right()[0] != 0 and pos[0] + right()[0] != 10 and pos[1] + right()[1] != 0 and pos[1] + right()[1] != 10:
    #     tmp_maze[pos[0] + right()[0] * 2][pos[1] + right()[1] * 2] = 0
    # if pos[0] + back()[0] != 0 and pos[0] + back()[0] != 10 and pos[1] + back()[1] != 0 and pos[1] + back()[1] != 10:
    #     tmp_maze[pos[0] + back()[0] * 2][pos[1] + back()[1] * 2] = 0


# cap nhat gia tri moi cho tmp_maze
def update_tmp_maze():
    global tmp_maze
    tmp_maze[pos[0]][pos[1]] = 9
    # show(tmp_maze)
    if all(direction == [-1, 0]):
        tmp='up'
    if all(direction == [0, -1]):
        tmp='left'
    if all(direction == [1, 0]):
        tmp='down'
    if all(direction == [0, 1]):
        tmp='right'
    print(pos,tmp)
    if pos[0] + direction[0] != 0 and pos[0] + direction[0] != 10 and pos[1] + direction[1] != 0 and pos[1] + direction[1] != 10:
        tmp_maze[pos[0] + direction[0] * 2][pos[1] + direction[1] * 2] = 5
    # if pos[0] + left()[0] != 0 and pos[0] + left()[0] != 10 and pos[1] + left()[1] != 0 and pos[1] + left()[1] != 10:
    #     tmp_maze[pos[0] + left()[0] * 2][pos[1] + left()[1] * 2] = 6
    # if pos[0] + right()[0] != 0 and pos[0] + right()[0] != 10 and pos[1] + right()[1] != 0 and pos[1] + right()[1] != 10:
    #     tmp_maze[pos[0] + right()[0] * 2][pos[1] + right()[1] * 2] = 7
    # if pos[0] + back()[0] != 0 and pos[0] + back()[0] != 10 and pos[1] + back()[1] != 0 and pos[1] + back()[1] != 10:
    #     tmp_maze[pos[0] + back()[0] * 2][pos[1] + back()[1] * 2] = 8

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
    global pos, direction, tmp_maze,all_step
    for i in way:
        print(i,end=' ')
        update_maze_to_tmp_maze()
        if i == 'f':
            pos += direction * 2
        elif i == 'l':
            direction = left()
        elif i == 'r':
            direction = right()
        elif i=='b':
            pos-=direction * 2
        update_tmp_maze()
        all_step+=i

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
        process(name[1])
        return True, road
    if r:
        road += name[2] + 'f'
        process(name[2])
        return True, road
    wall = check_wall()
    for i in np.random.choice(3, 3, False):
        if not wall[i]:
            t1, t2 = go(name[i] + 'f')
            if t1 == True:
                return True, road + t2
    print('Come back '+come_back(road))
    process(come_back(road))
    print('End come back')
    return False, None


global pos, direction, tmp_maze,all_step,imagine_maze
all_step=''
imagine_maze=np.zeros((21,21))
pos = np.argwhere(maze == 9)[0]
end = np.argwhere(maze == 3)[0]
name = ['', 'l', 'r', 'rr']
direction = np.array([-1, 0])
tmp_maze = np.array(maze)
show(maze)
wall = np.append(check_wall(), maze[pos[0] + back()[0]][pos[1] + back()[1]] == -1)

if any(np.append(check_out(),maze[pos[0] + back()[0]][pos[1] + back()[1]] == 3)):
    exit()

for i in np.random.choice(4, 4, False):
    if not wall[i]:
        tmp = name[i] + 'f'
        t1, t2 = go(tmp)
        if t1 == True:
            print(t2)
            break

tmp_maze=maze
pos = np.argwhere(maze == 9)[0]
direction = np.array([-1, 0])
fig, ax = plt.subplots(figsize=(5, 8))

def update(i):
    process(all_step[i])
    ax.imshow(tmp_maze*5)
    ax.set_title("Step: {}".format(i), fontsize=20)
    ax.set_axis_off()

def init():
    pass
anim = FuncAnimation(fig, update, frames=range(len(all_step)), interval=800,init_func=init)
anim.save('step.gif', dpi=80)
plt.close()

