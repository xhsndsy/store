import xlrd

# 读表
book = xlrd.open_workbook(filename='2020年每个月的销售情况.xls')

total = 0
num = 0
money = 0

down_jacket = 0
jeans = 0
dust_coat = 0
fur = 0
T_shirt = 0
best = 0
suits = 0
fur_clothing = 0
casual_pants = 0
fleece = 0
blouse = 0
cotton = 0
pencil_pants = 0

for sheet in range(book.nsheets):
    Jan = book.sheet_by_index(sheet)

    for rx in range(1, Jan.nrows):
        total += int(Jan.cell_value(rowx=rx, colx=4))
        money += int(Jan.cell_value(rowx=rx, colx=4)) * float(Jan.cell_value(rowx=rx, colx=2))
        if Jan.cell_value(rowx=rx, colx=1) == '羽绒服':
            down_jacket += int(Jan.cell_value(rowx=rx, colx=4))
        elif Jan.cell_value(rowx=rx, colx=1) == '牛仔裤':
            jeans += int(Jan.cell_value(rowx=rx, colx=4))
        elif Jan.cell_value(rowx=rx, colx=1) == '风衣':
            dust_coat += int(Jan.cell_value(rowx=rx, colx=4))
        elif Jan.cell_value(rowx=rx, colx=1) == '皮草':
            fur += int(Jan.cell_value(rowx=rx, colx=4))
        elif Jan.cell_value(rowx=rx, colx=1) == 'T血':
            T_shirt += int(Jan.cell_value(rowx=rx, colx=4))
        elif Jan.cell_value(rowx=rx, colx=1) == '马甲':
            best += int(Jan.cell_value(rowx=rx, colx=4))
        elif Jan.cell_value(rowx=rx, colx=1) == '皮衣':
            fur_clothing += int(Jan.cell_value(rowx=rx, colx=4))
        elif Jan.cell_value(rowx=rx, colx=1) == '小西装':
            suits += int(Jan.cell_value(rowx=rx, colx=4))
        elif Jan.cell_value(rowx=rx, colx=1) == '休闲裤':
            casual_pants += int(Jan.cell_value(rowx=rx, colx=4))
        elif Jan.cell_value(rowx=rx, colx=1) == '卫衣':
            fleece += int(Jan.cell_value(rowx=rx, colx=4))
        elif Jan.cell_value(rowx=rx, colx=1) == '衬衫':
            blouse += int(Jan.cell_value(rowx=rx, colx=4))
        elif Jan.cell_value(rowx=rx, colx=1) == '棉衣':
            cotton += int(Jan.cell_value(rowx=rx, colx=4))
        elif Jan.cell_value(rowx=rx, colx=1) == '铅笔裤':
            pencil_pants += int(Jan.cell_value(rowx=rx, colx=4))

    num += Jan.nrows
    avg = total / num

print('总销售额', money)

print('平均每日销售数量', avg)

print('羽绒服占比', down_jacket/total)
print('牛仔裤占比', jeans/total)
print('风衣占比', dust_coat/total)
print('皮草占比', fur/total)
print('T血占比', T_shirt/total)
print('马甲占比', best/total)
print('小西装占比', suits/total)
print('皮衣占比', fur_clothing/total)
print('休闲裤占比', casual_pants/total)
print('卫衣占比', fleece/total)
print('衬衫占比', blouse/total)
print('棉衣占比', cotton/total)
print('铅笔裤占比', pencil_pants/total)