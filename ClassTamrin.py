size = 4
names = []
fileds = []

for i in range(size):
    print("Enter name and fields")
    names.append(input())
    fileds.append(int(input()))

human = dict(zip(names, fileds))
print(human)


