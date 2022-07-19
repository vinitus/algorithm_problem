import sys

sys.stdin = open(r"SWEA\1206_view\input1.txt","r")

test_case = int(input())
building_list = list(map(int,input().split()))
stop_flag = False
total = 0
for i in range(2,test_case-2):
    stop_flag = False
    height_dif = building_list[i]
    for j in range(1,3):
        if (building_list[i] < building_list[i-j]) or (building_list[i] < building_list[i+j]):
            stop_flag = True
            break
        if building_list[i] - building_list[i-j] < height_dif:
            height_dif = building_list[i] - building_list[i-j]
        if building_list[i] - building_list[i+j] < height_dif:
            height_dif = building_list[i] - building_list[i+j]
    if stop_flag is not True:
        total += height_dif

print(f'#1 {total}')