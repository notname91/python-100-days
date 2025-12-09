#my_calculate.py - 我的计算模块
#这是一个简单的计算器模板，包括一些数学函数

def add(a,b):
    """加法函数"""
    return a + b

def subtract(a,b):
    """减法函数"""
    return a - b

def multiply(a,b):
    """乘法函数"""
    return a * b

def divide(a,b):
    """除法函数，处理除零错误"""
    if b == 0:
        return "错误：除数不能为零"
    return a / b

def is_even(number):
    """判断是否是偶数"""
    return number % 2 == 0

def is_prime(number):
    """判断是否为质数"""
    if number <= 1:
        return False
    for i in range(2,int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# 模块的测试代码
if __name__ == "__main__":
    print("🧮 测试我的计算器模块：")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 × 7 = {multiply(6, 7)}")
    print(f"8 ÷ 2 = {divide(8, 2)}")
    print(f"8 ÷ 0 = {divide(8, 0)}")
    print(f"4是偶数吗？{'是' if is_even(4) else '不是'}")
    print(f"7是质数吗？{'是' if is_prime(7) else '不是'}")
