##### Day 12 #####
import numpy as np
txt = [[line[:line.find(' ')]] + [[int(x) for x in line[line.find(' ')+1:-1].split(',')]] for line in open('day12.txt','r')]

def d12_recur(s, ls):
    str_len = len(s)
    num_ls = len(ls)
    best_map = {} # [a,b]:c means last a chars of s can fit last b numbers of ls in c ways
    ref_list = [ls[-1]] + [z+1 for z in np.cumsum(list(reversed(ls[:-1])))+ls[-1]]
    max_nums = {x:sum([x >= y for y in ref_list]) for x in range(1,str_len+1)}
    best_map[0,0] = 1
    for l in range(1,str_len+1):
        best_map[l,0] = 0 if '#' in s[-l:] else 1
    for l_ind in range(1,num_ls+1):
        ll = ls[-l_ind:]
        for s_ind in range(1,str_len+1):
            ss = s[-s_ind:]
            if max_nums[s_ind] < l_ind:
                best_map[s_ind,l_ind] = 0
            else:
                first_elem = ll[0]
                if len(ss) == first_elem:
                    best_map[s_ind,l_ind] = int(all([x in ['?','#'] for x in ss]))
                else:
                    num_combs = 0
                    if (sum([x in ['?','#'] for x in ss[:first_elem]]) == first_elem) and (ss[first_elem] != '#'):
                        num_combs += best_map[s_ind-first_elem-1,l_ind-1]
                    if ss[0] != '#':
                        num_combs += best_map[s_ind-1, l_ind]
                    best_map[s_ind,l_ind] = num_combs
    return best_map[s_ind, l_ind]

n = 5
sum([d12_recur((s+'?')*(n-1)+s,ls*n) for s,ls in txt])