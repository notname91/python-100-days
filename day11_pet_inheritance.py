class Pet:

    def __init__(self ,name ,age):
        self.name = name
        self.age = age
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    def status(self):
        print(f"\n{self.name}的状态：")
        print(f"  饥饿度：{self.hunger}/100")
        print(f'  快乐度：{self.happiness}/100')
        print(f'  精力：{self.energy}/100')

    def feed(self):
        self.hunger -= 20
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name}吃饱了！")

    def play(self):
        self.happiness += 40
        if self.happiness > 100:
            self.happiness = 100
        print(f"和{self.name}玩得很开心！")


class DogPet(Pet):

    def __init__(self, name, age ,breed):
        super().__init__(name, age)
        self.breed = breed
        self.tricks = []

    def bark(self):
        print(f'{self.name}:汪汪汪！')

    def make_sound(self):
        self.bark()

    def learn_trick(self ,trick_name):
        self.tricks.append(trick_name)
        self.happiness += 10
        print(f'{self.name}学会了新把戏：{trick_name}!')

    def show_trick(self):
        if self.tricks:
            print(f"{self.name}会的把戏：{','.join(self.tricks)}")
        else:
            print(f'{self.name}还不会任何把戏！')

    #重写play方法：狗玩的方式不同
    def play(self):
        print(f"和{self.name}玩接球游戏")
        self.happiness += 30
        self.energy -= 20


class CatPet(Pet):

    def __init__(self, name, age ,color):
        super().__init__(name, age)
        self.color = color
        self.mice_caught = 0

    def purr(self):
        print(f"{self.name}：呼噜呼噜~")

    def make_sound(self):
        print(f"{self.name}:喵喵~")

    def hunt(self):
        import random
        if random.random() > 0.5:
            self.mice_caught += 1
            print(f'{self.name}抓到一只老鼠！总共抓了{self.mice_caught}只！')
        else:
            print(f'{self.name}这次没抓到老鼠！')

    def play(self):
        print(f'用毛线球逗{self.name}玩！')
        self.happiness += 25
        self.energy -= 15


class BirdPet(Pet):

    def __init__(self, name, age ,wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def fly(self):
        self.energy -= 15
        self.happiness += 10
        self.hunger += 10
        print(f"{self.name}正在飞行！")

    def sing(self):
        self.happiness += 15
        self.energy -= 15
        print(f'{self.name}正在唱歌！')

    def make_sound(self):
        self.sing()

    def play(self):
        print(f"带{self.name}去公园遛弯玩！")
        self.happiness += 30
        self.energy -= 15





class Zoo:
    """动物园类，管理所有动物"""
    
    def __init__(self, name):
        self.name = name
        self.animals = []  # 存储所有动物
    
    def add_animal(self, animal):
        """添加动物"""
        self.animals.append(animal)
        print(f"✅ 添加了{animal.name}到{self.name}")
    
    def show_all_animals(self):
        """显示所有动物"""
        print(f"\n🏞️ {self.name}的所有动物：")
        for animal in self.animals:
            animal_type = type(animal).__name__
            print(f"  - {animal.name}（{animal_type}）")
    
    def make_all_sounds(self):
        """让所有动物发出声音"""
        print("\n🎵 动物园声音：")
        for animal in self.animals:
            if hasattr(animal, "make_sound"):       
                animal.make_sound()
            else:
                print(f'{self.name}不会发出声音！')
        

# ============================================
# 完整的测试代码
# ============================================
print("🎮 第11天：继承和多态完整测试")
print("=" * 50)

# 创建一个动物园
my_zoo = Zoo("快乐动物园")

# 创建各种宠物并添加到动物园
print("\n1. 创建并添加动物到动物园：")
dog1 = DogPet("旺财", 2, "金毛")
cat1 = CatPet("咪咪", 1, "橘色")
dog2 = DogPet("小黑", 3, "泰迪")
bird1 = BirdPet("小黄", 1, "30cm")

my_zoo.add_animal(dog1)
my_zoo.add_animal(cat1)
my_zoo.add_animal(dog2)
my_zoo.add_animal(bird1)

# 显示所有动物
print("\n2. 显示动物园所有动物：")
my_zoo.show_all_animals()

# 测试多态性
print("\n3. 测试多态性（每个动物玩的方式不同）：")
for animal in my_zoo.animals:
    print(f"\n--- 和{animal.name}玩耍 ---")
    animal.play()
    animal.status()

# 测试特有功能
print("\n4. 测试各动物的特有功能：")
for animal in my_zoo.animals:
    if isinstance(animal, DogPet):
        animal.learn_trick("握手")
        animal.learn_trick("趴下")
        animal.show_trick()
    elif isinstance(animal, CatPet):
        animal.hunt()
        animal.purr()
    elif isinstance(animal, BirdPet):
        animal.fly()
        animal.sing()

# 测试动物园的统一管理功能
print("\n5. 动物园统一管理功能：")
my_zoo.make_all_sounds()

print("\n🎉 继承和多态测试完成！")