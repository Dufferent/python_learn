#!/usr/bin/python3

# 题目：暂停一秒输出，并格式化当前时间。

import time as tm

print (tm.strftime("%Y-%m-%d -- %H-%M-%S",tm.localtime()))
tm.sleep(1)
print (tm.strftime("%Y-%m-%d -- %H-%M-%S",tm.localtime()))