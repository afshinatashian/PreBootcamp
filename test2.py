def tedad(c,b,a):
    count=0
    lengthCount=int(a/b)
    widthCount=0
    while(1):
        temp1=a-(lengthCount*b)
        temp2=temp1%c
        if(temp2==0):
            widthCount=int(temp1/c)
            count+=1
        lengthCount=lengthCount-1
        if(lengthCount==0):
            break   
    
    lengthCount=int(a/c)
    widthCount=0
    while(1):
        temp1=a-(lengthCount*c)
        temp2=temp1%b
        if(temp2==0):
            widthCount=int(temp1/b)
            count+=1
        lengthCount=lengthCount-1
        if(lengthCount==0):
            break
    return count

a,b,c = input().split()
a=int(a)
b=int(b)
c=int(c)
print(tedad(a,b,c))

