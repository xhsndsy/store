import json

d = dict(name='Bob', age = 20, score= 88)

f = open('2.txt','w')

f.write(json.dumps(d))

f.close()

f = open('2.txt','r')

a = f.read()

# 反序列化对象
print(json.loads(a))