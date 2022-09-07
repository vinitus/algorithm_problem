A = [1,5,2,1,4,3,4,5,2,1,0]
# A = [1,2,3,2,1,2,3,2,1]
# A = [10,20,30,40,20,30]
# A = [5,1,2,3,4,3,2,1]

# [1,5,2,0,4,3,4,5,2,0,0]
# [1,5,2,0,4,3,4,5,0,0,0]
# [1,5,2,0,4,3,4,5,0,0,0]
# [1,5,2,0,4,3,4,5,0,0,0]

def max_del(tmp_list):
    tmp_list1 = list(tmp_list)
    while True:
        try:
            tmp_list1.remove(max(tmp_list))
        except ValueError:
            return tmp_list1

def max_to_0(tmp_list):
    tmp_list[tmp_list.index(max(tmp_list))] = 0
    return tmp_list

A_max = max(A)

if 

# max_tmp = 0
# plus_list = []
# tmp_list = []
# for i in range(len(A)):
#     if A[i] > max_tmp:
#         max_tmp = A[i]
#         tmp_list.append(max_tmp)
#         print(f'tmp_list {tmp_list}')
#         if tmp_list not in plus_list:
#             plus_list.append(tmp_list)
#         if A[i] > A[i+1]:
#             tmp_list.pop()
#             max_tmp = max(tmp_list)

# print(plus_list)