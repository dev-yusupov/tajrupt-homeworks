my_list = [4, 2, 49, 10, 100]

def sort_list(list):
    n = len(list)

    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    
    return list
    

print(sort_list(my_list))