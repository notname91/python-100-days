# 第7天项目：个人日记本程序
import datetime
import os  # 导入操作系统模块，用于文件操作

print("📔 个人日记本程序")
print("=" * 50)

# 定义日记文件名
DIARY_FILE = "my_diary.txt"

def get_current_time():
    """获取当前日期时间"""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def add_new_entry():
    """添加新日记"""
    print("\n📝 写新日记")
    print("-" * 30)
    
    # 自动获取当前时间
    current_time = get_current_time()
    print(f"当前时间：{current_time}")
    
    # 获取日记内容
    weather = input("请输入天气：")
    mood = input("请输入心情：")
    content = input("请输入日记内容：\n")
    
    # ==== 这里是需要添加的代码 ====
    # 打开文件并追加内容
    # 'a' 表示追加模式，不会覆盖原有内容
    # encoding='utf-8' 确保中文正常保存
    with open(DIARY_FILE, "a", encoding="utf-8") as file:
        # 写入日记，格式为：
        # [时间] 天气：xxx 心情：xxx
        # 内容：xxx
        # ----------
        file.write(f"[{current_time}] 天气：{weather} 心情：{mood}\n")
        file.write(f"内容：{content}\n")
        file.write("-" * 40 + "\n")  # 分隔线
        
    print("✅ 日记已保存！")
    # =============================

def view_all_entries():
    """查看所有日记"""
    print("\n📖 所有日记")
    print("=" * 50)
    
    # ==== 这里是需要添加的代码 ====
    try:
        # 尝试打开文件
        with open(DIARY_FILE, "r", encoding="utf-8") as file:
            content = file.read()  # 读取所有内容
            
            if content:  # 如果内容不为空
                print(content)
            else:  # 文件存在但是空的
                print("📭 日记本是空的，快写第一篇日记吧！")
                
    except FileNotFoundError:
        # 文件不存在的情况
        print("📭 还没有日记，请先写日记吧！")
    # =============================

def search_by_date():
    """按日期搜索日记"""
    date = input("\n请输入要搜索的日期（格式：2024-01-01）：")
    
    # ==== 这里是需要添加的代码 ====
    try:
        found = False  # 标记是否找到
        with open(DIARY_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()  # 读取所有行
            
            for i in range(len(lines)):
                # 查找包含日期的行
                if date in lines[i]:
                    found = True
                    print("\n找到日记：")
                    print("=" * 40)
                    # 显示这篇日记（通常包含3行：时间行、内容行、分隔行）
                    for j in range(i, min(i+3, len(lines))):
                        print(lines[j], end="")
                    print("=" * 40)
                    
        if not found:
            print(f"❌ 没有找到{date}的日记")
            
    except FileNotFoundError:
        print("📭 还没有日记，请先写日记吧！")
    # =============================

def count_entries():
    """统计日记数量"""
    # ==== 这里是需要添加的代码 ====
    try:
        count = 0
        with open(DIARY_FILE, "r", encoding="utf-8") as file:
            for line in file:
                # 统计以"["开头的时间行（每篇日记的开头）
                if line.startswith("["):
                    count += 1
        
        print(f"\n📊 共有 {count} 篇日记")
        
    except FileNotFoundError:
        print("📭 还没有日记，请先写日记吧！")
    # =============================

def delete_diary():
    """删除日记文件"""
    confirm = input("\n⚠️  确定要删除所有日记吗？(y/n): ")
    if confirm.lower() == 'y':
        # ==== 这里是需要添加的代码 ====
        try:
            # 使用os模块删除文件
            os.remove(DIARY_FILE)
            print("✅ 日记已删除")
        except FileNotFoundError:
            print("❌ 日记文件不存在")
        # =============================
    else:
        print("❌ 取消删除")

# 主程序
def main():
    while True:
        print("\n请选择操作：")
        print("1. 写新日记")
        print("2. 查看所有日记")
        print("3. 按日期搜索")
        print("4. 统计日记数量")
        print("5. 删除所有日记")
        print("6. 退出程序")
        
        choice = input("请输入数字选择：")
        
        if choice == "1":
            add_new_entry()
        elif choice == "2":
            view_all_entries()
        elif choice == "3":
            search_by_date()
        elif choice == "4":
            count_entries()
        elif choice == "5":
            delete_diary()
        elif choice == "6":
            print("\n👋 退出日记本程序，再见！")
            break
        else:
            print("❌ 请输入1-6之间的数字")

# 启动程序
if __name__ == "__main__":
    main()
