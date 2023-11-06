import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

name = ["CY", "SK"]
print(name[N%2])