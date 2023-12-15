##### Day 14 #####
mat = open('day14.txt','r').read().splitlines()

def make_new_line(h_poss, o_cts, r_len):
    h_new = h_poss + [r_len]
    num_segs = len(o_cts)
    return '#'.join(['O'*o_cts[ind] + '.'*(h_new[ind+1]-h_new[ind]-1-o_cts[ind]) for ind in range(num_segs)])

def rot_cw(mat):
    return [''.join(r)[::-1] for r in list(zip(*mat))]

def cycle(mat,num_turns):
    s = 0
    for i in range(num_turns):
        r_len = len(mat[0])
        new_matt = []
        for r in mat:
            h_poss = [-1] + [ind for ind, c in enumerate(r) if c == '#']
            o_cts = [sum([c=='O' for c in s]) for s in r.split('#')] 
            s += sum([sum(range(r_len-h_pos-1,r_len-h_pos-1-o_ct,-1)) for h_pos, o_ct in zip(h_poss, o_cts)])
            new_matt.append(make_new_line(h_poss, o_cts, r_len))
        mat = rot_cw(new_matt)
    return mat, s

mat = rot_cw(rot_cw(rot_cw(mat)))

# Find first cycle
mats = [mat]
mn = mat.copy()
while True:
    mn, s = cycle(mn,4)
    if mn in mats:
        break
    mats.append(mn)

first_app = [ind for ind, m in zip(range(len(mats)),mats) if m == mn][0]
cycle_len = len(mats) - first_app

m_fin = mats[first_app + (int(1e9) - len(matts)) % cycle_len]
m = list(zip(*m_fin))
len_m = len(m[0])

print(cycle(mat,1)[1])
print(sum([sum([c == 'O' for c in l])*y for l, y in zip(m,range(len_m,0,-1))]))
