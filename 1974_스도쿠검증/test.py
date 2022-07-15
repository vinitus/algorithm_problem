import sys

sys.stdin = open("1974_스도쿠검증/input.txt","r")

T = int(input())

for t in range(1,T+1):
    L = []

    for i in range(9):
        tmp = list(map(int,input().split()))
        L.append(tmp)

    flag = False        # 탈출을 위한 조건

    # 행을 검사하기 위함
    for i in L:
        tmp = []        # 중복 검사를 위한 list인 tmp 선언
        for j in i:
            if j not in tmp:
                tmp.append(j)
            else:
                flag = True
                break
        if flag:
            break

    if flag is not True:        # 행 검사 통과시
        for i in range(9):      # 열 검사 시작
            tmp = []
            for j in range(9):
                if L[j][i] not in tmp:
                    tmp.append(L[j][i])
                else:
                    flag = True
                    break
            if flag:
                break
    else:
        pass

    if flag is not True:        # 열 검사 통과시
        for i in range(0,9,3):  # 3x3을 검사하기 위해서 시작 인덱스는 0 3 6이 되어야함
            for j in range(0,9,3):  # 이하 동문이에요
                tmp = []
                for k in range(3):
                    for l in range(3):      # 3x3을 검사하기 위함임
                        if L[i+k][j+l] not in tmp:
                            tmp.append(L[i+k][j+l])
                        else:
                            flag = True
                            break
                if flag:
                    break
            if flag:
                break
    else:
        pass
    if flag:
        print(f"#{t} 0")
    else:
        print(f"#{t} 1")