#!/usr/bin/python3

# 题目：判断101-200之间有多少个素数，并输出所有素数。
from math import sqrt

def judge(nums):
    for i in range(2,int(sqrt(nums))+1):
        if ((nums % i) == 0):
            return -1
    return 0
ct = 0
for var in range(101,200):
    if ( judge(var) == 0):
        print (var)
        ct += 1
print ("totol nums:[%d]"%ct)