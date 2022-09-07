def star(star_list,count,goal):
    move_index = (count - 1) // 2
    count *= 3
    tmp = goal // count
    middle = (goal - 1) // 2
    for x_i in range(-(tmp-1)//2,(tmp-1)//2+1):
        for y_i in range(-(tmp-1)//2,(tmp-1)//2+1):
            middle_x = middle + count*x_i
            middle_y = middle + count*y_i
            for x in range(-move_index,move_index+1):
                for y in range(-move_index,move_index+1):
                    star_list[middle_x+x][middle_y+y] = " "


    if count == goal:
        for x in star_list:
            for y in x:
                print(y,end="")
        return
    else:
        star(star_list,count,goal)

T = int(input())
star_dot = []
for i in range(T):
    tmp_list = list("*" for j in range(T-1))
    tmp_list.append("*\n")
    star_dot.append(tmp_list)
star(star_dot,1,T)