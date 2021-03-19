#!/usr/bin/python3

# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
# 例如6=1＋2＋3.编程找出1000以内的所有完数。

from math import sqrt

def devid(nums, array):
    var = nums
    for i in range(1,nums):
        if (var%i == 0):
            array.append(i)

for var in range(1,1000):
    results = []
    devid(var , results)
#    print (results)
    sum = 0
    for index in range(0,len(results)):
        sum += results[index]
    if ( sum == var ):
        print (var)