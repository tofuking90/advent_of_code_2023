##### Day 22 #####
def sq_list(brick):
    return list(itertools.product(*[range(brick[0][i], brick[1][i]+1) for i in range(3)]))

def lowest_free_spot(b, occupado):
    x,y,z = b
    zs_below = [ind for ind in range(len(occupado[x][y])) if occupado[x][y][ind] == 1 and ind < z]
    return max(zs_below) + 1 if zs_below else 0

def drop_brick(ind):
    b = bricks[ind]
    if b[0][2] < b[1][2]: # Vertical brick:
        mv_dist = b[0][2] - lowest_free_spot(b[0], occupado)
    else:
        mv_dist = b[0][2] - max([lowest_free_spot(br, occupado) for br in sq_list(b)])
    new_b = [[b[0][0], b[0][1], b[0][2] - mv_dist], [b[1][0], b[1][1], b[1][2] - mv_dist]]
    for sq in sq_list(b):
        occupado[sq] = 0
    for sq in sq_list(new_b):
        occupado[sq] = 1
    bricks[ind] = [new_b[0], new_b[-1]]


bricks = [sorted([[int(z) for z in y.split(',')] for y in x.split('~')]) for x in open('day22.txt','r').read().strip().split('\n')]
bricks = sorted(bricks, key = lambda x: min(x[0][2], x[1][2]))
num_bricks = len(bricks)

xyz_lims = [max([max(x[0][dim], x[1][dim])+1 for x in bricks]) for dim in range(3)]
tot_cells = xyz_lims[0]*xyz_lims[1]*xyz_lims[2]

# Populate current state of tower
occupado = np.zeros(xyz_lims)
for b in bricks:
    for sq in sq_list(b):
        occupado[sq] = 1

# settle bricks
prev_state = np.zeros(xyz_lims)
while True:
    for i in range(num_bricks):
        drop_brick(i)
    if sum(sum(sum(prev_state == occupado))) == tot_cells:
        break
    prev_state = occupado.copy()

# Count removable bricks
num_removable = 0
occupado_backup = occupado.copy()
bricks_backup = bricks.copy()
for i in range(num_bricks):
    print(i)
    occupado = occupado_backup.copy()
    bricks = bricks_backup.copy()
    for sq in sq_list(bricks[i]):
        occupado[sq] = 0
    del bricks[i]
    occupado2 = occupado.copy()
    for j in range(num_bricks-1):
        if bricks[j][0][2] > bricks_backup[i][0][2]:
            drop_brick(j)
            if sum(sum(sum(occupado2 == occupado))) != tot_cells:
                print('stopped at: ' + str(j))
                break
    if sum(sum(sum(occupado2 == occupado))) == tot_cells:
        num_removable += 1

print(num_removable) 

# Part b
num_moved = 0
occupado = occupado_backup.copy()
bricks = bricks_backup.copy()
occupado_backup = occupado.copy()
bricks_backup = bricks.copy()
for i in range(num_bricks):
    print(i)
    occupado = occupado_backup.copy()
    bricks = bricks_backup.copy()
    for sq in sq_list(bricks[i]):
        occupado[sq] = 0
    del bricks[i]
    prev_state = occupado.copy()
    bricks_del = bricks.copy()
    while True:
        for j in range(num_bricks-1):
            drop_brick(j)
        if sum(sum(sum(prev_state == occupado))) == tot_cells:
            break
        prev_state = occupado.copy()
    num_moved += sum([x!=y for x,y in zip(bricks, bricks_del)])

print(num_moved)





