#第七天：文件操作基础
#学习目标：理解如何读写文件

print("第七天：学习文件操作")
print("=" * 50)

#==================================
#1.写入文件
#==================================
print("\n1.写入文件示例：")

# 使用 with open() 打开文件，'w' 表示写入模式
# encoding='utf-8' 确保中文能正确保存
with open("test_file.txt","w",encoding = "utf-8") as file:
    #写入内容到文件
    file.write("这是我的第一个文件！\n")
    file.write("Hello,World!\n")
    file.write("今天学习了文件操作。\n")
    file.write("Python 文件操作很简单！\n")

print(" 已创建 test_file.txt 并写入内容")

#==================================
#2.读取整个文件内容
#==================================
print('\n2.读取整个文件内容：')

#使用 'r' 模式读取文件
with open("test_file.txt","r",encoding = "utf-8") as file:
    #读取文件全部内容
    content = file.read()
    print('文件内容：')
    print('-' * 30)
    print(content)
    print('-' * 30)

#3.逐行读取文件
print("\n3.逐行读取文件：")

with open("test_file.txt","r",encoding = "utf-8") as file:
    print('文件内容（逐行显示）：')
    line_number = 1
    for line in file:
        #每行末尾有换行符，用 strip() 去掉
        print(f"第{line_number}行：{line.strip()}")
        line_number += 1

#4.追加文件内容
print('\n追加文件内容:')

#使用 'a' 模式追加内容，不会覆盖原有内容
with open("test_file.txt","a",encoding = "utf-8") as file:
    file.write('这是追加的内容！\n')
    file.write("追加内容不会覆盖原有内容。\n")

print(" 已追加内容到文件")

#再次读取显示所有内容
print('\n追加后的文件内容：')
with open("test_file.txt","r",encoding = "utf-8") as file:
    print(file.read())

#5.文件操作模式是总结
print("\n5. 文件操作模式总结：")
print("   'w' - 写入模式：创建新文件或覆盖已有文件")
print("   'r' - 读取模式：读取文件内容（文件必须存在）")
print("   'a' - 追加模式：在文件末尾添加内容")
print("   'x' - 创建模式：创建新文件，如果文件已存在则失败")