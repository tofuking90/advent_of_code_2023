##### Day 13 #####
import numpy as np
mats2 = [mat.splitlines() for mat in open('day13.txt','r').read().split('\n\n')]

def h_mirror(mat,s): # 0 for a, 1 for b
    n_rows = len(mat)
    for mir in range(1,n_rows):
        half_len = min(n_rows - mir, mir)
        if sum([sum(mat[mir-x-1] != mat[mir+x]) for x in range(half_len)]) == s:
            return mir
    return 0

sum([100*h_mirror(np.array([list(l) for l in mat]),0) + h_mirror(np.array([list(l) for l in mat]).transpose(),0) for mat in mats])
sum([100*h_mirror(np.array([list(l) for l in mat]),1) + h_mirror(np.array([list(l) for l in mat]).transpose(),1) for mat in mats])
