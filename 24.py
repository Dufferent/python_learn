# coding=utf-8

def numWays(steps,arrLen):
    dp = []
    
    for s in range(0,steps+1):
        tmps = []
        for p in range(0,arrLen):
            tmps.append(0)
        dp.append(tmps)
    dp[0][0] = 1
    # print (dp)


    for s in range(1,steps+1):
        for p in range(0,min(s+1,arrLen)):
            dp[s][p] += dp[s-1][p]
            if (p-1>=0):
                dp[s][p] += dp[s-1][p-1]
            if (p+1<arrLen):
                dp[s][p] += dp[s-1][p+1]
    # for s in range(0,steps+1):
    #     print (dp[s])
    return dp[steps][0]%(1000000007)

if __name__ == "__main__":
    print (numWays(438,315977))