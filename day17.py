##### Day 17 #####
import numpy as np
import heapq as hq
mat = open('day17.txt','r').read().strip().split('\n')

def inbounds(cell):
    return cell[0] >= 0 and cell[0] <= len(mat)-1 and cell[1] >= 0 and cell[1] <= len(mat[0])-1

def d17(mat, lb, ub):
    dirs = {0:[0,1], 1:[0,-1], 2:[1,0], 3:[-1,0]}# l-r, r-l, t-b, b-t
    opp_dir = {0:1, 1:0, 2:3, 3:2}
    h = [[int(mat[0][1]),(0,1),0,1],[int(mat[1][0]),(1,0),2,1]]
    mem = {tuple(x[1:]):x[0] for x in h}
    hq.heapify(h)
    while h:
        dist, cur_cell, prev_dir, prev_ct = hq.heappop(h)
        for dr in dirs.keys():
            if prev_dir != opp_dir[dr]:
                if (dr != prev_dir and prev_ct >= lb) or (dr == prev_dir and prev_ct < ub):
                    next_cell = (cur_cell[0] + dirs[dr][0], cur_cell[1] + dirs[dr][1])
                    if next_cell[0] == len(mat)-1 and next_cell[1] == len(mat[0])-1:
                        return dist + int(mat[next_cell[0]][next_cell[1]])
                    if inbounds(next_cell):
                        next_ct = 1 if dr != prev_dir else prev_ct + 1
                        next_tup = (next_cell, dr, next_ct)
                        next_dist = dist + int(mat[next_cell[0]][next_cell[1]])
                        if (next_tup not in mem) or (mem[next_tup] > next_dist):
                            hq.heappush(h, [next_dist, next_cell, dr, next_ct])
                            mem[next_tup] = next_dist
    return 'gg'

d17(mat,0,3)
d17(mat,4,10)
