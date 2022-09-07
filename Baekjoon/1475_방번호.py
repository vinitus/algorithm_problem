N = str(input())
N_list = list(N)
count = 0
while True:
    for i in range(1,11):
        if str(i) in N_list:
            N_list.remove(str(i))
            if count == 0:
                count += 1            
