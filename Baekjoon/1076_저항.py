color_1 = str(input())
color_2 = str(input())
color_3 = str(input())

color_list = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
value_list = [i for i in range(10)]

print((value_list[color_list.index(color_1)]*10+value_list[color_list.index(color_2)])*(10**(value_list[color_list.index(color_3)])))