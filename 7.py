#!/usr/bin/python3

# 题目：将一个列表的数据复制到另一个列表中

array = ["hellow", 1 ,"xny" , '!']

def list_copy(lsta , lstb):
    for var in lsta:
        lstb.append(var)

print (array)
cp = []
list_copy(array,cp)
print (cp)