#!/usr/bin/python3

#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
for num_1 in range(1,5):
    for num_2 in range(1,5):
        for num_3 in range(1,5):
            if (num_1 != num_2) and (num_2 != num_3) and (num_1 != num_3):
                print(num_1,num_2,num_3)