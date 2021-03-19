#!/usr/bin/python3

# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
def calcu( times, base):
    var = base
    if(times > 0):
        var = calcu( times-1, var/2)
    else:
        return var
    return var

def acum( times, base, sums):
    ct = times
    h  = base
    while ( ct ):
        sums += (h + h / 2)
        h /= 2
        ct -= 1
    return (sums - calcu(times,base))


times = int(input("请输入球的弹跳次数:=>"))
high  = int(input("请输入初始高度:=>"))
sum = 0
print (calcu(times , high))
print (acum(times,high,sum))
