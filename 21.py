#/usr/bin/python3.5

# PID

class PID:
    def __init__(self,
                 kp,
                 ki,
                 kd,
                 ex):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.err = 0
        self.err_last = 0
        self.sum_err = 0
        self.ex = ex

    def compute(self,get):
        self.err = float(self.ex)-float(get)
        out = float(self.kp)*float(self.err) \
        + float(self.ki)*float(self.sum_err) \
        + float(self.kd)*float(self.err-self.err_last)
        self.sum_err += self.err
        self.err_last = self.err
        return out


if __name__ == "__main__":
    print ("main function")
    obj = PID(0.2,0.5,0.0,3.6)

    X = 0.5

    while (1):
        Y = 2*X+3
        X = obj.compute(Y)
        err_sum = obj.sum_err
        print ("real val:%0.3f => Ex val:3.6 "%Y,end='')
        print ("=> Sum err:%0.3f"%err_sum)
        for i in range(1,1024000*2):
            continue
        
        

