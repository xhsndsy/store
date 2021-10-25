grade = [
    ['罗恩', 23, 35, 44],
    ['哈利', 60, 77, 68, 88, 90],
    ['赫敏', 97, 99, 89, 91, 95, 90],
    ['马尔福', 100, 85, 90],

]

Potter = 0
Hermione = 0
Ronald = 0
Malfoy = 0


l = grade[0]
a = grade[1]
b = grade[2]
c = grade[3]

for i in range(1,len(l)):
    Ronald += l[i]

for i in range(1,len(a)):
    Potter += a[i]

for i in range(1,len(b)):
    Hermione += b[i]

for i in range(1,len(c)):
    Malfoy += c[i]

print('Ronald:',Ronald)
print('Potter:',Potter)
print('Hermione:',Hermione)
print('Malfoy:',Malfoy)