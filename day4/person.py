names = [
    ["曹操", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700, "10"]
]
'''
    平均薪资
'''
l = [x[5] for x in names]
count = 0
for i in range(len(l)):
    count += l[i]

avg = count / len(l)
print('平均薪资', avg)

# 平均年龄
l = [x[6] for x in names]
count = 0
for i in range(len(l)):
    count += int(l[i])

avg = count / len(l)
print('平均年纪', avg)

# 新增员工
names += [
    ['刘备', '45', '男', 220, 'alibaba', 500, 30]
]
print(names)

# 统计男女人数
l = [a[2] for a in names]

woman = 0
man = 0

for i in range(len(l)):
    if l[i] == '男':

        man += 1

    elif l[i] == '女':

        woman += 1

print('男：', man, '女：', woman)



# 每个部门人数
l = [a[4] for a in names]

IBM = 0
Microsoft = 0
Oracle = 0
Tencent = 0
Alibaba = 0

for i in range(len(l)):
    if l[i] == 'IBM':

        IBM += 1

    elif l[i] == '微软':

        Microsoft += 1

    elif l[i] == 'Tencent':

        Tencent += 1

    elif l[i] == 'alibaba':

        Alibaba += 1

print('IBM：', IBM, 'Microsoft：', Microsoft, 'Tencent：', Tencent , 'Alibaba：',  Alibaba)