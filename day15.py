##### Day 14 #####
hs = open('day15.txt','r').read().strip().split(',')

def hash(s):
    x = 0
    for c in s:
        x = 17*(x+ord(c)) % 256
    return x

boxes = {n:[] for n in range(256)}
for h in hs:
    eq = max(h.find('='), h.find('-'))
    s = h[:eq]
    sb = hash(s)
    if h[eq] == '=': 
        num = int(h[eq+1:])
        if s in [x[0] for x in boxes[sb]]:
            ind = [x[0] for x in boxes[sb]].index(s)
            boxes[sb][ind] = [s, num]
        else:
            boxes[sb].append([s,num])
    else:
        if s in [x[0] for x in boxes[sb]]:
            ind = [x[0] for x in boxes[sb]].index(s)
            del boxes[sb][ind]

sum([hash(s) for s in hs])
sum([(k+1)*sum([a*b for a,b in zip(range(1,len(v)+1),[q[1] for q in v])]) for k, v in boxes.items()])
