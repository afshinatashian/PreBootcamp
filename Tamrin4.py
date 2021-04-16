def tedad(a,b,c):
    lengthCount=int(a/b)
    widthCount=0
    if(a%b==0):
        return lengthCount,widthCount
    else:
        while(1):
            temp1=a-(lengthCount*b)
            temp2=temp1%c
            if(temp2==0):
                widthCount=int(temp1/c)
                return lengthCount,widthCount
            lengthCount=lengthCount-1
            if(lengthCount==0):
                break
        if(lengthCount==0 & widthCount==0):
            return -1
        return lengthCount,widthCount

a,b,c = input().split()
a=int(a)
b=int(b)
c=int(c)
result1=tedad(a, b, c)
if(result1==-1):
    print(-1,end='')
else:
    print(result1[0],result1[1],end='')
# print(tedad(a,b,c),end='')
# print(1,2,3)