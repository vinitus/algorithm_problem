count = 0
while True:
    N = int(input())
    count += 1 
    if N == 0:
        break
    kids = {}
    kids_name = []
    for i in range(N):
        mes = list(map(str,input().split()))
        kid = mes.pop(0)
        kids_name.append(kid)
        kids[kid] = mes
    kids_name_copy = kids_name[:]
    print_no = []
    print(f"Group {count}")
    for i in kids_name_copy:
        for k in range(N-1):
            if kids[i][k] == "N":
                for j in range(len(kids_name)):
                    if kids_name[0] != i:
                        kids_name.append(kids_name.pop(0))
                print_no.append("a")
                print(f"{kids_name[-(k+1)]} was nasty about {i}")
    if len(print_no) == 0:
        print("Nobody was nasty")
    print("")