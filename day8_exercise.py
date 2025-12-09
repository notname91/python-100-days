# 练习：安全计算器
print("🧮 安全计算器练习")
print("=" * 40)

def safe_calculator():
    """安全的四则运算计算器"""
    while True:
        print("\n请选择运算：")
        print("1. 加法")
        print("2. 减法")
        print("3. 乘法")
        print("4. 除法")
        print("5. 退出")
        
        choice = input("请输入选择（1-5）：")
        
        if choice == "5":
            print("👋 退出计算器")
            break
        
        # TODO: 添加异常处理，确保输入的是1-5的数字
        try:
            choice_num = int(choice)
            if choice_num < 1 or choice_num > 5:
                print("❌ 请输入1-5之间的数字")
                continue
        except ValueError:
            print("❌ 请输入数字！")
            continue
        
        try:
            # TODO: 获取两个数字输入
            num1 = float(input("请输入第一个数字："))
            num2 = float(input("请输入第二个数字："))
            
            # TODO: 根据选择进行运算
            if choice == "1":
                result = num1 + num2
                operator = "+"
            elif choice == "2":
                result = num1 - num2
                operator = "-"
            elif choice == "3":
                result = num1 * num2
                operator = "×"
            elif choice == "4":
                # TODO: 处理除数为0的情况
                if num2 == 0:
                    print("❌ 除数不能为0！")
                    continue
                result = num1 / num2
                operator = "÷"
            
            # TODO: 显示计算结果
            print(f"✅ {num1} {operator} {num2} = {result}")
            
        except ValueError:
            print("❌ 请输入有效的数字！")
        except Exception as e:
            print(f"❌ 发生未知错误：{e}")
        else:
            print("✅ 计算成功！")
        finally:
            print("=" * 30)

# TODO: 调用函数运行计算器
# 提示：添加 if __name__ == "__main__": 判断
if __name__ == "__main__":
    safe_calculator()