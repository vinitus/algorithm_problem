N = int(input())

num_list = []

for _ in range(N):
    num_list.append(int(input()))

def merge_sort(L_list):
    if len(L_list) < 2:
        return L_list
    middle_point = len(L_list)//2
    lower_list = merge_sort(L_list[:middle_point])
    higher_list = merge_sort(L_list[middle_point:])
    
    lower_index = higher_index = 0
    merge_result = []
    while lower_index < len(lower_list) and higher_index < len(higher_list):
        if lower_list[lower_index] < higher_list[higher_index]:
            merge_result.append(lower_list[lower_index])
            lower_index += 1
        else:
            merge_result.append(higher_list[higher_index])
            higher_index += 1
    merge_result += lower_list[lower_index:]
    merge_result += higher_list[higher_index:]
    
    return merge_result
        

num_list = merge_sort(num_list)
for i in num_list:
    print(i)