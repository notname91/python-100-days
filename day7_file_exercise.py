# 练习：文件复制程序
# 目标：读取一个文件的内容，复制到另一个文件

print("📋 练习1：文件复制程序")
print("=" * 40)

# 1. 首先创建源文件
with open("source.txt", "w", encoding="utf-8") as source_file:
    source_file.write("这是源文件的内容。\n")
    source_file.write("第一行内容。\n")
    source_file.write("第二行内容。\n")
    source_file.write("第三行内容。\n")

print("✅ 已创建源文件 source.txt")

# 2. 你的任务：复制文件内容
# TODO: 请完成以下代码
# 读取 source.txt 的内容
with open("source.txt", "r", encoding="utf-8") as source: 
    content = source.read()  

# 将内容写入新文件 copy.txt
with open("copy.txt", "w", encoding="utf-8") as target:  
    target.write(content)  

print("✅ 文件复制完成！")

# 3. 验证复制结果
print("\n验证复制结果：")
with open("copy.txt", "r", encoding="utf-8") as file:
    print(file.read())

