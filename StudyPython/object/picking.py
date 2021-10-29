import pickle
import os

d = dict(name='Bob', age=20, score=88)

try:
    f = open('./' + 'new' + '.txt', 'wb')

    pickle.dump(d, f)

finally:
    if f:
        f.close()

try:
    f = open('new.txt', 'rb')
    a = pickle.load(f)
finally:
    f.close()
print(a)
