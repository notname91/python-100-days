# 练习2：学生成绩管理系统
print("\n📊 学生成绩管理系统")
print("=" * 40)

def manage_student_scores():
    """管理学生成绩"""
    scores = {}  # 用字典存储学生成绩
    
    while True:
        print("\n请选择操作：")
        print("1. 添加学生成绩")
        print("2. 查看所有成绩")
        print("3. 删除学生成绩")
        print("4. 计算平均分")
        print("5. 退出")
        
        choice = input("请输入选择：")
        
        if choice == "1":
            # TODO: 添加学生成绩
            # 要求：处理学生姓名输入（不能为空）
            #       处理成绩输入（必须是0-100的数字）
            try:
                name =input("请输入学生名字：").strip()
                if not name:
                    print("名字不能为空！")
                    continue
                elif name in scores:
                    print(f"{name}的成绩已存在，即将覆盖原有成绩")
            
                scores_input = input('请输入该学生成绩：(0-100)').strip()
                if not scores_input:
                    print("成绩不能为空")
                    continue

                score = float(scores_input)

                if score < 0 or score > 100:
                    print("成绩只能在0-100！")
                    continue

                scores[name] = score
                print("添加成功")

            except ValueError:
                print("请输入有效的数字！")
            
        
        elif choice == "2":
            # TODO: 显示所有学生成绩
            # 要求：如果没有成绩，显示提示信息
            if not scores:
                print("还没有学生成绩！")
            else:
                print("\n所有学生成绩：")
                print('=' * 30)
                for name,score in scores.items():
                    print(f"{name:10} {score:5.1f}分")
                print('-' * 30)
        
        elif choice == "3":
            # TODO: 删除学生成绩
            # 要求：处理学生不存在的情况
            name = input("请输入你要删除学生名字：").strip()
            if not name:
                print("名字不能为空")
                continue
            if name in scores:
                del scores[name]
                print(f"已删除{name}")
            else:
                print("没有该学生！")
        
        
        elif choice == "4":
            # TODO: 计算平均分
            # 要求：处理没有成绩的情况（除零错误）
            if not scores:
                print("还没有学生！")
            else:
                total = sum(scores.values())
                count = len(scores) 
                average = total / count
                print(f'平均分：{average:.2f}分')
                print(f'学生人数：{count}人')
                print(f'总分；{total:.1f}分')

        elif choice == "5":
            print("👋 退出系统")
            break
        
        else:
            print("❌ 请输入1-5之间的数字")

# TODO: 运行学生成绩管理系统
if __name__ == "__main__":
    manage_student_scores()