import json

d = dict(name='bob', age=20, score=80)

print(json.dumps(d))

s = json.dumps(d)


print(json.loads(s))