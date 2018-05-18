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


# hien thi vi tri hien tai
def show_pos():
    if all(direction == [-1, 0]):
        tmp = 'up'
    if all(direction == [0, -1]):
        tmp = 'left'
    if all(direction == [1, 0]):
        tmp = 'down'
    if all(direction == [0, 1]):
        tmp = 'right'
    print(pos, tmp)

# ham check phia truoc, trai, phai co phai loi ra khong
def check_out():
    return maze[pos] == 4

def check_if_pass():
    return imagine_maze[pos_imagine[0] + direction[0]][pos_imagine[1] + direction[1]]==-1

# phia truoc, ben trai, ben phai

# ham thuc hien viec di chuyen
def process(way,maze,pos):
    for i in way:
        print(str(i),end=' ')
        update_maze_to_tmp_maze()
        if i == 'f':
            pos += direction * 2
            pos_imagine+=direction * 2
            imagine_maze[pos_imagine[0]][pos_imagine[1]] = -1
        elif i == 'l':
            direction = left()
        elif i == 'r':
            direction = right()
        elif i=='b':
            pos-=direction * 2
        show_pos()
        update_tmp_maze()

# dieu khien robot chay
def go(road,maze,pos):
    process(road)
    if check_out():
        return True,''
    wall = check_wall()
    for i in np.random.choice(3, 3, False):
        if not wall[i]:
            process(name[i])
            if check_if_pass() and i==0:
                print('Come back because pass' + come_back(road))
                process(come_back(name[i]))
                print('End come back')
                continue
            t1,t2 = go('f',maze,pos)
            if t1 == True:
                return True, road +name[i]+ t2
    return False, None

def init():
    global imagine_maze,pos_imagine,pos,direction,tmp_maze
    imagine_maze=np.zeros((30,30))
    direction = np.array([-1, 0])
    pos_imagine=np.array([15,15])
    pos = np.argwhere(maze == 9)[0]
    tmp_maze = np.array(maze)



all_step=''
init()
show(maze)
show_pos()
name = ['', 'l', 'r', 'rr']
start=np.argwhere(maze==2)[0]
wall = np.append(check_wall(), maze[pos[0] + back()[0]][pos[1] + back()[1]] == -1)

if any(np.append(check_out(),maze[pos[0] + back()[0]][pos[1] + back()[1]] == 3)):
    exit()

for i in np.random.choice(4, 4, False):
    if not wall[i]:
        tmp = name[i] + 'f'
        t1, t2 = go(tmp,tmp_maze,start)
        if t1 == True:
            print(t2)
            break

# fig, ax = plt.subplots(figsize=(5, 8))
#
# def update(i):
#     process(all_step[i])
#     ax.imshow(tmp_maze*5)
#     ax.set_title("Step: {}".format(i), fontsize=20)
#     ax.set_axis_off()


# anim = FuncAnimation(fig, update, frames=range(len(all_step)), interval=800,init_func=init)
# anim.save('step.gif', dpi=80)
# plt.close()

