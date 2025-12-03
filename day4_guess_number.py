import random

print("🎮 猜数字游戏")
print("=" * 40)
print("电脑已经想好了一个1-100之间的数字")
print("你有10次机会猜中它，开始吧！")
print("=" * 40)


num = random.randint(1,100)

for i in range(0,10):

    print(f"\n第{i}次尝试，还剩{10 - i}次机会")

    try:
        guess_num = int(input("请输入你猜测的数字：")) 
    except:
        print("请输入有效的数字！")
        continue

    if guess_num < 1 or guess_num > 100:
        print("请输入1-100内的数字")
        continue

    if guess_num < num:
        print("猜小了，再大一点！")
    elif guess_num > num:
        print("猜大了，再小一点！")
    else:
        print(f"恭喜你猜对了！！！答案就是{num}")
        print(f"你用了{i}次就猜对了")
        break




else:
    print(f"\n 很遗憾，机会已经用完了。\n答案是{num}！")
    
print(f"\n" + "=" * 40)
print("游戏结束，感谢游玩！！！")
        

