import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1,T+1):
    _, N = input().split()
    N = int(N)
    input_lst = list(input().split())
    tmp = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    tmp2 = [i for i in range(10)]
    print(f'#{t}')
    zero_to_nine = {string:number for string,number in zip(tmp,tmp2)}
    input_lst.sort()
    for i in tmp:
        stop_flag = False
        for j in input_lst:
            if j == i:
                print(j,end = " ")
                stop_flag = True
            elif stop_flag:
                break
    print()