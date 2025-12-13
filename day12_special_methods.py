# day12_special_methods.py - 特殊方法学习
print("✨ 第12天：特殊方法（魔法方法）")
print("=" * 50)

print("\n🌟 什么是特殊方法？")
print("   特殊方法 = 让类更智能的方法")
print("   格式：__方法名__（双下划线包围）")
print("   作用：让我们的对象像内置对象一样工作")

# ============================================
# 1. __str__ 和 __repr__ 方法
# ============================================
print("\n🌟 __str__ 和 __repr__ 方法：")

class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __repr__(self):
        return f"《{self.title}》 - {self.author} - ￥{self.price}"
    
    def __len__(self):
        return int(self.price)
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other
    
    def __add__(self, other):
        if isinstance(other, Book):
            return self.price + other.price
        elif isinstance(other, (int, float)):
            return self.price + other
        else:
            raise TypeError("只能与Book或数字相加")
        
print("\n1. 创建图书对象：")
book1 = Book('Python编程从入门到实践',"Eric Matthes",89.9)
book2 = Book("流畅的Python","Luciano Ramalho",119.0)

print("   使用__str__（用户友好）：")
print(f"   {book1}")  # 自动调用 __str__
print(f"   {book2}")

print("\n   使用__repr__（开发者友好）：")
print(f"   {repr(book1)}")  # 显示如何创建这个对象
print(f"   {repr(book2)}")

print("\n   使用__len__：")
print(f"   《{book1.title}》的长度值：{len(book1)}")
print(f"   《{book2.title}》的长度值：{len(book2)}")

print("\n   使用__eq__比较：")
book3 = Book("Python编程从入门到实践", "Eric Matthes", 89.9)
print(f"   book1 == book3？{book1 == book3}")
print(f"   book1 == book2？{book1 == book2}")

print("\n   使用__add__相加：")
print(f"   book1 + book2 = {book1 + book2}元")
print(f"   book1 + 10 = {book1 + 10}元")
    
# ============================================
# 2. 更多特殊方法示例
# ============================================
print("\n🌟 更多特殊方法示例：")

class ShoppingCart:

    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, item, price):
        self.items.append((item, price))
        self.total += price

    def __len__(self):
        return len(self.items)
    
    def __contains__(self, item_name):
        for item,_ in self.items:
            if item == item_name:
                return True
        return False
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __call__(self):
        print(f"购物车中有{len(self)}件商品,总价：￥{self.total}")
        

print("\n2. 购物车特殊方法演示：")
cart = ShoppingCart()
cart.add_item("Python书", 89.9)
cart.add_item("鼠标", 199.0)
cart.add_item("键盘", 299.0)

print(f"   购物车长度（__len__）：{len(cart)}件商品")
print(f"   检查包含（__contains__）：'Python书'在购物车中吗？{'Python书' in cart}")
print(f"   检查包含（__contains__）：'显示器'在购物车中吗？{'显示器' in cart}")

print("\n   迭代购物车（__iter__）：")
for item, price in cart:
    print(f"      - {item}: ¥{price}")

print("\n   索引访问（__getitem__）：")
print(f"      第1件商品：{cart[0]}")
print(f"      最后1件商品：{cart[-1]}")

print("\n   调用对象（__call__）：")
cart()  # 像函数一样调用

print("\n🎉 特殊方法学习完成！") 