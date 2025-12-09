# data_storage.py - 数据存储模块
import json
import os

class DataStorage:
    """数据存储类，负责保存和加载数据"""
    
    def __init__(self, filename="people_data.json"):
        self.filename = filename
        self.people = []
    
    def save_person(self, person):
        """保存一个人到列表"""
        self.people.append(person.to_dict())
        print(f"✅ 已保存 {person.name} 的信息")
    
    def save_to_file(self):
        """保存所有数据到文件"""
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(self.people, f, ensure_ascii=False, indent=2)
            print(f"✅ 数据已保存到 {self.filename}")
            return True
        except Exception as e:
            print(f"❌ 保存失败：{e}")
            return False
    
    def load_from_file(self):
        """从文件加载数据"""
        try:
            if not os.path.exists(self.filename):
                print(f"📭 数据文件不存在，将创建新文件")
                return True
                
            with open(self.filename, "r", encoding="utf-8") as f:
                self.people = json.load(f)
            print(f"✅ 已从 {self.filename} 加载数据")
            return True
        except Exception as e:
            print(f"❌ 加载失败：{e}")
            return False
    
    def display_all(self):
        """显示所有人员信息"""
        if not self.people:
            print("📭 还没有人员信息")
            return
        
        print(f"\n📋 所有人员信息（共{len(self.people)}人）：")
        for i, person_data in enumerate(self.people, 1):
            print(f"\n  {i}. {person_data['name']}，{person_data['age']}岁")
            if person_data['hobbies']:
                print(f"     爱好：{', '.join(person_data['hobbies'])}")

# 模块测试
if __name__ == "__main__":
    print("🧪 测试DataStorage模块：")
    storage = DataStorage("test_data.json")
    storage.load_from_file()
    storage.display_all()
