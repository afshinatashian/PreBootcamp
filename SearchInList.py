def search_list(li,item):
    for i in li:
        if i==item:
            return True
        else:
            return False


input_list=eval(input())
search_item=input()
print(search_list(input_list,search_item))