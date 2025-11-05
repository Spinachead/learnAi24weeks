import os
import re
import pandas as pd
import json
import random

#猜数字
def guess_number():
    target = random.randint(1, 100)
    guess_count = 0
    print("欢迎来到猜数字游戏, 请输入一个1~100的数字")
    while True:
        try:
            user_input = input("请输入: ")
            user_number = int(user_input)
            guess_count += 1
            if user_number < 1 or user_number > 100:
                print("请输入1~100的数字")
                continue
            if user_number > target:
                print("数字太大了")
            elif user_number < target:
                print("数字太小了")
            else:
                print("恭喜你猜对了, 猜了%d次" % guess_count)
                break
        except ValueError:
            print("请输入有效数字")

#计算器
def calculator():
    print("欢迎使用简易计算器！请输入两个数字和运算符（+ - * /）")

    while True:
        try:
            user_input = input("请输入两个数字（用空格分隔），或输入 'q' 退出：")
            if user_input.lower() == 'q':
                print("感谢使用，再见！")
                break

            num1, num2 = map(int, user_input.split())
            operator = input("请输入运算符（+ - * /）：")

            if operator == '+':
                print(f"结果是：{num1 + num2}")
            elif operator == '-':
                print(f"结果是：{num1 - num2}")
            elif operator == '*':
                print(f"结果是：{num1 * num2}")
            elif operator == '/':
                if num2 == 0:
                    print("错误：不能除以 0！")
                    continue
                print(f"结果是：{num1 / num2}")
            else:
                print("请输入有效的运算符！")
        except ValueError:
            print("请输入有效的数字和格式！")



def sample_task_manage():
    print("欢迎体验待办事项管理器,按v查看所有任务,按a添加任务,按d删除任务,按s保存任务到本地")
    task = []

    # 如果存在历史任务，加载进来
    if os.path.exists('task.txt'):
        with open('task.txt', 'r', encoding='utf-8') as f:
            task = [line.strip() for line in f.readlines()]

    while True:
        print("\n可用命令：v(查看) | a(添加) | d(删除) | s(保存) | q(退出)")
        user_input = input("请输入命令：").strip().lower()

        if user_input == 'v':
            if not task:
                print("当前没有任务")
            else:
                for index, content in enumerate(task):
                    print(f"任务ID: {index}, 内容: {content}")

        elif user_input == 'a':
            new_task = input("请输入任务内容：")
            task.append(new_task)
            print("任务添加成功")

        elif user_input == 'd':
            try:
                task_id = int(input("请输入任务ID："))
                if 0 <= task_id < len(task):
                    task.pop(task_id)
                    print("任务删除成功")
                else:
                    print("任务ID不存在")
            except ValueError:
                print("请输入有效的数字作为任务ID")

        elif user_input == 's':
            with open('task.txt', 'w', encoding='utf-8') as f:
                for item in task:
                    f.write(item + '\n')
            print("任务已保存到本地")

        elif user_input == 'q':
            print("感谢使用，再见！")
            break

        else:
            print("请输入合法的命令")





def word_count():
    print("欢迎使用单词统计器，输入文件名称，统计每个单词出现的次数（忽略大小写）")
    while True:
        file_name = input("请输入文件名称（输入 q 退出）：").strip()
        if file_name.lower() == 'q':
            print("感谢使用，再见！")
            break

        if not os.path.exists(file_name):
            print("文件不存在，请重新输入")
            continue

        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                text = f.read().lower()  # 统一转为小写
                # 使用正则表达式提取单词（只保留字母组成的单词）
                words = re.findall(r'\b[a-z]+\b', text)

                count = {}
                for word in words:
                    if word in count:
                        count[word] += 1
                    else:
                        count[word] = 1
                print("\n单词统计结果如下：")
                for word, num in count.items():
                    print(f"单词: {word}, 出现次数: {num}")
                print(f"共统计了 {len(count)} 个不同的单词。")

        except Exception as e:
            print(f"读取文件时发生错误：{e}")




def sample_contacts():
    print("这是一个通讯录,可以添加联系人(姓名+电话),查找 删除联系人")
    contacts = {}

    if os.path.exists('contacts.csv'):
        try:
            df = pd.read_csv('contacts.csv')
            # 把 DataFrame 转为字典 {姓名: 电话}
            contacts = dict(zip(df['姓名'], df['电话']))
        except Exception as e:
            print(f"读取文件失败：{e}")

    while True:
        print("\n可用命令：v(查看) | a(添加) | d(删除) | s(保存) | q(退出)")
        user_input = input("请输入命令：").strip().lower()

        if user_input == 'v':
            if not contacts:
                print("没有联系人")
            else:
                for name, phone in contacts.items():
                    print(f"姓名: {name}, 电话: {phone}")

        elif user_input == 'a':
            try:
                name, phone = input("请输入姓名和电话(用空格分割): ").split()
                if name in contacts:
                    print("联系人已存在")
                    continue
                if len(name) > 20 or len(phone) > 11 or not phone.isdigit():
                    print("请输入正确的姓名和电话（电话为数字，不超过11位）")
                else:
                    contacts[name] = phone
                    print("添加成功")
            except ValueError:
                print("请输入姓名和电话，用空格分隔")

        elif user_input == 'd':
            name = input("请输入要删除的联系人姓名：")
            if name in contacts:
                del contacts[name]
                print("删除成功")
            else:
                print("联系人不存在")

        elif user_input == 's':
            try:
                df = pd.DataFrame(list(contacts.items()), columns=['姓名', '电话'])
                df.to_csv('contacts.csv', index=False)
                print("保存成功")
            except Exception as e:
                print(f"保存失败：{e}")

        elif user_input == 'q':
            print("感谢使用，再见！")
            break

        else:
            print("请输入合法的命令")



def student_manage():
    print("欢迎使用学生管理系统")
    students = []

    if os.path.exists('students.json'):
        with open('students.json', 'r', encoding='utf-8') as f:
            students = json.load(f)

    while True:
        print("\n可用命令：v(查看) | a(添加) | d(删除) | s(保存) | q(退出)")
        user_input = input("请输入命令：").strip().lower()

        if user_input == 'v':
            if not students:
                print("没有学生")
                continue
            for student in students:
                print(f"学生ID: {student['id']} 姓名: {student['name']} 成绩: {student['score']}")

        elif user_input == 'a':
            try:
                student_id = int(input("请输入学生ID："))
                name = input("请输入学生姓名：").strip()
                score = int(input("请输入学生成绩："))

                if any(s['id'] == student_id for s in students):
                    print("学生ID已存在")
                    continue
                if not name or len(name) > 20:
                    print("请输入正确的学生姓名（1~20个字符）")
                    continue

                students.append({'id': student_id, 'name': name, 'score': score})
                print("添加成功")

            except ValueError:
                print("请输入正确的学生信息（ID和成绩应为整数）")

        elif user_input == 'd':
            try:
                student_id = int(input("请输入要删除的学生ID："))
                original_len = len(students)
                students[:] = [s for s in students if s['id'] != student_id]
                if len(students) < original_len:
                    print("删除成功")
                else:
                    print("学生不存在")
            except ValueError:
                print("请输入正确的学生ID")

        elif user_input == 's':
            try:
                with open('students.json', 'w', encoding='utf-8') as f:
                    json.dump(students, f, ensure_ascii=False, indent=4)
                print("保存成功")
            except Exception as e:
                print(f"保存文件发生错误：{e}")

        elif user_input == 'q':
            print("感谢使用，再见！")
            break

        else:
            print("请输入合法的命令")


# 定义选项
OPTIONS = {
    'r': '石头',
    'p': '剪刀',
    's': '布',
    'q': '退出'
}

def determine_winner(player, computer):
    """判断胜负"""
    if player == computer:
        return "平局"
    win_conditions = {
        'r': 's',  # 石头赢剪刀
        'p': 'r',  # 剪刀赢石头
        's': 'p'   # 布赢剪刀
    }
    if win_conditions[player] == computer:
        return "你赢了"
    else:
        return "你输了"

#剪刀石头布的游戏
def play_game():
    print("欢迎来到石头剪刀布游戏！")
    print("输入以下命令进行游戏：")
    print("r: 石头 | p: 剪刀 | s: 布 | q: 退出")

    while True:
        # 玩家输入
        player_choice = input("请输入你的选择 (r/p/s/q): ").lower()

        if player_choice == 'q':
            print("游戏结束，感谢游玩！👋")
            break

        if player_choice not in ['r', 'p', 's']:
            print("无效输入，请重新输入 r(石头), p(剪刀), s(布) 或 q(退出)")
            continue

        # 电脑随机选择
        computer_choice = random.choice(['r', 'p', 's'])

        # 显示选择
        print(f"你出了: {OPTIONS[player_choice]}")
        print(f"电脑出了: {OPTIONS[computer_choice]}")

        # 判断胜负
        result = determine_winner(player_choice, computer_choice)
        print(f"结果: {result}\n")
