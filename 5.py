#!/usr/bin/python3

# 题目:输入三个整数x,y,z，请把这三个数由小到大输出。

xyz = input("input like x.y.z!")

x = int(xyz[0:1])
y = int(xyz[2:3])
z = int(xyz[4:5])
print("no order xyz:",x,y,z)

array = [x , y , z]
for i in range(0,3-1):
    for j in range(0,3-i-1):
        if (array[j] > array[j+1]):
            ts = array[j]
            array[j] = array[j+1]
            array[j+1] = ts
    print ("冒泡排序:[index:",i,"]:",array)