def tedad(h,nh,o):
    s=4*h+nh+2*o
    darsad_h=round(((4*h)/s)*100,2)
    darsad_nh=round((nh/s*100),2)
    darsad_o=round(((2*o)/s)*100,2)
    result={'hungry':darsad_h,'not hungry':darsad_nh,'ok':darsad_o,}
    return result

a,b,c = input().split()
a=int(a)
b=int(b)
c=int(c)
print(tedad(a,b,c))