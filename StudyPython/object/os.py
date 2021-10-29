import os

# 获取操作系统 posix 为linux unix Mac os X    nt为 windows
print(os.name)

# 获取系统环境变量
print(os.environ)

# 查看当前目录的绝对路径
print(os.path.abspath('.'))
print(os.path.abspath('../../all_sort_test.py'))

# 在某个目录下创建新目录，然后把文件目录完整表示
print(os.path.join('.', '123'))

# 获取文件扩展名
print(os.path.splitext('os.py'))

