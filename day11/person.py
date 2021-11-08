class person:
    __age = 0
    __name = ''
    __sex = ''

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_sex(self, sex):
        self.__sex = sex

    def get_sex(self):
        return self.__sex

class worker(person):
    def do_work(self):
        print('这个工人叫%s，是%s性，已经%s岁大了' % (self.get_name(), self.get_sex(), self.get_age()))

class student(person):
    __number = 0

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number

    def study(self):
        print('%s的学号是%s，性别%s，已经%s岁大了'% (self.get_name(), self.get_number(), self.get_sex(), self.get_age()))

    def sing_song(self):
        print('唱歌')

