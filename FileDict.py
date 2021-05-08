import json
def merg_dict(d1,d2):
    res={}
    val=d1.values()
    for key, value in d1.items():
        for key1,value1 in d2.items():
            if value==key1:
                res[key]=value1
    return res



n,m=input().split()
with open(n, 'r') as f1:
    parsed_json1 = (json.loads(f1.read()))
with open(m, 'r') as f2:
    parsed_json2 = (json.loads(f2.read()))
print(merg_dict(parsed_json1,parsed_json2))

