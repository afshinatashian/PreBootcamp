obj=eval(input())
#obj = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print(type(obj))
exit()
key=obj.keys()
l=len(key)
result=[]
result2={}
for k in key:
    temp=obj[k]
    for i in range(len(temp)):
        if len(result)<i+1:
            result.append({})
        result2.update(result[i])
        result2[k]=temp[i]
        result[i]=result2.copy()
        result2.clear()
print(result)