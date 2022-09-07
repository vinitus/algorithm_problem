def Euclidean(num1,num2):
    num1,num2 = max(num1,num2), min(num1,num2)
    if num2 == 0:
        return num1
    
    tmp1 = num1 % num2
    print(f'tmp1 {tmp1}')
    if tmp1 == 0:
        print(f'num2 {num2}')
        return num2
    
    tmp2 = num2 % tmp1        
    print(f'tmp2 {tmp2}')
    if tmp2 == 0:
        return tmp1
    else:
        print(tmp1,tmp2)
        Euclidean(tmp1,tmp2)

# N = int(input())
# num_list = []
# for i in range(N):
#     num_list.append(int(input()))
x = Euclidean(1071,1029)
print(x)
x = Euclidean(78696,19332)
print(x)