import sys
def input():
    return sys.stdin.readline().rstrip()

lst = []
a = input()
while a != 'end':
    lst.append(a)
    a = input()


for word in lst:
    check = [1,2,2]
    answer = ''

    if word[0] in ['a','e','i','o','u']:
        check[0] = 0
        check[1] -= 1
    else:
        check[2] -= 1
    
    for i in range(1,len(word)):
        if word[i-1] == word[i]:
            if word[i] not in ['e','o']:
                answer = 'not '
                break
        if word[i] in ['a','e','i','o','u']:
            check[0] = 0
            if check[1]:
                check[1] -= 1
                check[2] = 2
            else:
                answer = 'not '
                break
        else:
            if check[2]:
                check[1] = 2
                check[2] -= 1
            else:
                answer = 'not '
                break
    if check[0]:
        answer = 'not '
    print(f'<{word}> is {answer}acceptable.')