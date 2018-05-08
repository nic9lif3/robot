from generate import maze
import numpy as np


pos=np.argwhere(maze==2)[0]
end=np.argwhere(maze==3)[0]
treasure=np.argwhere(maze==4)

direction=np.array([-1,0])

def left():
	if all(direction==[-1,0]):
		return np.array([0,-1])
	if all(direction==[0,-1]):
		return np.array([1,0])
	if all(direction==[1,0]):
		return np.array([0,1])
	if all(direction==[0,1]):
		return np.array([-1,0])

def right():
	if all(direction==[-1,0]):
		return np.array([0,1])
	if all(direction==[0,1]):
		return np.array([1,0])
	if all(direction==[1,0]):
		return np.array([0,-1])
	if all(direction==[0,1]):
		return np.array([-1,0])

def back_to_check_point(road):
	way='ll'
	for i in road[::-1]:
		if i=='g':
			way+='g';
		if i=='l':
			way+='r'
		if i=='r':
			way+=l
	return way

def check_wall():
	return np.array([maze[pos[0]+direction[0]][pos[1]+direction[1]],maze[pos[0]+left()[0]][pos[1]+left()[1]],maze[pos[0]+right()[0]][pos[1]+right()[1]]])==-1 
	# phia truoc, ben trai, ben phai
def check_out():
	return np.array([maze[pos[0]+direction[0]][pos[1]+direction[1]],maze[pos[0]+left()[0]][pos[1]+left()[1]],maze[pos[0]+right()[0]][pos[1]+right()[1]]])==3
	# phia truoc, ben trai, ben phai

print(check_wall())
print(check_out())

def go(first_turn=None):
	pass
