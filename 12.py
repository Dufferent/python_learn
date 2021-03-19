#!/usr/bin/python3

# 题目：打印出所有的"水仙花数"，
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

from math import pow

for var in range(100,1000):
    BW = int(var / 100)
    SW = int((var % 100) / 10)
    GW = int((var % 100) % 10 )
    if( int(pow(BW,3)) + int(pow(SW,3)) + int(pow(GW,3)) == var ):
        print (var)
