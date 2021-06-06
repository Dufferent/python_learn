#!/usr/bin/python3.5
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import os
import math

CIRCLE = 500
NEGETIVE = 0
ACTIVATE = 1

''' without timescale '''
class PID:
    def __init__(self,kp,ki,kd,exp,out):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.exp = exp
        self.out = out
        self.out.append(0)

        self.sum_err = 0
        self.err = 0
        self.last_err = 0
    def calcu(self,acq,mode):
        self.err = self.exp[0] - acq
        self.sum_err += self.err
        self.out[0] = self.kp * self.err + \
                      self.ki * self.sum_err + \
                      self.kd * (self.err - self.last_err) 
        if mode == NEGETIVE:
            self.out[0] = float(self.out[0]*(-1.0))
        self.last_err = self.err



if __name__ == "__main__":
    set_val = []
    out     = []
    set_val.append(7.9862)
    out.append(0)

    pid_handler = PID(0.1,0.05,0.0,set_val,out)
    calcu_times = CIRCLE

    fx = 0       # input

    fd = open("pid.txt","w+") # write data
    chart_rel_x = [bound for bound in range(0,CIRCLE)]
    chart_rel_y = []

    while (calcu_times):
        calcu_times -= 1
        # fx = -3*out[0] + 7
        fx = math.exp(out[0])
        pid_handler.calcu(fx,ACTIVATE)
        data = "set:%0.4lf\trel:%0.4lf\r\n"%(set_val[0],fx)
        fd.write (data)
        chart_rel_y.append(fx)
        os.system("clr.sh")
        print ("set:[%0.4f]"%set_val[0],"rel:[%0.4f]"%fx)

    fd.close()

    chart_set_x = [bound for bound in range(0,CIRCLE)]
    chart_set_y = []
    for x in range(0,CIRCLE):
        chart_set_y.append(set_val[0])
    np.array(chart_set_x)
    np.array(chart_set_y)
    np.array(chart_rel_x)
    np.array(chart_rel_y)
    plt.plot(chart_set_x,chart_set_y,'b')
    plt.plot(chart_rel_x,chart_rel_y,'r')
    plt.show()
    