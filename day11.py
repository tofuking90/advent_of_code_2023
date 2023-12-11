##### Day 11 #####
mat = np.array([list(line.strip()) for line in open('day11.txt','r')])
dotrows = [ind for line, ind in zip(mat, range(len(mat))) if all(x=='.' for x in line)]
dotcols = [ind for ind in range(len(mat[0])) if all([x[ind]=='.' for x in mat])]
poss = np.where(mat=='#')

def expanded_dists(expansion):
    dists = 0
    for x1, y1, ind in zip(poss[0], poss[1],range(len(poss[0]))):
        for x2, y2 in zip(poss[0][ind+1:], poss[1][ind+1:]):
            dists += abs(x1-x2) + abs(y1-y2) + sum([z in dotrows for z in range(min(x1,x2),max(x1,x2))])*(expansion-1) + sum([z in dotcols for z in range(min(y1,y2),max(y1,y2))])*(expansion-1)
    return dists

expanded_dists(2)
expanded_dists(1000000)
