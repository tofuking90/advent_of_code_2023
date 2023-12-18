##### Day 18 #####
mat = open('day18.txt','r').read().strip().split('\n')

def day18_load_dict(inst):
    n2d = {'0':'R','1':'D','2':'L','3':'U'}
    bd = {0:[0]}
    x,y = 0,0
    bd = {x:[(y,'U')]}
    print(str(len(inst)) + ' rows to process:')
    c=0
    for dr, num in inst:
        print(c)
        c+=1
        if dr == 'R':
            y += num
        elif dr == 'L':
            y -= num
        elif dr == 'D':
            if x in bd:
                bd[x].append((y,dr))
            else:
                bd[x] = [(y,dr)]
            for n in range(1,num):
                x += 1
                if x in bd:
                    bd[x].append((y,'C'))
                else:
                    bd[x] = [(y,'C')]
            x += 1
            if x in bd:
                bd[x].append((y,dr))
            else:
                bd[x] = [(y,dr)]
        elif dr == 'U':
            if x in bd:
                bd[x].append((y,dr))
            else:
                bd[x] = [(y,dr)]
            for n in range(1,num):
                x -= 1
                if x in bd:
                    bd[x].append((y,'C'))
                else:
                    bd[x] = [(y,'C')]
            x -= 1
            if x in bd:
                bd[x].append((y,dr))
            else:
                bd[x] = [(y,dr)]
    return bd

def fill_ct(bd):
    print(str(len(bd)) + ' values to process:')
    a = 0
    c = 0
    bd[0] = sorted(list(set(bd[0])))
    for v in bd.values():
        c+= 1
        if c % 100000 == 0:
            print(c)
        outside = True
        s = sorted(list(v))
        a += len(s) # one for each corner, just add the between-stuff now
        ud_so_far = 0
        for ind in range(len(s)-1):
            n, dr = s[ind]
            n2, dr2 = s[ind+1]
            if dr in 'UD':
                ud_so_far += 1
                if dr2 in 'UD' and (ud_so_far % 2 == 1):
                    a += n2 - n - 1
                    outside = outside if dr != dr2 else not outside
                elif not outside:
                    a += n2 - n - 1
            else: # just a column
                outside = not outside
                if not outside:
                    a += n2 - n - 1
    return a

inst = [[y[0],int(y[1])] for y in [x.split(' ') for x in mat]]
print(fill_ct(day18_load_dict(inst))) # 18a

inst = [[n2d[x[-2]], int(x[x.find('#')+1:-2],16)] for x in mat]
print(fill_ct(day18_load_dict(inst))) # 18b



############## Flood fill ##############
# Intractable for 18b
mat = open('day18.txt','r').read().strip().split('\n')
mat = [[x.split(' ')[0], int(x.split(' ')[1])] for x in open('day18.txt','r').read().strip().split('\n')]
max_r = sum([v for x,v in mat if x == 'R'])
max_d = sum([v for x,v in mat if x == 'D'])
max_l = sum([v for x,v in mat if x == 'L'])
max_u = sum([v for x,v in mat if x == 'U'])

def inbounds(x,y):
    return x >= 0 and x <= len(g)-1 and y >= 0 and y <= len(g[0])-1
    
g = [[0 for r in range(max_r+max_l+1)] for d in range(max_d+max_u+1)]

x,y = max_u+1, max_l+1
g[x][y] = 1
lrud = {'L':[0,1],'R':[0,-1],'U':[1,0],'D':[-1,0]}
for dr, num in mat:
    for n in range(num):
        x += lrud[dr][0]
        y += lrud[dr][1]
        g[x][y] = 1

max_height = min([ind for ind, val in zip(range(len(g)),g) if sum(val) == 0 and ind >= max_u+1])
min_height = max([ind for ind, val in zip(range(len(g)),g) if sum(val) == 0 and ind <= max_u+1])
g = g[min_height+1:max_height]
max_right = max([max([i for i,v in zip(range(len(g[0])),r) if v == 1]) for r in g])
min_right = min([min([i for i,v in zip(range(len(g[0])),r) if v == 1]) for r in g])
g = [x[min_right:max_right+1] for x in g]
g2 = g.copy()
# s = [[1,235]]
s = [[1,235]]
while s:
    x,y = s.pop()
    g[x][y] = 1
    for v in lrud.values():
        new_x, new_y = x+v[0], y+v[1]
        if inbounds(new_x, new_y) and g[new_x][new_y] == 0 and ([new_x, new_y] not in s):
            s.append([new_x,new_y])

sum([sum(x) for x in g])