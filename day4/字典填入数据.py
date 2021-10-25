dict={}#键 1  2  3    4 56789
name=input("请输入2个字符")
for i,x in zip(range(1,len(name)+1),name):
    dict[i]=x
print(dict)