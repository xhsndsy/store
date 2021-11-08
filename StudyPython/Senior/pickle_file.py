import pickle
import os

d = dict(name='Bob', age=20, score=88)

f = open('1.txt','w')
pickle.dump(d, f)

f.close()

f = open('1.txt','r')
print(f.read())

a = pickle.load(f)

print(a)
f.close()

