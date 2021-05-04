def GCD1(N):
    gcdresult=[]
    for i in range(1,N+1):
        if N%i==0:
            gcdresult.append(i)
    return gcdresult


n,m=input().split()
match=[]
for i in GCD1(int(n)):
    for j in GCD1(int(m)):
        if i==j:
            match.append(i)
match.sort()
print(match[-1])