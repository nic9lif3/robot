from generate import maze,show
import numpy as np

global pos, direction,tmp_maze
pos = np.argwhere(maze == 2)[0]
end = np.argwhere(maze == 3)[0]
treasure = np.argwhere(maze == 4)
name = ['f', 'l', 'r', 'b']
direction = np.array([-1, 0])
tmp_maze=maze

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
    if all(direction == [0, 1]):
        return np.array([-1, 0])


# ham xac dinh toa do phia sau
def back():
    if all(direction == [-1, 0]):
        return np.array([1, 0])
    if all(direction == [0, 1]):
        return np.array([0, -1])
    if all(direction == [1, 0]):
        return np.array([-1, 0])
    if all(direction == [0, 1]):
        return np.array([0, -1])


# ham de tao ra con duong di nguoc lai dua tren con duong da co
def come_back(road):
    way = 'll'
    for i in road[::-1]:
        if i == 'f':
            way += 'f';
        if i == 'l':
            way += 'r'
        if i == 'r':
            way += 'l'
    return way


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
    global pos, direction,tmp_maze
    for i in way:
        if i == 'f':
            tmp_maze[pos[0]][pos[1]]=maze[pos[0]][pos[1]]
            pos += direction * 2
            tmp_maze[pos[0]][pos[1]]=4
        if i == 'l':
            direction = left()
        if i == 'r':
            direction = right()


# dieu khien robot chay
def go(road):
    global pos
    process('g')

    road += name[0]
    f, l, r = check_out()
    if f:
        road += name[0]
        return True, road
    if l:
        road += name[1]
        return True, road
    if r:
        road += name[2]
        return True, road
    wall = check_wall()
    for i in np.random.choice(3, 3, False):
        if wall[i]:
            t1, t2 = go([name[wall[i]]])
            if t1 == True:
                return True, road + t2
    process(come_back(road))
    return False, None


wall = np.array(
    [maze[pos[0] + direction[0]][pos[1] + direction[1]], maze[pos[0] + left()[0]][pos[1] + left()[1]], maze[pos[0]
                                                                                                            + right()[
                                                                                                                0]][
        pos[1] + right()[1]], maze[pos[0] + back()[0]][pos[1] + back()[1]]]) == -1

for i in np.random.choice(4, 4, False):
    if not wall[i]:
        if i==0:
            tmp=''
        if i==3:
            tmp='rr'
        t1, t2 = go(name[wall[i]])
        if t1 == True:
            print(t2)
            break
