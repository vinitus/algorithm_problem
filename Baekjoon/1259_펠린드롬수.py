while True:
    N = int(input())
    if N == 0:
        break
    else:
        yes_no = True
        N_list = list(str(N))
        if len(N_list) % 2 == 0:
            for i in range(len(N_list)//2):
                j = len(N_list) - 1 - i
                if N_list[i] != N_list[j]:
                    yes_no = False
                    break
        else:
            for i in range((len(N_list) - 1) // 2):
                j = len(N_list) - 1 - i
                if N_list[i] != N_list[j]:
                    yes_no = False
                    break

    if yes_no:
        print("yes")
    else:
        print("no")