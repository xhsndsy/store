import random

guess = input("请输入你要猜的数")
rand = random.randint(0,90)

times = 0
while rand != int(guess) | times == 10:


    if rand > int(guess):
        print("这个数比", guess, "大")
    elif rand < int(guess):
        print("这个数比", guess, "小")
    guess = input("请输入你要猜的数")

    times = times + 1
if rand == int(guess):
     print("猜对了")

if times == 10:
    print("次数到达上线了")


