# n에 대하여 n보다는크고 2n보다는 작거나 같은 수 중에서 소수는 적어도 하나는 존재
# import time

# def prime(aa,tmp_list):
#     standard = 1
#     if aa == 1:
#         standard = 0
#     for i in range(2,int(aa**0.5)+1):
#         if aa % i == 0:
#             standard = 0
#             break
#     if standard != 0:
#         tmp_list.append(aa)

# while True:
#     result_list = []
#     n = int(input())
#     start_time = time.time()
#     if n == 0:
#         break
#     for i in range(n+1,2*n+1):
#         prime(i,result_list)
#     print(len(result_list))
    
#     print("time :", time.time()-start_time)

def prime(number, some_list):
    stop = 1
    if number == 1:
        stop = 0
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            stop = 0
            break
    if stop != 0:
        some_list.append(number)

list_prime = []
for i in range(2,123456*2+1):
    prime(i,list_prime)

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in list_prime:
        if n < i <= n*2:
            count += 1
    print(count)