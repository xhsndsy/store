def exchange(grade):
    if grade >= '90':
        return 'A'
    elif grade >= '80':
        return 'B'
    elif grade >= '70':
        return 'C'
    elif grade >= '60':
        return 'D'
    else:
        return 'E'

if __name__ == '__main__':
    grade = input('请输入成绩')
    print(exchange(grade))