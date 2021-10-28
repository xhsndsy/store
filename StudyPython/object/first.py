class Student(object):

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def set_name(self, name):
        self._name = name

    def set_score(self, score):
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self._name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student()

bart.set_name('王二狗')
bart.set_score(99)

print(bart.print_score())

print(bart.get_grade())