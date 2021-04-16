z1,z2,z3=input().split()
result=int(z1)+int(z2)+int(z3)
if(int(z1)==0 or int(z2)==0 or int(z3)==0):
    print("No",end='')
else:
    print("Yes",end='') if (result==180) else print("No",end='')