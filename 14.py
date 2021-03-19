#!/usr/bin/python3

# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

array = input("请输入一行字符:=>")
Engwd_nums = 0
num_nums = 0
space_nums = 0
other_nums = 0

for index in range(0,len(array)):
    var = ord(array[index])
    if ( var >= 48 ) and ( var <= 57 ):
        num_nums += 1
    elif ( ( var >= 65 ) and ( var <= 90 ) ) \
        or ( ( var >= 97 ) and ( var <= 122 ) ):
        Engwd_nums += 1
    elif ( array[index] == ' ' ):
        space_nums += 1
    else:
        other_nums += 1

print ("Engwd:",Engwd_nums)
print ("nums:",num_nums)
print ("spaces:",space_nums)
print ("othrs:",other_nums)



