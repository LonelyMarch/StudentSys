#!/usr/bin/env python
# coding=utf-8

"""
Author: LonelyMarch
Date: 2020-12-27 18:28:29
LastEditors: LonelyMarch
LastEditTime: 2020-12-29 09:37:35
FilePath: /StudentSys/student_system.py
"""

import os

student_info_txt = "student_info.txt"  # 将文件赋给一个变量

implemented = 1  # 标记是否子函数被执行，1为执行过

print("\n====================学生信息管理系统====================")


def main():
    global implemented  # 声明全局变量
    while True:
        menu()
        choice = input("请选择\n")
        if choice in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            if choice == "0":
                implemented = 0  # 标记子函数未被执行
                sign_out()
                break
            elif choice == "1":
                print("\n—=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-—=-=-=-=-=-=-=-=-")
                insert()  # 录入学生信息
            elif choice == "2":
                print("\n—=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-—=-=-=-=-=-=-=-=-")
                search()  # 查找学生信息
            elif choice == "3":
                print("\n—=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-—=-=-=-=-=-=-=-=-")
                delete()  # 删除学生信息
            elif choice == "4":
                print("\n—=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-—=-=-=-=-=-=-=-=-")
                modify()  # 修改学生信息
            elif choice == "5":
                print("\n—=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-—=-=-=-=-=-=-=-=-")
                reorder()  # 排序
            elif choice == "6":
                print("\n—=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-—=-=-=-=-=-=-=-=-")
                total()  # 统计总人数
            else:
                print("\n—=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-—=-=-=-=-=-=-=-=-")
                show()  # 显示所有学生信息
        else:
            implemented = 0  # 标记子函数未被执行


def menu():
    if implemented == 1:  # 子函数执行后，再显示一遍功能菜单；若子函数未被执行，则不显示菜单，继续显示"请选择"
        print("------------------------功能菜单------------------------")
        print("\t1.录入学生信息")
        print("\t2.查找学生信息")
        print("\t3.删除学生信息")
        print("\t4.修改学生信息")
        print("\t5.排序")
        print("\t6.统计总人数")
        print("\t7.显示所有学生信息")
        print("\t0.退出")
        print("========================================================")


def insert():
    student_list = []  # 初始化用于储存要添加的学生的信息的列表
    id_list = []  # 初始化用于存储已存在id的列表
    id_yn = 1  # 初始化学生信息是否输入成功的标记
    name_yn = 1
    chinese_yn = 1
    math_yn = 1
    english_yn = 1
    physics_yn = 1
    while True:  # 循环录入
        try:  # NOTE:此处的 try_except 可以用 if(os.path.exists)_else 替换
            with open(student_info_txt, "r", encoding="utf-8") as rfile:
                for item in rfile:  # 遍历文件的每一个字典，结果为字符串
                    d = dict(eval(item))  # 将字符串转为字典
                    id_list.append(d["id"])  # 追加id到列表
        except:
            open(student_info_txt, 'w', encoding='utf-8')  # 文件不存在则创建
        if id_yn:  # 如果未成功录入，则录入，否则跳过
            id = input("\n请输入id:")
        if not id:  # 判断id是否不为空
            continue
        elif not id.isdecimal():    # 判断id是否不又十进制的数字组成
            print('仅能输入数字')
            continue
        elif id in id_list:  # 判断id是否重复
            print("\nid与信息库中的重复，请重新输入")
            continue
        id_yn = 0  # 标记id录入成功
        if name_yn:
            name = input("请输入姓名:")
        if not name:
            continue
        name_yn = 0
        try:
            if chinese_yn:
                chinese = int(input("请输入语文成绩："))
        except:  # 捕获因输入的不是整数而产生的错误
            print("输入无效")
            continue
        chinese_yn = 0
        try:
            if math_yn:
                math = int(input("请输入数学成绩："))
        except:
            print("输入无效")
            continue
        math_yn = 0
        try:
            if english_yn:
                english = int(input("请输入英语成绩："))
        except:
            print("输入无效")
            continue
        english_yn = 0
        try:
            if physics_yn:
                physics = int(input("请输入物理成绩："))
        except:
            print("输入无效")
            continue
        physics_yn = 0
        student = {
            "id": id,
            "name": name,
            "chinese": chinese,
            "math": math,
            "english": english,
            "physics": physics,
        }  # 将学生信息存入字典
        student_list.append(student)  # 写入储存列表
        insert_again = input("\n是否继续添加学生信息？\ty/n\n")
        if insert_again == "y":
            id_yn = 1  # 标记归位，以便下一次录入
            name_yn = 1
            chinese_yn = 1
            math_yn = 1
            english_yn = 1
            physics_yn = 1
            continue
        else:
            break
    save(student_list, 1)  # 追加进文件
    print("\n学生信息录入完毕\n")


def search():
    info_search = []  # 初始化用于储存查询到的学生信息的列表
    info = []  # 初始化储存库中学生信息的列表
    if os.path.exists(student_info_txt):  # 判断文件是否存在
        with open(student_info_txt, "r", encoding="utf-8") as rfile:
            for item in rfile:
                info_d = dict(eval(item))
                info.append(info_d)
    else:
        print("\n暂未保存学生信息\n")
        return
    while True:
        found = 1  # 标记是否找到，未找到为1
        query_mode = input("\n按id查找请输入1\t\t按姓名查找请输入2\n")
        if query_mode == "1":
            while True:
                query_id = input("\n请输入id：")
                if query_id != '':
                    break
            for info_item in info:  # 遍历列表中的字典
                if info_item["id"] == query_id:
                    info_search.append(info_item)
                    found = 0  # 如果匹配，标记为0
        elif query_mode == "2":
            while True:
                query_name = input("\n请输入姓名：")
                if query_name != '':
                    break
            for info_item in info:
                if info_item["name"] == query_name:
                    info_search.append(info_item)
                    found = 0
        elif query_mode == '':
            continue
        else:
            print("输入有误，请重新输入：")
            continue
        if found:
            print('\n未查询到此学生的信息')
        else:
            show_info(info_search)  # 显示信息
            info_search.clear()  # 清空列表
        while True:
            search_again = input("\n是否继续查询?\ty/n\n")
            if search_again in ['y', 'n']:  # 判断回答是否有误
                break
        if search_again == "y":
            continue
        else:
            print()
            break


def delete():
    if not os.path.exists(student_info_txt):
        print("暂未保存学生信息")
    else:
        while True:
            info = []
            after = []
            delete_flag = 1
            with open(student_info_txt, 'r', encoding='utf-8') as rfile:
                for item in rfile:
                    info_d = dict(eval(item))
                    info.append(info_d)
            mode = input("\n按id删除请输入1\t\t按姓名删除请输入2\n")
            if mode == '1':
                while True:
                    delete_id = input("\n请输入id：")
                    if delete_id != '':
                        break
                    for info_item in info:
                        if info_item["id"] != delete_id:
                            after.append(info_item)
                        else:
                            delete_flag = 0
            elif mode == '2':
                while True:
                    delete_name = input("\n请输入姓名：")
                    if delete_name != '':
                        break
                    for info_item in info:
                        if info_item["name"] != delete_name:
                            after.append(info_item)
                        else:
                            delete_flag = 0
            else:
                continue
            if delete_flag:
                print('库中无此学生信息')
            else:
                save(info, 0)
                show()
            while True:
                delete_again = input("\n是否继续删除\ty/n\n")
                if delete_again in ['y', 'n']:
                    break
            if delete_again == "y":
                continue
            else:
                print()
                break


def modify():
    show()
    if os.path.exists(student_info_txt):
        with open(student_info_txt, "r", encoding="utf-8") as rfile:
            student_old = rfile.readlines()
    else:
        print("\n暂未保存学生信息\n")
        return
    modify_id = input("请输入要修改的学生的id")
    with open(student_info_txt, "w", encoding="utf-8") as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d["id"] == modify_id:
                print("已找到这名学生,可以修改相关信息")
                while True:
                    try:
                        d["name"] = input("请输入姓名：")
                        d["chinese"] = input("请输入语文成绩：")
                        d["math"] = input("请输入数学成绩：")
                        d["english"] = input("请输入英语成绩：")
                        d["physics"] = input("请输入物理成绩：")
                    except:
                        print("输入有误，请重新输入")
                    else:
                        break
                wfile.write(str(d) + "\n")
                print("修改成功")
            else:
                wfile.write(str(d) + "\n")
    modify_again = input("是否继续修改\ty/n\n")
    if modify_again == "y":
        modify()


def reorder():
    show()
    if os.path.exists(student_info_txt):
        with open(student_info_txt, "r", encoding="utf-8") as rfile:
            info_list = rfile.readlines()
        new = []
        for item in info_list:
            d = dict(eval(item))
            new.append(d)

    else:
        print("\n暂未保存学生信息\n")
        return
    reorder_mode = int(
        input("请选择排序方式：\n0.按总成绩排序\n1.按语文成绩排序\n2.按数学成绩排序\n3.按英语成绩排序\n4.按物理成绩排序")
    )
    if reorder_mode not in [0, 1, 2, 3, 4]:
        print("\n输入有误请重新输入\n")
        reorder()
    reorder_mode_ad = int(input("选择 1.升序 或 2.降序\n"))
    if reorder_mode_ad == 1:
        reorder_mode_ad = True
    elif reorder_mode_ad == 2:
        reorder_mode_ad = False
    else:
        print("输入有误，请重新输入\n")
        reorder()
    if reorder_mode == 0:
        new.sort(
            key=lambda new: int(new["chinese"])
            + int(new["math"])
            + int(new["english"])
            + int(new["physics"]),
            reverse=reorder_mode_ad,
        )
    elif reorder_mode == 1:
        new.sort(key=lambda new: int(new["chinese"]), reverse=reorder_mode_ad)
    elif reorder_mode == 2:
        new.sort(key=lambda new: int(new["math"]), reverse=reorder_mode_ad)
    elif reorder_mode == 3:
        new.sort(key=lambda new: int(new["english"]), reverse=reorder_mode_ad)
    else:
        new.sort(key=lambda new: int(new["physics"]), reverse=reorder_mode_ad)
    show_info(new)


def total():
    if os.path.exists(student_info_txt):
        with open(student_info_txt, "r", encoding="utf-8") as rfile:
            student_list = rfile.readlines()
            if student_list != "":
                print(f"共有{len(student_list)}名学生")
            else:
                print("无学生信息")
    else:
        print("\n暂未保存学生信息\n")


def show():
    info_list = []
    if os.path.exists(student_info_txt):
        with open(student_info_txt, "r", encoding="utf-8") as rfile:
            info = rfile.readlines()
            for item in info:
                info_list.append(eval(item))
            if info_list:
                show_info(info_list)
            else:
                print('无学生信息')
    else:
        print("\n暂未保存学生信息\n")


def save(lst, mode):
    if mode:  # mode为1则追加
        student_info = open(student_info_txt, "a", encoding="utf-8")
    else:  # mode为0则写入
        student_info = open(student_info_txt, "r", encoding="utf-8")
    for item in lst:  # 遍历列表中的字典(student_list中可能存在多位学生的信息，所以要遍历，而不是直接追加)
        student_info.write(str(item) + "\n")  # 将字典转换为字符串，再追加
    student_info.close()


def show_info(lst):
    format_title = "{:6}\t{:^12}\t{:^10}\t{:^10}\t{:^10}\t{:^10}  {:6}"
    print(format_title.format("ID", "姓名", "语文成绩", "数学成绩", "英语成绩", "物理成绩", "总成绩"))
    format_data = "{:6}\t{:^12}\t{:^10}\t{:^10}\t{:^10}\t{:^10}{:6}"
    for item in lst:
        print(
            format_data.format(
                item["id"],
                item["name"],
                item["chinese"],
                item["math"],
                item["english"],
                item["physics"],
                int(item["chinese"])
                + int(item["math"])
                + int(item["english"])
                + int(item["physics"]),
            )
        )


def sign_out():
    answer = input("\n您确定要退出吗？\ty/n\n")
    if answer == "y":
        print("\n已退出程序，谢谢您的使用。\n")
        return  # 回答为y，执行break，退出程序
    elif answer == "n":
        print()  # 换行
        main()  # 回答为n，再次执行主函数,就跳过了break
    else:
        sign_out()  # 回答错误，再次询问


if __name__ == "__main__":
    main()
