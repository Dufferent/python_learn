#/usr/bin/python3.5
# coding=utf-8

if __name__ == "__main__":
    # print ("你好，世界")
    rows = input("请输入打印菱形的行数")
    rows = int(rows)
    if (rows%2):
        half = rows/2+1
    else:
        half = rows/2
    half = int(half)
    
    for i in range(1,half+1):
        space_nums = ((half*2-1)-(2*i-1))/2
        space_nums = int(space_nums)
        for j in range(1,space_nums+1):
            print (' ',end='')
        for k in range(1,2*i):
            print ('*',end='')
        print ('')
    if (rows%2):
        space_nums = 1
    else:
        space_nums = 0
    for i in range(half+1,rows+1):
        for j in range(1,space_nums+1):
            print (' ',end='')
        for k in range(1,2*(rows-i+1)):
            print ('*',end='')
        space_nums+=1
        print ('')

