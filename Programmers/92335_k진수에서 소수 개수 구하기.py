def solution(n, k):
    change = ''
    while n > 0:
        change = str(n % k) + change
        n //= k
    answer = 0
    gogo = []
    for i in change.split('0'):
        if i and int(i) != 1:
            i = int(i)
            for j in range(2,int(i**0.5)+1):
                if i % j == 0:
                    break
            else:
                answer += 1    
            
    return answer