import math
def GCD1(N):
    gcdresult=[]
    for i in range(1,int(N/2+1)):
        for j in range(N,int(N/2-1),-1):
            g=math.gcd(i,j)
            gcdresult.append(g)
    gcdresult.sort()
    largestnum=gcdresult[-1]
    return largestnum

n=int(input())
print(GCD1(n),end='')
        