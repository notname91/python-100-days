# person_module.py - 个人信息模块

class Person:
    """人类，表示一个人的信息"""
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.hobbies = []
    
    def add_hobby(self, hobby):
        """添加爱好"""
        self.hobbies.append(hobby)
        print(f"✅ 已为{self.name}添加爱好：{hobby}")
    
    def display_info(self):
        """显示个人信息"""
        print(f"\n👤 个人信息：")
        print(f"   姓名：{self.name}")
        print(f"   年龄：{self.age}")
        print(f"   邮箱：{self.email}")
        if self.hobbies:
            print(f"   爱好：{', '.join(self.hobbies)}")
        else:
            print(f"   爱好：暂无")
    
    def to_dict(self):
        """转换为字典，方便存储"""
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "hobbies": self.hobbies
        }
    
    @classmethod
    def from_dict(cls, data):
        """从字典创建Person对象"""
        person = cls(data["name"], data["age"], data["email"])
        person.hobbies = data["hobbies"]
        return person

# 模块测试
if __name__ == "__main__":
    print("🧪 测试Person模块：")
    p1 = Person("张三", 25, "zhangsan@example.com")
    p1.add_hobby("编程")
    p1.add_hobby("阅读")
    p1.display_info()