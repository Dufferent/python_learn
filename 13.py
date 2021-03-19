#!/usr/bin/python3

# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
from math import sqrt

def judge(nums):
    for i in range(2,int(sqrt(nums))+1):
        if ((nums % i) == 0):
            return -1
    return 0


def devid(nums, array):
    var = nums
    while (var > 0):
        for i in range(2,var):
            if (judge(i) == 0) and (var % i == 0):
                array.append(i)
                var /= i
                var = int(var)
                break
        if (judge(var) == 0):
            array.append(var)
            break
            

result = []
num = input("Please input a num:=>")
devid(int(num),result)
#print ("[result]:",result)
print ("[result:]",num,'=',end='')
for index in range(0,len(result)):
    print (result[index],end='')
    if( index != (len(result)-1) ):
        print (" x ",end='')
print (" ")