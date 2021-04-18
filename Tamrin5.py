def zojfard(N,item):
    Adad=[]
    for i in range(N):
        if(i%2!=0):
            Adad.append(i)
    for i in range(N, 0, -1):
        if(i%2==0):
            Adad.append(i)
    indexitem = Adad.index(item)
    return Adad,indexitem

n,k = input().split()
result=zojfard(int(n),int(k))
print(result[1],end='')
