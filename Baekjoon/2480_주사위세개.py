dice_list = list(map(int,input().split()))
count = 1
dice_num = dice_list[0]
for i in range(1,3):
    if dice_num == dice_list[i]:
        count += 1
if dice_list[1] == dice_list[2] and count == 1:
    dice_num = dice_list[1]
    count += 1
if count == 1:
    print(max(dice_list)*100)
elif count == 2:
    print(1000+dice_num*100)
elif count == 3:
    print(10000+dice_num*1000)
