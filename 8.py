#!/usr/bin/python3

# 题目：输出 9*9 乘法口诀表。

for i in range(1,10):
    for j in range(0,i):
        print (i,'x',j+1,'=',i*(j+1)," ",end='')
    print(" ")
