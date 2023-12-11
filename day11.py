##### Day 11 #####
txt = []
with open("day11.txt","r") as f:
    for line in f:
        txt.append(line.rstrip('\n'))

dotrows = [ind for line, ind in zip(txt, range(len(txt))) if line == '.'*len(txt)]
dotcols = [ind for ind in range(len(txt[0])) if all([x[ind]=='.' for x in txt])]

poss = []
for line, ind in zip(txt,range(len(txt))):
    for n, ind2 in zip(line,range(len(line))):
        if n == '#':
            poss.append([ind,ind2])

expansion = 1000000
dists = 0
for pair, ind in zip(poss,range(len(poss))):
    for pair2 in poss[ind+1:]:
        x1,y1 = pair
        x2,y2 = pair2
        dists += abs(x1-x2) + abs(y1-y2) + sum([z in dotrows for z in range(min(x1,x2),max(x1,x2))])*(expansion-1) + sum([z in dotcols for z in range(min(y1,y2),max(y1,y2))])*(expansion-1)
