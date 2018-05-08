from generate import maze
import numpy as np


pos=np.argwhere(maze==2)[0]
end=np.argwhere(maze==3)[0]
treasure=np.argwhere(maze==4)

direction=[0,1]

def left():
	if direction==[0,-1]:
		return [-1,0]
	if direction==[-1,0]:
		return [0,1]
	if direction==[0,1]:
		return [1,0]
	if direction==[1,0]:
		return [0,-1]

def right():
	if direction==[0,-1]:
		return [1,0]
	if direction==[1,0]:
		return [0,1]
	if direction==[0,1]:
		return [-1,0]
	if direction==[-1,0]:
		return [0,-1]	

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



