##### Day 9 #####
import re
import numpy as np

nums = []
with open("day9.txt","r") as f:
    for line in f:
        nums.append([int(x) for x in line.rstrip('\n').split(' ')])

c = 0
ind = 0
for num in nums:
    arr = [num]
    while True:
        this_num = arr[-1]
        arr.append([this_num[j]-this_num[j-1] for j in range(1,len(this_num))])
        if sum(arr[-1]) == 0:
            break
    c += sum([x[-1] for x in arr])

print(c)

c = 0
for num in nums:
    arr = [num]
    while True:
        this_num = arr[-1]
        arr.append([this_num[j]-this_num[j-1] for j in range(1,len(this_num))])
        if sum(arr[-1]) == 0:
            break
    c += sum([arr[n][0]*(-1)**n for n in range(len(arr))])

print(c)


