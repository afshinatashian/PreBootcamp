def ali(statments):
    statments.sort()
    smallest_statment=""
    for i in statments[0]:
        smallest_statment +=i
        smallest_statment +=" "
    print("\n",smallest_statment)



n=int(input())
statments = []
for i in range(n):
    statment=input()
    my_list = statment.split()
    statments.append(my_list)

ali(statments)

