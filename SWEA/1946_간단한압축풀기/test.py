import sys

sys.stdin = open("1946_간단한압축풀기/input.txt","r")

T = int(input())

for t in range(1,T+1):
    N = int(input())            # 리스트 길이 입력받고
    L = []                      # 빈 리스트 선언
    C = list(range(N))          # C는 문자열
    K = list(range(N))          # K는 숫자
    for n in range(N):
        C[n], K[n] = map(str,input().split())   # 네
    result = ""                 # 문자열 연산을 위한 선언
    for i in range(N):
        result += C[i] * int(K[i])  # 문자열에 숫자를 곱하면 숫자만큼의 문자열이 복사댐
    count = 1                   # while문 조건을 위한 count
    while count <= 20:          # count 는 무한 loop를 방지하기 위함임
        tmp = result[0:10]      # result는 무지 긴데 이걸 앞에서부터 10글자만 복사
        L.append(tmp)           # 그걸 리스트 L에 넣음
        if len(result) <= 10:   # 조건문인데 만약 마지막에 리스트에 넣은 문자열의 길이가 10보다 작으면
            break               # 더 이상 10글자마다 줄바꿀 필요가 없기에 삭제
        result = result[10:]    # 복사한 문자열 만큼 제거한거임
        count += 1              
    print(f"#{t}")
    for i in L:
        print(i)