# 第8天项目：安全银行账户系统
print("🏦 安全银行账户系统")
print("=" * 50)

class BankAccount:
    """银行账户类"""
    
    def __init__(self, account_number, account_name, initial_balance=0):
        """初始化账户"""
        try:
            if not account_number:
                raise ValueError("账户号不能为空")
            if not account_name:
                raise ValueError("账户名不能为空")
            if initial_balance < 0:
                raise ValueError("初始余额不能为负数")
                
            self.account_number = account_number
            self.account_name = account_name
            self.balance = initial_balance
            print(f"✅ 账户创建成功：{account_name} ({account_number})，初始余额：¥{initial_balance:.2f}")
            
        except ValueError as e:
            print(f"❌ 账户创建失败：{e}")
            raise  # 重新抛出异常，让调用者知道创建失败
    
    def deposit(self, amount):
        """存款"""
        try:
            # 检查amount是否为数字
            amount = float(amount)
            
            # 检查amount是否为正数
            if amount <= 0:
                print("❌ 存款金额必须大于0")
                return False
                
            # 更新余额
            old_balance = self.balance
            self.balance += amount
            print(f"✅ 存款成功：¥{amount:.2f}")
            print(f"   原余额：¥{old_balance:.2f} → 新余额：¥{self.balance:.2f}")
            return True
            
        except ValueError:
            print("❌ 请输入有效的数字金额")
            return False
        except Exception as e:
            print(f"❌ 存款失败：{e}")
            return False
    
    def withdraw(self, amount):
        """取款"""
        try:
            # 检查amount是否为数字
            amount = float(amount)
            
            # 检查amount是否为正数
            if amount <= 0:
                print("❌ 取款金额必须大于0")
                return False
                
            # 检查余额是否充足
            if amount > self.balance:
                print(f"❌ 余额不足！当前余额：¥{self.balance:.2f}，取款金额：¥{amount:.2f}")
                return False
                
            # 更新余额
            old_balance = self.balance
            self.balance -= amount
            print(f"✅ 取款成功：¥{amount:.2f}")
            print(f"   原余额：¥{old_balance:.2f} → 新余额：¥{self.balance:.2f}")
            return True
            
        except ValueError:
            print("❌ 请输入有效的数字金额")
            return False
        except Exception as e:
            print(f"❌ 取款失败：{e}")
            return False
    
    def transfer(self, target_account, amount):
        """转账到另一个账户"""
        try:
            # 检查target_account是否存在
            if not target_account:
                print("❌ 目标账户不存在")
                return False
                
            # 检查amount是否为数字且为正数
            amount = float(amount)
            if amount <= 0:
                print("❌ 转账金额必须大于0")
                return False
                
            # 检查余额是否充足
            if amount > self.balance:
                print(f"❌ 余额不足！当前余额：¥{self.balance:.2f}，转账金额：¥{amount:.2f}")
                return False
                
            # 执行转账：从本账户扣除，向目标账户增加
            old_balance_self = self.balance
            old_balance_target = target_account.balance
            
            self.balance -= amount
            target_account.balance += amount
            
            print(f"✅ 转账成功：¥{amount:.2f}")
            print(f"   从 {self.account_name} 转账到 {target_account.account_name}")
            print(f"   本账户余额：¥{old_balance_self:.2f} → ¥{self.balance:.2f}")
            print(f"   目标账户余额：¥{old_balance_target:.2f} → ¥{target_account.balance:.2f}")
            return True
            
        except ValueError:
            print("❌ 请输入有效的数字金额")
            return False
        except AttributeError:
            print("❌ 目标账户无效")
            return False
        except Exception as e:
            print(f"❌ 转账失败：{e}")
            return False
    
    def display_balance(self):
        """显示余额"""
        print(f"💰 账户信息：")
        print(f"   账户名：{self.account_name}")
        print(f"   账号：{self.account_number}")
        print(f"   余额：¥{self.balance:.2f}")
        print(f"   状态：{'正常' if self.balance >= 0 else '透支'}")
        if self.balance < 0:
            print("   ⚠️  警告：账户已透支！")

# 主程序
def main():
    """银行系统主程序"""
    accounts = {}  # 存储所有账户，格式：{account_number: account_object}
    
    # 创建几个示例账户（可选）
    accounts["1001"] = BankAccount("1001", "张三", 1000)
    accounts["1002"] = BankAccount("1002", "李四", 500)
    accounts["1003"] = BankAccount("1003", "王五", 2000)
    
    while True:
        print("\n" + "=" * 50)
        print("请选择操作：")
        print("1. 创建账户")
        print("2. 存款")
        print("3. 取款")
        print("4. 转账")
        print("5. 查询余额")
        print("6. 显示所有账户")
        print("7. 退出系统")
        
        try:
            choice = int(input("请输入选择（1-7）："))
        except ValueError:
            print("❌ 请输入数字！")
            continue
        
        if choice == 1:
            # 创建账户
            print("\n📝 创建新账户")
            print("-" * 30)
            
            try:
                account_number = input("请输入账户号：")
                if account_number in accounts:
                    print(f"❌ 账户号 {account_number} 已存在")
                    continue
                    
                account_name = input("请输入账户名：")
                initial_balance = float(input("请输入初始余额（默认0）：") or "0")
                
                # 创建账户
                account = BankAccount(account_number, account_name, initial_balance)
                accounts[account_number] = account
                print(f"✅ 账户创建完成，已添加到系统")
                
            except ValueError as e:
                print(f"❌ 输入错误：{e}")
            except Exception as e:
                print(f"❌ 创建账户失败：{e}")
        
        elif choice == 2:
            # 存款
            print("\n💰 存款操作")
            print("-" * 30)
            
            account_number = input("请输入账户号：")
            if account_number not in accounts:
                print(f"❌ 账户号 {account_number} 不存在")
                continue
                
            account = accounts[account_number]
            amount = input("请输入存款金额：")
            account.deposit(amount)
        
        elif choice == 3:
            # 取款
            print("\n💰 取款操作")
            print("-" * 30)
            
            account_number = input("请输入账户号：")
            if account_number not in accounts:
                print(f"❌ 账户号 {account_number} 不存在")
                continue
                
            account = accounts[account_number]
            amount = input("请输入取款金额：")
            account.withdraw(amount)
        
        elif choice == 4:
            # 转账
            print("\n🔄 转账操作")
            print("-" * 30)
            
            from_account_number = input("请输入转出账户号：")
            if from_account_number not in accounts:
                print(f"❌ 转出账户 {from_account_number} 不存在")
                continue
                
            to_account_number = input("请输入转入账户号：")
            if to_account_number not in accounts:
                print(f"❌ 转入账户 {to_account_number} 不存在")
                continue
                
            if from_account_number == to_account_number:
                print("❌ 不能向自己转账")
                continue
                
            from_account = accounts[from_account_number]
            to_account = accounts[to_account_number]
            
            amount = input("请输入转账金额：")
            from_account.transfer(to_account, amount)
        
        elif choice == 5:
            # 查询余额
            print("\n📊 查询余额")
            print("-" * 30)
            
            account_number = input("请输入账户号：")
            if account_number not in accounts:
                print(f"❌ 账户号 {account_number} 不存在")
                continue
                
            account = accounts[account_number]
            account.display_balance()
        
        elif choice == 6:
            # 显示所有账户
            print("\n📋 所有账户信息")
            print("=" * 50)
            
            if not accounts:
                print("📭 系统中还没有账户")
            else:
                total_balance = 0
                for acc_num, account in accounts.items():
                    print(f"账户号：{acc_num}")
                    print(f"  账户名：{account.account_name}")
                    print(f"  余额：¥{account.balance:.2f}")
                    print("-" * 30)
                    total_balance += account.balance
                
                print(f"系统总账户数：{len(accounts)}")
                print(f"系统总余额：¥{total_balance:.2f}")
        
        elif choice == 7:
            print("\n" + "=" * 50)
            print("👋 退出银行系统")
            print("感谢使用，再见！")
            break
        else:
            print("❌ 请输入1-7之间的数字")

# 启动程序
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中断程序")
    except Exception as e:
        print(f"\n\n❌ 程序出现未处理的错误：{e}")
    finally:
        print("程序结束")