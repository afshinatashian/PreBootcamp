# ( "gold", 1000, ("navid check", 3542),["neda watch",500],{"sanad khone" :"felan ja"}, {"name" :"navid", "pass" :"qwerty 1234"} )
# {str : 1,dict:2,list:1,tuple:1,set:0,}


result = {str:0,dict:0,list:0,tuple:0,set:0}
tpl = eval(input())
for i in tpl:
    if type(i) is list:
        result[list]+=1
    elif type(i) is dict:
        result[dict] += 1 
    elif type(i) is str:
        result[str] += 1 
    elif type(i) is tuple:
        result[tuple] +=1 
    elif type(i) is set:
        result[set] += 1 
print(result)