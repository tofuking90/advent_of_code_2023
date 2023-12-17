##### Day 17 #####
import numpy as np
import heapq as hq
mat = open('day17.txt','r').read().strip().split('\n')
# mat = ['2413432311323','3215453535623','3255245654254','3446585845452','4546657867536','1438598798454','4457876987766','3637877979653','4654967986887','4564679986453','1224686865563','2546548887735','4322674655533']

def inbounds(cell):
    return cell[0] >= 0 and cell[0] <= len(mat)-1 and cell[1] >= 0 and cell[1] <= len(mat[0])-1

dirs = {0:[0,1], 1:[0,-1], 2:[1,0], 3:[-1,0]}# l-r, r-l, t-b, b-t
opp_dir = {0:1, 1:0, 2:3, 3:2}
h = [[int(mat[0][1]),(0,1),0,1],[int(mat[1][0]),(1,0),2,1]]
mem = {tuple(x[1:]):x[0] for x in h}
mins = []
ct = 0
# h_dict = {v[1:]:v[0] for v in h}
hq.heapify(h)
while h:# and ct <= 20:
    # print(len(h))
    dist, cur_cell, prev_dir, prev_ct = hq.heappop(h)
    # print(1,dist, cur_cell, prev_dir, prev_ct)
    # print(cur_cell)
    for dr in dirs.keys():
        # print(dr)
        if (dr != prev_dir or prev_ct < 3) and prev_dir != opp_dir[dr]:
            next_cell = (cur_cell[0] + dirs[dr][0], cur_cell[1] + dirs[dr][1])
            # print(10)
            if next_cell[0] == len(mat)-1 and next_cell[1] == len(mat[0])-1:
                print(dist + int(mat[next_cell[0]][next_cell[1]]))
                h = []
                break
            if inbounds(next_cell):
                next_ct = 1 if dr != prev_dir else prev_ct + 1
                next_tup = (next_cell, dr, next_ct)
                next_dist = dist + int(mat[next_cell[0]][next_cell[1]])
                if (next_tup not in mem) or (mem[next_tup] >= next_dist):
                    hq.heappush(h, [next_dist, next_cell, dr, next_ct])
                    mem[next_tup] = next_dist