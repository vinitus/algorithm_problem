N = int(input())
L = list(map(int,input().split()))
L.sort()          # 중간값을 찾기 위해 정렬
print(L[N//2])    # //를 통해서 정수 몫만 구함