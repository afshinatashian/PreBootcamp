def seprator(N):
    list1=[]
    while (N):
        z=N % 10
        list1.append(z)
        N= int(N / 10)
    return sum(list1)

num=int(input("please enter number: "))
z=seprator(num)
while(z>10):
    z=seprator(z)
print(z)
