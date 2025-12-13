# day12_encapsulation.py - 封装基础
print("🔒 第12天：封装和特殊方法")
print("=" * 50)

print("\n🌟 什么是封装？")
print("   封装 = 数据保护 + 隐藏实现细节")
print("   就像银行账户：")
print("   - 你不能直接修改余额")
print("   - 必须通过存款、取款等方法来操作")
print("   - 内部实现细节对外部隐藏")

# ============================================
# 1. 没有封装的银行账户（有问题）
# ============================================
print("\n❌ 问题示例：没有封装的银行账户")

class BadBankAccount:
    """不好的银行账户类 - 没有封装"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner      # 账户持有人
        self.balance = balance  # 余额（直接公开访问，不安全！）

# 创建账户
account1 = BadBankAccount("张三", 1000)
print(f"初始状态：{account1.owner} 有 {account1.balance}元")

# 问题：可以直接修改余额，不安全！
account1.balance = 1000000  # 直接变成百万富翁！
print(f"修改后：{account1.owner} 有 {account1.balance}元")
print("⚠️ 问题：余额可以被任意修改，不安全！")

# ============================================
# 2. 使用封装的银行账户
# ============================================
print("\n" + "=" * 50)
print("✅ 正确示例：使用封装的银行账户")

class BankAccount:
    """好的银行账户类 - 使用封装"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner          # 公开属性
        self.__balance = balance    # 私有属性（双下划线开头）
        self.__transaction_history = []  # 交易记录也是私有的
        print(f"✅ 为{self.owner}创建账户，初始余额：{self.__balance}元")
    
    # 公共方法：存款
    def deposit(self, amount):
        """存款"""
        if amount <= 0:
            print("❌ 存款金额必须大于0")
            return False
        
        self.__balance += amount
        self.__record_transaction(f"存款 {amount}元")
        print(f"✅ {self.owner}存款{amount}元，当前余额：{self.__balance}元")
        return True
    
    # 公共方法：取款
    def withdraw(self, amount):
        """取款"""
        if amount <= 0:
            print("❌ 取款金额必须大于0")
            return False
        
        if amount > self.__balance:
            print(f"❌ 余额不足！当前余额：{self.__balance}元")
            return False
        
        self.__balance -= amount
        self.__record_transaction(f"取款 {amount}元")
        print(f"✅ {self.owner}取款{amount}元，当前余额：{self.__balance}元")
        return True
    
    # 公共方法：查看余额（只读）
    def get_balance(self):
        """获取余额"""
        return self.__balance
    
    # 公共方法：查看账户信息
    def get_account_info(self):
        """获取账户信息"""
        return {
            "owner": self.owner,
            "balance": self.__balance,
            "transaction_count": len(self.__transaction_history)
        }
    
    # 私有方法：记录交易（外部不能直接调用）
    def __record_transaction(self, description):
        """记录交易（私有方法）"""
        import datetime
        transaction = {
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "description": description
        }
        self.__transaction_history.append(transaction)
    
    # 公共方法：查看最近交易（有限访问）
    def get_recent_transactions(self, count=5):
        """获取最近交易记录"""
        recent = self.__transaction_history[-count:] if self.__transaction_history else []
        return recent

# ============================================
# 3. 测试封装的银行账户
# ============================================
print("\n🌟 测试封装的银行账户：")

# 创建账户
my_account = BankAccount("李四", 5000)
print(f"账户持有人：{my_account.owner}")

# 正常操作
print("\n1. 正常存款：")
my_account.deposit(1000)

print("\n2. 正常取款：")
my_account.withdraw(2000)

print("\n3. 尝试取款超过余额：")
my_account.withdraw(5000)

# 查看余额（只能通过方法）
print(f"\n4. 查看余额：{my_account.get_balance()}元")

# 查看账户信息
print("\n5. 账户信息：")
info = my_account.get_account_info()
for key, value in info.items():
    print(f"   {key}: {value}")

# 测试私有属性保护
print("\n6. 测试私有属性保护：")
try:
    # 尝试直接访问私有属性
    print(f"尝试访问私有余额：{my_account.__balance}")
except AttributeError as e:
    print(f"❌ 访问失败：{e}")
    print("✅ 私有属性被成功保护！")

# 测试私有方法保护
print("\n7. 测试私有方法保护：")
try:
    # 尝试直接调用私有方法
    my_account.__record_transaction("测试")
except AttributeError as e:
    print(f"❌ 调用失败：{e}")
    print("✅ 私有方法被成功保护！")

print("\n🎉 封装基础学习完成！")