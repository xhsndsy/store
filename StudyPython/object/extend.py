class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


if __name__ == '__main__':

    dog = Dog()
    cat = Cat()

    dog.run()
    cat.run()

    print(type(dog.run))
    print(isinstance(dog, Animal))
    print(dir('ABC'))
    print('ABC'.lower())