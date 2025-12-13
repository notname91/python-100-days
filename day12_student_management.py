# 学生类模板
class Student:
    def __init__(self, student_id, name, age):
        # 你的代码：初始化属性，合理使用封装
        self.student_id = student_id
        self.name = name
        self.age = age
        self.__scores = {}

        print(f'创建学生：{self.name} (学号：{self.student_id})')

    # 封装：成绩应该是私有属性
    def add_score(self, course, score):
        """添加成绩"""
        if not isinstance(score, (int, float)) or score < 0 or score > 100:
            print(f"❌ {course}成绩无效：必须是0-100的数字")
            return False
        # not isinstance(score, (int, float))：
        # 判断score的类型是否不是整数（int）或浮点数（float）

        self.__scores[course] = score
        # 字典添加值
        print(f"✅ {self.name}的{course}成绩：{score}分")
        return True
    
    def get_average_score(self):
        """计算平均分"""
        if not self.__scores:
            print(f"⚠️ {self.name}还没有任何成绩")
            return 0
        
        total = sum(self.__scores.values())
        average = total / len(self.__scores)
        return round(average, 2)
    
    def get_course_count(self):
        """补充：获取已修课程数量（解决未定义问题）"""
        return len(self.__scores)

    def __len__(self):
        return len(self.__scores)
    
    # 特殊方法
    def __str__(self):
        """返回学生信息字符串"""
        avg_score = self.get_average_score()
        course_count = self.get_course_count()
        return f"👤 {self.name}（学号：{self.student_id}，{self.age}岁）平均分：{avg_score}，课程数：{course_count}"
    
    def __repr__(self):
        """返回开发者友好的表示"""
        return f"Student('{self.student_id}', '{self.name}', '{self.age}'"
    
    def __eq__(self, other):
        """比较两个学生是否相同（学号相同）"""
        if not isinstance(other, Student):
            return False
        return self.student_id == other.student_id and self.name == other.name
    
    def __lt__(self, other):
        """比较学生平均分大小（用于排序）"""
        if not isinstance(other, Student):
            return TypeError("只能与Student对象比较")
        return self.get_average_score() < other.get_average_score()
    
    def __len__(self):
        """返回学生已修课程数量"""
        return self.get_course_count()

# 班级类模板
class Classroom:
    def __init__(self, class_name):
        # 你的代码
        self.class_name =class_name
        self.__students = []

        print(f"🏫 创建班级：{self.class_name}")
    
    def add_student(self, student):
        """添加学生"""
        if not isinstance(student, Student):
            print("❌ 只能添加Student对象")
            return False
        
        # 检查学号是否重复
        for s in self.__students:
            if s.student_id == student.student_id:
                print(f"❌ 学号{student.student_id}已存在")
                return False
        
        self.__students.append((student))
        print(f"✅ 添加学生：{student.name} 到 {self.class_name}")
        return True
    
    def find_student(self, student_id):
        """根据学号查找学生，返回学生对象或None"""
        for student in self.__students:
            if student.student_id == student_id:
                return student
        return None
    
    # 特殊方法
    def __len__(self):
        """返回班级学生数量"""
        return len(self.__students)
    
    def __contains__(self, student_id):
        """检查学生是否在班级中"""
        for student in self.__students:
            if student.student_id == student_id:
                return True
        return False
    
    def __iter__(self):
        """使班级可迭代"""
        return iter(self.__students)
    
    def __getitem__(self, index):
        """通过学号获取学生"""
        if isinstance(index, int):
            # 整数索引
            if 0 <= index < len(self.__students):
                return self.__students[index]
            else:
                raise IndexError("索引超出范围")
        elif isinstance(index, str):
            # 字符串索引（按学号查找）
            student = self.find_student(index)
            if student:
                return student
            else:
                raise KeyError(f"未找到学号为{index}的学生")
        else:
            raise TypeError("索引必须是整数或字符串")


# 测试代码
# 创建学生
stu1 = Student("001", "张三", 18)
stu2 = Student("002", "李四", 17)
stu3 = Student("001", "王五", 18)  # 学号与stu1重复

# 学生添加成绩
stu1.add_score("数学", 90)
stu1.add_score("语文", 85)
stu2.add_score("数学", 88)

# 创建班级
cls = Classroom("高一(1)班")

# 添加学生
cls.add_student(stu1)
cls.add_student(stu2)
cls.add_student(stu3)  # 学号重复，添加失败

# 测试特殊方法
print(len(stu1))  # 输出：2（两门课程）
print(stu1)  # 输出学生信息字符串
print(repr(stu1))  # 输出开发者友好的表示
print(stu1 < stu2)  # 比较平均分
print(len(cls))  # 输出：2（两名学生）
print("001" in cls)  # 输出：True
print(cls[0])  # 输出第一个学生对象
print(cls["002"])  # 输出学号为002的学生对象