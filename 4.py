#!/usr/bin/python3

# 题目：输入某年某月某日，判断这一天是这一年的第几天？

def judge_year(years):
    if ((years % 4) == 0) and (years % 100 != 0) or (years % 400 == 0):
        return 0

date = input("请输入[xxxx(年)].[xx(月)].[xx(日)]")

year = int(date[0:4])
month = int(date[5:7])
day = int(date[8:10])

print(year,month,day)

dth = 0

flag = judge_year(year)
if (month >= 1):
    dth += 0
if (month >= 2):
    dth += 31
if (month >= 3):
    if (flag == 1):
        dth += 29
    else:
        dth += 28
if (month >= 4):
    dth += 31
if (month >= 5):
    dth += 30
if (month >= 6):
    dth += 31
if (month >= 7):
    dth += 30
if (month >= 8):
    dth += 31
if (month >= 9):
    dth += 31
if (month >= 10):
    dth += 30
if (month >= 11):
    dth += 31
if (month >= 12):
    dth += 30

dth += day
print ("The day is the[",dth,"]th of the year!")