##### Day 16 #####
txt = open('day16.txt','r').read().strip().split('\n')

# [l to r, r to l, b to t, t to b] 1 if it's ever been in that d, 0 else.
d_next_c = {0:1,1:-1,2:0,3:0}
d_next_r = {0:0,1:0,2:-1,3:1}
bs_dict = {0:3,1:2,2:1,3:0} # \ 
s_dict = {0:2,1:3,2:0,3:1} # /

def inbounds(cell):
    global d_dict
    return cell[0] >= 0 and cell[1] >= 0 and cell[0] <= len(txt)-1 and cell[1] <= len(txt[0])-1

def lazerz(start_cell, d):
    S = [[start_cell,d]]
    d_dict = {(x,y):[0,0,0,0] for x in range(len(txt)) for y in range(len(txt[0]))}
    while S:
        (x,y), d = S.pop()
        if d_dict[(x,y)][d] == 0:
            d_dict[(x,y)][d] = 1
            if txt[x][y] == '.':
                next_cell = x + d_next_r[d], y + d_next_c[d]
                if inbounds(next_cell): # not boundary
                    S.append([(next_cell), d])
            elif txt[x][y] == '|':
                if d in [2,3]:
                    next_cell = x + d_next_r[d], y + d_next_c[d]
                    if inbounds(next_cell): # not boundary
                        S.append([(next_cell), d])
                else:
                    next_cell_t = x + d_next_r[2], y + d_next_c[2]
                    next_cell_b = x + d_next_r[3], y + d_next_c[3]
                    if inbounds(next_cell_t): # not boundary
                        S.append([(next_cell_t), 2])
                    if inbounds(next_cell_b): # not boundary
                        S.append([(next_cell_b), 3])
            elif txt[x][y] == '-':
                if d in [0,1]:
                    next_cell = x + d_next_r[d], y + d_next_c[d]
                    if inbounds(next_cell): # not boundary
                        S.append([(next_cell), d])
                else:
                    next_cell_r = x + d_next_r[0], y + d_next_c[0]
                    next_cell_l = x + d_next_r[1], y + d_next_c[1]
                    if inbounds(next_cell_r): # not boundary
                        S.append([(next_cell_r), 0])
                    if inbounds(next_cell_l): # not boundary
                        S.append([(next_cell_l), 1])
            elif txt[x][y] == '\\':
                next_cell = x + d_next_r[bs_dict[d]], y + d_next_c[bs_dict[d]]
                if inbounds(next_cell): # not boundary
                    S.append([(next_cell), bs_dict[d]])
            elif txt[x][y] == '/':
                next_cell = x + d_next_r[s_dict[d]], y + d_next_c[s_dict[d]]
                if inbounds(next_cell): # not boundary
                    S.append([(next_cell), s_dict[d]])
    return sum([any([x==1 for x in v]) for v in d_dict.values()])

print(lazers((0,0),0))

m = max([lazerz((r,0),0) for r in range(len(txt))])
m = max(m,max([lazerz((r,len(txt[0])-1),1) for r in range(len(txt))]))
m = max(m,max([lazerz((0,c),3) for c in range(len(txt[0]))]))
m = max(m,max([lazerz((len(txt)-1,c),2) for c in range(len(txt[0]))]))
print(m)