##### Day 8 #####
txt = []
with open("day8.txt","r") as f:
    for line in f:
        txt.append(line.rstrip('\n'))

# txt = ['LLR','','AAA = (BBB, BBB)','BBB = (AAA, ZZZ)','ZZZ = (ZZZ, ZZZ)']
lrlr = txt[0]
mp = {}
for row in txt[2:]:
    mp[row[:3]] = {'L':row[7:10], 'R':row[12:15]}

found = False
steps = 0
lr_ind = 0
len_lr = len(lrlr)
cur = 'AAA'
while ~found:
    cur = mp[cur][lrlr[lr_ind]]
    steps += 1
    if cur == 'ZZZ':
        print(steps)
        break
    lr_ind += 1
    if lr_ind == len_lr:
        lr_ind = 0

curs = [x for x in mp.keys() if x[-1] == 'A']
cycles = []
for cur in curs:
    found = False
    steps = 0
    lr_ind = 0
    while ~found:
        cur = mp[cur][lrlr[lr_ind]]
        steps += 1
        if cur[-1] == 'Z':
            cycles.append(steps)
            break
        lr_ind += 1
        if lr_ind == len_lr:
            lr_ind = 0

np.lcm.reduce([np.int64(x) for x in cycles])

