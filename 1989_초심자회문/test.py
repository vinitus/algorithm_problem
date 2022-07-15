import sys

sys.stdin = open("1989_초심자회문/input.txt","r")

T = int(input())

for t in range(T):
    L = list(map(str,input()))
    L_rev = []              # 뒤집어서 저장할 리스트
    for i in range(len(L)-1,-1,-1):     # 뒤집어버리기
        L_rev.append(L[i])
    L_str = "".join(L)      # "".join은 리스트를 문자열로 바꿔줘요
    L_rev_str = "".join(L_rev)
    if L_str == L_rev_str:  # 뒤집은 문자열과 그냥 문자열 비교
        print(f"#{t+1} 1")
    else:
        print(f"#{t+1} 0")