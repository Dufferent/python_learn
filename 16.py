#!/usr/bin/python3

# 题目：求s=a+aa+aaa+aaaa+aa...a的值，
# 其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

def acumulate(a , count):
    sum = 0
    pre = 0
    for i in range(0,count):
        var = pre*10 + a
        pre = var
        sum += var
    return sum

a  = int(input("please input num[a]:=>"))
ct = int(input("please input count[ct]:=>"))
result = acumulate(a,ct)
print (result)



