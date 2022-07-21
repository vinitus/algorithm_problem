import sys

sys.stdin = open(r"C:\Users\multicampus\algorithm_problem\SWEA\1210_LADDER1\input1.txt","r")

def search_left_right(n, dir_flag, tmp_list):
    edge_flag = False
    if (n == 0) or (n == 99):
        edge_flag = True
    if edge_flag:
        if n == 0:       
            if tmp_list[0] == 1 and dir_flag == "L":
                print("1")
                return "R","R"
            else:
                print("2")
                return "D","D"
        else:
            if tmp_list[0] == 1 and dir_flag == "R":
                print("3")
                return "L","L"
            else:
                print("4")
                return "D","D"
    else:
        for i in range(len(tmp_list)):
            if (tmp_list[i] == 1):
                if i == 0 and dir_flag != "R":
                    print("5")
                    return "L","L"
                elif i == 1 and dir_flag != "L":
                    print("7")
                    return "R","R"
                else:
                    print("8")
                    return "D","D"
        else:
            print("9")
            return "D","D"
t = int(input())
ladder = []

for _ in range(100):
    tmp = list(map(int,input().split()))
    ladder.append(tmp)

one_in_ladder = []

for i in range(len(ladder[0])):
    if ladder[0][i] == 1:
        one_in_ladder.append(i)
        
for i in range(len(ladder[-1])):
    if ladder[-1][i] == 2:
        goal = i
print(one_in_ladder)
stop_flag = False
#for one in one_in_ladder:
one = 67
y,x = 0,one
dir_flag = "D"
for _ in range(200):
    if (x > 0) and (x < 99):
        go_to_dir,dir_flag = search_left_right(x,dir_flag,[ladder[y][x-1],ladder[y][x+1]])
    elif x == 0:
        go_to_dir,dir_flag = search_left_right(x,dir_flag,[ladder[y][x+1]])
    else:
        go_to_dir,dir_flag = search_left_right(x,dir_flag,[ladder[y][x-1]])
    if go_to_dir == "L":
        x -= 1
    elif go_to_dir == "R":
        x += 1
    else:
        y+=1
    print(x,y,ladder[y][x],go_to_dir)
    if y == 99:
        if (ladder[y][x] == 2):
            stop_flag = True
            print(one)
            break
        else:
            break
# if stop_flag:
#     break