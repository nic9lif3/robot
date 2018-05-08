import numpy as np
def generate():
	maze=np.zeros((11,11))-2
	# chon o co the di
	maze[1::2,1::2]=0
	# chon cac duong noi giua cac o
	maze[1::2,2::2]=1
	maze[2::2,1::2]=1
	# chon bo tuong bao
	maze[0,:]=-1
	maze[10,:]=-1
	maze[:,0]=-1
	maze[:,10]=-1
	start=np.random.choice(range(1,10,2),[4,2])
	
	#chon kho bau:
	maze[start[1][0]][start[1][1]]=4
	maze[start[2][0]][start[2][1]]=4
	maze[start[3][0]][start[3][1]]=4
	# chon diem bat dau
	maze[start[0][0]][start[0][1]]=2
	# chon diem ket thuc
	end=np.zeros(2)
	end=np.random.choice([0,1,3,5,7,9,10],2)
	door=np.random.randint(2)
	end[door]=np.random.choice([0,10])
	#chon tuong chan
	a=np.argwhere(maze==1)
	inwall=np.random.choice(a.shape[0],8)
	for x in inwall:
		maze[a[x][0]][a[x][1]]=-1
	maze[end[0]][end[1]]=3

	return maze

def test(maze):
	start=np.argwhere(maze==2)[0]
	end=np.argwhere(maze==3)[0]
	if end[0]==end[1] or abs(end[0]-end[1])==10:
		return False
	else:
		if end[0]==0:
			end[0]+=1
			if maze[end[0]][end[1]-1]+maze[end[0]+1][end[1]]+maze[end[0]][end[1]+1]==-3:
				return False
		if end[0]==10:
			end[0]-=1
			if maze[end[0]][end[1]-1]+maze[end[0]-1][end[1]]+maze[end[0]][end[1]+1]==-3:
				return False
		if end[1]==0:
			end[1]+=1
			if maze[end[0]+1][end[1]]+maze[end[0]-1][end[1]]+maze[end[0]][end[1]+1]==-3:
				return False
		if end[1]==10:
			end[1]-=1
			if maze[end[0]][end[1]-1]+maze[end[0]-1][end[1]]+maze[end[0]+1][end[1]]==-3:
				return False
	if maze[start[0]-1][start[1]]+maze[start[0]][start[1]-1]+maze[start[0]+1][start[1]]+maze[start[0]][start[1]+1]==-4:
		return False
	return True
def show(maze):
	for i in range(maze.shape[0]):
		for j in range(maze.shape[1]):
			if maze[i][j]==-2:
				tmp=' '
			elif maze[i][j]==-1:
				tmp='x'
			elif maze[i][j]==0:
				tmp='0'
			elif maze[i][j]==1:
				if j%2==0:
					tmp='-'
				if i%2==0:
					tmp='|'
			elif maze[i][j]==2:
				tmp='i'
			elif maze[i][j]==3:
				tmp='o'
			elif maze[i][j]==4:
				tmp='t'
			print(tmp,end='')
		print()

while True:
	maze=generate()
	if test(maze):
		break
show(maze)
