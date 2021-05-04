def search_Dict(li,item):
    if item in li:
        return True
    else:
        return False


input_list=eval(input())
search_item=input()
print(search_Dict(input_list,search_item))