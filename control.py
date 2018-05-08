from generate import maze
import numpy as np


start=np.argwhere(maze==2)[0]
end=np.argwhere(maze==3)[0]
treasure=np.argwhere(maze==4)

direction=np.array([0,0])
direction[np.random.choice(2,1)]=np.random.choice([-1,1],1)
print(direction)
