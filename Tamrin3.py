import math

def maghsom(n):
    magh1=[]
    i=int(math.sqrt(n))
    for j in range(1,i+1):
        if n%j==0:
            magh1.append(j)
            magh1.append(int(n/j))
    return list(set(magh1))

n = int(input())
tedad = 0
sum1 = 0
for i in range(1,n+1):

    p = maghsom(i)

    tedad += len(p)
    sum1 += sum(p)
print(tedad,sum1,end='')
