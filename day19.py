##### Day 18 #####
import re
txt = open('day19.txt','r').read().strip().split('\n\n')

rts = {x[:x.find('{')]: [[y[:y.find(':')],y[y.find(':')+1:]] if y.find(':') > -1 else y for y in x[x.find('{')+1:-1].split(',')] for x in txt[0].split('\n')}
ins = [[int(y) for y in re.findall(r'\d+', x)] for x in txt[1].split('\n')]

#a
def proc_line(xmas, st):
    x,m,a,s = xmas
    rt = rts[st]
    for r in rt[:-1]:
        if eval(r[0]):
            if r[1] in 'AR':
                return r[1]
            else:
                return proc_line(xmas, r[1])
    if rt[-1] in 'AR':
        return rt[-1]
    else:
        return proc_line(xmas, rt[-1])

sum([sum(xmas) if proc_line(xmas,'in') == 'A' else 0 for xmas in ins])

#b
def opp_cond(s):
    return s[0] + ('>' if s[1] == '<' else '<') + str(int(s[2:])+(1 if s[1] == '>' else -1))

for k,v in rts.items():
    rts[k] = v[:-1] + [[opp_cond(v[-2][0]),v[-1]]]

leads_to_A = []
st = 'in'
st_path = []
def all_A_paths(st, st_path):
    pt = st_path.copy()
    for ind,rt in zip(range(len(rts[st])),rts[st]):
        if ind > 0 and (ind != len(rts[st])-1):
            pt.append(opp_cond(last_rt))
        if rt[1] == 'A':
            leads_to_A.append(pt + [rt[0]])
        elif rt[1] != 'R':
            all_A_paths(rt[1], pt + [rt[0]])
        last_rt = rt[0]

all_A_paths(st,[])

s = 0
for pt in leads_to_A:
    bds = {xmas:[0,4001] for xmas in 'xmas'}
    for cond in pt:
        if cond[1] == '<':
            bds[cond[0]][1] = min(bds[cond[0]][1], int(cond[2:]))
        else:
            bds[cond[0]][0] = max(bds[cond[0]][0], int(cond[2:]))
    rg = [x[1]-x[0]-1 for x in bds.values()]
    s += rg[0]*rg[1]*rg[2]*rg[3]

print(s)