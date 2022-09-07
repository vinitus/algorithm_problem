X,Y = map(str,input().split())

X = list(X)
X.reverse()
Y = list(Y)
Y.reverse()

XY = list(str(int("".join(i for i in X))+int("".join(i for i in Y))))
XY.reverse()
print(int("".join(i for i in XY)))