def half_up(n,count):
    count += 1
    if len(str(n)) == count:
        print(n)
        return
    tmp = n % 10**count
    n -= tmp
    if tmp >= 5*10**(count-1):
        n += 10**count
    return half_up(n,count)

N = int(input())

half_up(N,0)