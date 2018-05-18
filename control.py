import physic,sys,numpy as np
physic.change_speed_left(30)
physic.change_speed_right(30)
N = 250
E = 166
W = 360
S = 83
G=np.array([N,E,S,W])
road=sys.argv[1]
physic.reset_compass()
degree=physic.compass()
degree=degree['degree'] + degree['minute'] / 60
g=np.argmin(np.abs(G-degree))

for i in road:
    if i=='f':
        physic.hieuchinh(G[g])
        physic.go(G[g])
    elif i=='r':
        physic.turn_right_degree(90)
        g=(g+1)%4
    elif i=='l':
        physic.turn_left_degree(90)
        g=(g-1)%4