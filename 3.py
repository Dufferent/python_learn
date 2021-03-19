#!/usr/bin/python3

# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？


def judge_d(num):
    for i in range(1,num):
        if(i*i == num):
            return 1
    if(i == (num-1)):
        return 0

for num in range(0,10000):
    d20 = (num+100) 
    d21 = (num+268)
    k = 0
    k += judge_d(d20)
    k += judge_d(d21)
    if(k == 2):
        print ("find the int num:",num)
        k = 0
    else:
        k = 0