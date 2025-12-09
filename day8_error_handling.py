#第八天：错误处理进阶
#学习目标：让程序在遇到错误时不会崩溃，而是优雅的处理

print("第八天：学习完整的错误处理")
print('=' * 40)

#1.try-except-els-fianlly 完整结构
print('\n1.try-except-els-fianlly 完整结构：')

def divide_numbers(a,b):
    '''安全的除法函数'''
    try:
        #尝试执行可能出错的代码
        result = a / b
    except ZeroDivisionError:
        # 如果发生除零错误，执行这里
        print(f' 错误：除数不能为零！')
        return None
    except TypeError:
        #如果发生类型错误（比如用字符串除），执行这里
        print(f' 错误：请输入数字！')
        return None
    else:
        print(' 计算成功！')
        return result
    finally:
        #如果没有发生任何错误，执行这里
        print(f' 计算过程结束')
        print('=' * 30)

# 测试不同的情况
print("测试1：正常除法")
print(f"10 ÷ 2 = {divide_numbers(10, 2)}")

print("\n测试2：除数为0")
print(f"10 ÷ 0 = {divide_numbers(10, 0)}")

print("\n测试3：类型错误")
print(f"10 ÷ 'a' = {divide_numbers(10, 'a')}")

#2.获取异常信息

print('\n2.获取异常信息')

def safe_open_file(filename):
    '''安全的打开文件并读取内容'''
    try:
        with open(filename,'r',encoding = 'utf-8') as file:
            content = file.rede()
            print(f' 文件内容：\n{content}')
    except FileNotFoundError as e:
        # 获取异常的具体信息
        print(f" 文件未找到错误：{e}")
        print(f" 文件 '{filename}' 不存在")
    except PermissionError as e:
        print(f'权限错误：{e}')
        print(f"没有权限读取文件 '{filename}'")
    except Exception as e:
        #捕获所有其他异常
        print(f"未知错误：{type(e).__name__}:{e}")
    else:
        print("文件读取成功")
    finally:
        print("文件操作结束")

# 测试文件操作
print("\n测试文件操作：")
safe_open_file("day8_test.txt")  # 这个文件不存在

#3.自定义异常信息
print('\n3.自定义异常信息:')

def check_age(age):
    '''检查年龄是否合法'''
    try:
        if age < 0:
            # 使用 raise 主动抛出异常
            raise ValueError("年龄不能为负数！")
        elif age > 150:
            raise ValueError('年龄不能超过150岁！')
        elif age < 18:
            print(f"你{age}岁，是未成年人")
        else:
            print(f"你{age}岁，是成年人")
    except ValueError as e:
        print(f"输入错误：{e}")
    else:
        print("年龄检查完成")
    finally:
        print("年龄检查结束")

# 测试年龄检查
print("\n测试年龄检查：")
check_age(25)
check_age(-5)
check_age(200)
check_age(16)
