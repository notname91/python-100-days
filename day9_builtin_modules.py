# 第9天：常用内置模块介绍
print("📚 常用内置模块介绍")
print("=" * 50)

# ============================================
# 1. datetime模块 - 日期和时间
# ============================================
print("\n1. datetime模块 - 日期和时间：")
import datetime

# 获取当前时间
now = datetime.datetime.now()
print(f"   当前时间：{now}")
print(f"   年份：{now.year}")
print(f"   月份：{now.month}")
print(f"   日期：{now.day}")
print(f"   小时：{now.hour}")
print(f"   分钟：{now.minute}")
print(f"   星期几：{now.weekday() + 1}")  # 0=周一，所以要+1

# 格式化时间
formatted = now.strftime("%Y年%m月%d日 %H:%M:%S")
print(f"   格式化时间：{formatted}")

# ============================================
# 2. time模块 - 时间相关
# ============================================
print("\n2. time模块 - 时间相关：")
import time

print("   当前时间戳：", time.time())
print("   程序暂停2秒...")
time.sleep(2)  # 暂停2秒
print("   继续执行！")

# ============================================
# 3. os模块 - 操作系统功能
# ============================================
print("\n3. os模块 - 操作系统功能：")
import os

print(f"   当前工作目录：{os.getcwd()}")
print(f"   当前目录下的文件：")
for file in os.listdir("."):
    if file.endswith(".py"):
        print(f"     📄 {file}")

# 检查文件是否存在
if os.path.exists("my_calculator.py"):
    print("   ✅ my_calculator.py 文件存在")
else:
    print("   ❌ my_calculator.py 文件不存在")

# ============================================
# 4. json模块 - 处理JSON数据
# ============================================
print("\n4. json模块 - 处理JSON数据：")
import json

# 创建一个Python字典
person = {
    "name": "张三",
    "age": 25,
    "city": "北京",
    "hobbies": ["读书", "编程", "运动"]
}

# 将字典转换为JSON字符串
json_string = json.dumps(person, ensure_ascii=False, indent=2)
print("   Python字典转JSON：")
print(json_string)

# ============================================
# 5. 其他有用模块
# ============================================
print("\n5. 其他有用模块：")

# sys模块 - 系统相关
import sys
print(f"   Python版本：{sys.version[:6]}")
print(f"   系统平台：{sys.platform}")

# statistics模块 - 统计功能
import statistics
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"   数据 {data} 的平均值：{statistics.mean(data)}")

# collections模块 - 高级数据结构
from collections import Counter
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print(f"   单词统计：{word_count}")
