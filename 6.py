#!/usr/bin/python3

# 题目:斐波那契数列。

F0 = 0
F1 = 1

farray = []

farray.append(F0)
farray.append(F1) 

for i in range(0,20):
    farray.append(farray[i]+farray[i+1])
ct = 0
for i in range(0,20):
    print ("\t\t\t",end='')
    for j in range(0,i):
        print (farray[ct]," ",end='')
        ct += 1
        if(ct >= 20):
            break
    print (" ")
    if(ct >= 20):
        break

