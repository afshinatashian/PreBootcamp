import math
def Prime(N):
    counter=1
    if N==1:
        return False
    j=int(math.sqrt(N))
    for i in range(1,j+1):
        if N%i==0:
            counter+=1
    return counter==2

def TPrime(N):
    z=math.sqrt(N)
    if(Prime(z)):
        return "yes"
    else:
        return "no"

inputLength=int(input())
stringInput=input()
stringNumbers=stringInput.split(' ')
numbers=[]
for i in range(inputLength):
    numbers.append(int(stringNumbers[i]))

TP=[]
for i in range(inputLength):
    TP.append(TPrime(numbers[i]))

for i in range(TP.__len__()):
    print(TP[i],end=' ')