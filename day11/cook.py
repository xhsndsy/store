import time

class cook:
    __name = ''
    __age = 0

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def cook_food(self):
        pass

class apprentice(cook):
    def cook_vegetables(self):
        pass

class trainee(apprentice):
    def cook_food(self):
        print()
        print('蒸饭ing')
        for i in range(5):
            print('.', end='')
            time.sleep(0.5)

    def cook_vegetables(self):
        print()
        print('炒菜ing')
        for i in range(5):
            print('.', end='')
            time.sleep(0.5)


if __name__ == '__main__':
    t = trainee()
    t.set_age(20)
    t.set_name('惠小可怜')

    print('厨师叫%s，已经%s岁大了' % (t.get_name(), t.get_age()))

    t.cook_food()
    t.cook_vegetables()