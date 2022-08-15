class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('걷는다!')

    def eat(self):
        print(f'{self.name}!먹는다!')

dog = Animal('dog')
dog.walk()