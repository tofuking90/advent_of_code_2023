##### Day 10 #####
import re
import numpy as np

txt = []
with open("day10.txt","r") as f:
    for line in f:
        txt.append(line.rstrip('\n'))

s_pos = np.array([-1,-1])
for line, ind in zip(txt,range(len(txt))):
    s = line.find('S')
    if s > -1:
        s_pos = np.array([ind, s])

cur_pos = s_pos
prev_pos = np.array([-1,-1])
cur_sym = 'S'
next_dict1 = {'S':np.array([0,1]),'F':np.array([1,0]), 'L':np.array([-1,0]),'J':np.array([-1,0]),'7':np.array([1,0]),'|':np.array([1,0]),'-':np.array([0,-1])}
next_dict2 = {'S':np.array([1,0]),'F':np.array([0,1]), 'L':np.array([0,1]),'J':np.array([0,-1]),'7':np.array([0,-1]),'|':np.array([-1,0]),'-':np.array([0,1])}
c = 0
mapdot = [['.' for x in range(len(txt[0]))] for x in range(len(txt))]
while True:
    # print(cur_sym)
    next_pos = cur_pos + next_dict1[cur_sym]
    if all(next_pos == prev_pos):
        next_pos = cur_pos + next_dict2[cur_sym]
    prev_pos = cur_pos
    cur_pos = next_pos
    cur_sym = txt[cur_pos[0]][cur_pos[1]]
    mapdot[cur_pos[0]][cur_pos[1]] = cur_sym
    c += 1
    if cur_sym == 'S':
        mapdot[cur_pos[0]][cur_pos[1]] = '-'
        break

print(int(c/2))

#b
b = 0
matchy = {'F':'7','L':'J'}
for line in mapdot:
    out = True
    stay = False
    last_turn = 'X'
    for n in line:
        if not(out) and n == '.':
            b+=1
        if not n == '.':
            if not stay:
                out = not(out)
                if n in ['F','L']:
                    stay = not(stay)
                    last_turn = n
            else:
                if n in ['7','J']:
                    stay = not(stay)
                    if matchy[last_turn] == n:
                        out = not(out)

print(b)
