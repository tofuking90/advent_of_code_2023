##### Day 21 #####
txt = open('day21.txt','r').read().strip().split('\n')

s_loc = [x.find('S') for x in txt]
s_pos = ([ind for ind, v in zip(range(len(txt)),s_loc) if v > 0][0],max(s_loc))

def inbounds(pos, nrs):
    return pos[0] >= 0 and pos[0] <= nrs-1 and pos[1] >= 0 and pos[1] <= nrs-1

def grid_bfs(txt, num_steps):
    nrs = len(txt)
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    cur_locs = [(int((nrs-1)/2), int((nrs-1)/2))]
    for step in range(num_steps):
        if step % 10 == 0:
            print(step)
        next_locs = []
        for loc in cur_locs:
            for dr in dirs:
                new_pos = (loc[0] + dr[0], loc[1] + dr[1])
                if inbounds(new_pos, nrs) and txt[new_pos[0]][new_pos[1]] != '#':
                    next_locs.append(new_pos)
        cur_locs = set(next_locs)
    return len(cur_locs)

grid_bfs(txt, 64)
##### b
def rep_grid(width):
    x = []
    for r in txt:
        x.append(r*width)
    x0 = x.copy()
    for i in range(width-1):
        x.extend(x0)
    return x

txt = open('day21.txt','r').read().strip().split('\n')
width = 9
txtw = rep_grid(width)
num_steps = int(65 + 131*(width-1)/2)
print(num_steps)
grid_bfs(txtw, num_steps)

target_width = (26501365-65)/131 * 2 + 1
404601
1: 3868
5: 95262
9: 308232
 
import numpy as np
x = np.linalg.solve(np.array([[x*x, x, 1] for x in [1,5,9]]),np.array([3868, 95262, 308232]))
print(target_width**2*x[0] + target_width*x[1] + x[2])
