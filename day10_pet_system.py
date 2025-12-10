# ============= 宠物养成系统 - 详细教学版 =============
# day10_pet_system.py


class Pet:
    """宠物类 — 就像创建一个宠物的蓝图"""

    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        
        print(f'宠物{self.name}创建成功！')

    def status(self):
        """显示宠物的当前状态"""

        print(f'\n{self.name}的状态报告：')
        print('-' * 30)

        # 使用表情符号表示状态
        hunger_emoji = "😋" if self.hunger < 30 else ("😐" if self.hunger < 70 else "😫")
        happiness_emoji = "😄" if self.happiness > 70 else ("😊" if self.happiness > 30 else "😔")
        energy_emoji = "⚡" if self.energy > 70 else ("🔋" if self.energy > 30 else "😴")

        print(f"{hunger_emoji} 饥饿度：{self.hunger}/100")
        print(f"{happiness_emoji} 快乐度：{self.happiness}/100")
        print(f"{energy_emoji} 精力：{self.energy}/100")

        #给出建议
        if self.hunger > 70:
            print('建议：宠物饿了，需要喂食！')
        if self.happiness <30:
            print("建议：宠物不开心，陪它玩吧！")
        if self.energy < 30:
            print("建议：宠物累了，让它休息一下吧！")

    def feed(self):
        """ 喂宠物吃东西"""
        print(f'\n 正在喂{self.name}吃东西...')

        #喂食效果
        self.hunger -= 30
        if self.hunger < 0:
            self.hunger = 0

        self.energy += 10
        print(f"{self.name}吃饱了！饥饿度下降，精力恢复一点！")

    def play(self):
        """和宠物玩耍"""
        print(f"\n 正在和{self.name}玩耍...")

        #玩耍效果
        self.happiness += 40
        if self.happiness > 100:
            self.happiness = 100

        self.energy -= 30
        self.hunger += 20

        print(f"玩得很开心！快乐大幅提升，但也消耗了体力和精力！")

    def sleep(self):
        """让宠物睡觉"""
        print(f'\n {self.name}正在睡觉！')

        #睡觉效果
        self.energy += 60
        if self.energy > 100:
            self.energy = 100

        self.hunger -= 10

        print(f'{self.name}睡醒了，精力充沛！')

    def train(self):
        """训练宠物"""
        print(f"你的宠物{self.name}正在训练！")

        #训练效果
        self.energy += 60
        if self.energy < 30:
            self.energy = 30

        self.happiness += 30
        self.hunger -= 60

        print(f'{self.name}训练完成，消耗大量精力，增加了一点快乐度，饥饿度大量增加！')

    def get_mood(self):
        """获取宠物心情"""
        #计算平均状态
        average = (self.happiness + (100 - self.hunger) + self.energy) / 3

        # 根据平均值返回不同的心情
        if average > 80:
            return "😄 超级开心！"
        elif average > 60:
            return "😊 心情不错"
        elif average > 40:
            return "😐 一般般"
        elif average > 20:
            return "😕 有点不开心"
        else:
            return "😢 非常不开心"
        


# ============= 创建宠物并测试 =============
print("🎮 欢迎来到宠物养成系统！")
print("=" * 50)

# 创建一只狗
print("\n第一步：创建宠物")
my_dog = Pet("旺财", "狗", 2)

# 查看初始状态
print("\n第二步：查看宠物状态")
my_dog.status()

# 进行一些互动
print("\n第三步：与宠物互动")
my_dog.feed()      # 喂食
my_dog.play()      # 玩耍
my_dog.sleep()     # 睡觉

# 查看最终状态
print("\n第四步：查看互动后的状态")
my_dog.status()

print("\n🎉 基础宠物系统完成！")