def seprator(N):
    
    if int(N)<10:
        return N
    s = 0 
    for i in N:
        s+= int(i)
    return seprator(str(s))

num=input("")
print(seprator(num),end='')