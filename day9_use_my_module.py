# 第9天：使用自己创建的模块
print("🔧 使用自己创建的计算器模块")
print("=" * 50)

# 导入我们刚才创建的模块
import my_calculator as calc

print("1. 使用计算器模块的函数：")
print(f"   12 + 8 = {calc.add(12, 8)}")
print(f"   20 - 9 = {calc.subtract(20, 9)}")
print(f"   6 × 7 = {calc.multiply(6, 7)}")
print(f"   15 ÷ 3 = {calc.divide(15, 3)}")
print(f"   15 ÷ 0 = {calc.divide(15, 0)}")

print("\n2. 使用判断函数：")
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"   检查数字 {numbers}：")
for num in numbers:
    even_status = "偶数" if calc.is_even(num) else "奇数"
    prime_status = "质数" if calc.is_prime(num) else "合数"
    print(f"     {num}: {even_status}, {prime_status}")

print("\n3. 创建一个简单的计算器程序：")
while True:
    print("\n请选择运算：")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    print("5. 退出")
    
    choice = input("请输入选择：")
    
    if choice == "5":
        print("👋 退出计算器")
        break
    
    try:
        num1 = float(input("第一个数字："))
        num2 = float(input("第二个数字："))
        
        if choice == "1":
            result = calc.add(num1, num2)
            operator = "+"
        elif choice == "2":
            result = calc.subtract(num1, num2)
            operator = "-"
        elif choice == "3":
            result = calc.multiply(num1, num2)
            operator = "×"
        elif choice == "4":
            result = calc.divide(num1, num2)
            operator = "÷"
        else:
            print("❌ 无效选择")
            continue
        
        print(f"✅ {num1} {operator} {num2} = {result}")
        
    except ValueError:
        print("❌ 请输入有效的数字")
    except Exception as e:
        print(f"❌ 发生错误：{e}")

