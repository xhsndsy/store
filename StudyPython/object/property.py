class Student(object):

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def resolution(self):
        return self._width * self._height

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value



if __name__ == '__main__':
    a = Student()

    a.width = 1024
    a.height = 768
    print('resolution =', a.resolution)
    if a.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')