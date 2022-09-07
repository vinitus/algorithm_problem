while True:
    N, M = map(int,input().split())
    if N == 0 and M == 0:
        break
    if M % N == 0:          # 첫번째 숫자가 두번째 숫자의 약수
        print('factor')
    elif N % M == 0:        # 첫번째 숫자가 두번째 숫자의 배수
        print('multiple')   
    else:                   # 둘 다 아니면
        print('neither')