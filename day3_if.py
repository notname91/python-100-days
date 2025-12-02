#学习程序做决定
print("第三天：学习程序做决定")
print("=" * 40)

#1.最简单的判断
print("例1：判断数字大小")

数字 = 10

#if 是“如果”的意思
if 数字 > 5:
    print("这个数字大于5")

print("判断结束")

print("/n" + "=" * 30)
print("例2：如果...否则...")

#if...else 结构
年龄 = int(input("请输入你的年龄："))

if 年龄 >= 18:
    print("你是成年人")
else:
    print("你是未成年人")

print("/n" + "=" * 30)
print("例3：多个条件")

#判断成绩等级
分数 = int(input("请输入你的成绩："))

if 分数 >=90:
    print("太棒了！")
elif 分数 >=80:
    print("良好！不错！")
elif 分数 >=60:
    print("及格！继续加油！")
else:
    print("不及格了，要加油了！")
