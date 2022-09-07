N = int(input())

# N = 5면

# -1 0 1 2 3 4 5 6 7 8 9 0 1 2
#      B A B A B A B A B A B A
#  A B B A B A B A B A B     A
#  A B B A B A     B A B B A A
#  A B B A B A A B B     B A A


# -1 0 1 2 3 4 5 6 7 8 9 10
#      B A B A B A B A B A
#  A B B A B A B A B B    A
#  A B B A     B A B B A A
#  A B B A A B B     B A A
#  A     A A B B B B B A A
#  A A A A A B B B B B

#         B A B A B A
#     A B B A B     A
#     A B B     A B A
#     A B B B A A
# A A A B B B

def sol(n):
    if n == 3:
        print()