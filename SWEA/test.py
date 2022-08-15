<<<<<<< HEAD
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('걷는다!')

    def eat(self):
        print(f'{self.name}!먹는다!')

dog = Animal('dog')
dog.walk()
=======
arr = [3,6,7,1]
n = len(arr)
for i in range(1<<n):   # 1<<n 은 부분 집합의 갯수
	for j in range(n):    # 원소의 수만큼 비트를 비교
		if i & (1<<j):      # i의 j번 비트가 1인 경우
			print(f'{i = }, {j = }, {arr[j]}', end=", ")
	print()
print()
>>>>>>> fd5117d5a18ab82df4763a163766bbf8aa252ef8
