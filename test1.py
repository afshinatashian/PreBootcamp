# number of markers:
# 1 <= N <= 100 
# # color_range of markers:
# 1 <= m <= 1000
# question :
# 3
# 1 1 2
# answer : 2
# question :
# 5
# 1 2 1 3 4
# answer : 2


n=int(input())
m=input().split()
duplicate_dict={} 
for i in m:
    duplicate_dict[i]=m.count(i)
best_key = min(duplicate_dict, key=duplicate_dict.get)

print(best_key)
