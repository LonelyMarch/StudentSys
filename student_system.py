#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-19 18:50:44
@FilePath: /StudentSys/student_system.py
@version:
@Descripttion:
'''


import os

import prettytable

student_info_txt = "student_info.txt"  # 将文件赋给一个变量

implemented = 1  # 标记是否子函数被执行，1为执行过

print("\n====================学生信息管理系统====================")


def main():
    global implemented  # 声明全局变量
    function = {"1": insert, "2": search, "3": delete,
                "4": modify, "5": reorder, "6": total, "7": show}
    while True:
        menu()
        try:
            choice = input("请选择\t(输入行首数字)\n")
        except:
            implemented = 0  # 标记子函数未被执行
            continue
        if choice == "0":
            implemented = 0  # 标记子函数未被执行
            sign_out()
            break
        print("\n—=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-—=-=-=-=-=-=-=-=-")
        function[choice]()


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
    if not os.path.exists(student_info_txt):
        with open(student_info_txt, "r", encoding="utf-8"):
            pass
    while True:  # 循环录入
        dictionary = putin(id_repeated=1)
        student_list.append(dictionary)  # 写入储存列表
        while True:
            insert_again = input("\n是否继续添加学生信息？\ty/n\n")
            if insert_again in ["y", "n"]:
                break
        if insert_again == "y":
            continue
        else:
            break
    save(student_list, 1)  # 追加进文件
    print("\n学生信息录入完毕\n")
    return


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
            if search_again in ['y', 'n']:
                break
        if search_again == "y":
            continue
        else:
            print()  # 换行
            break
    return


def delete():
    if not os.path.exists(student_info_txt):
        print("暂未保存学生信息")
        return
    else:
        while True:
            info = []  # 初始化信息列表
            after = []  # 初始化删除之后的列表
            delete_flag = 1  # 标记是否删除成功
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
                        after.append(info_item)  # 将不是要删除的学生的信息存入列表
                    else:
                        delete_flag = 0  # 标记已删除
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
                save(after, 0)
                print("删除完成\n")
                while True:
                    show_answer = input("是否显示现在库中的信息\ty/n\n")
                    if show_answer in ['y', 'n']:
                        break
                if show_answer == 'y':
                    show()
            while True:
                delete_again = input("\n是否继续删除\ty/n\n")
                if delete_again in ['y', 'n']:
                    break
            if delete_again == "y":
                continue
            else:
                print()
                return


def modify():
    if not os.path.exists(student_info_txt):
        print("\n暂未保存学生信息\n")
    else:
        after = []
        while True:
            modify_flag = 1
            mode = input("\n按id修改请输入1\t\t按姓名修改请输入2\n")
            if mode == '1':
                while True:
                    modify_id = input("\n请输入id：")
                    if modify != '':
                        break
                with open(student_info_txt, 'r', encoding='utf-8') as rfile:
                    for item in rfile:
                        d = dict(eval(item))
                        if d["id"] == modify_id:
                            modify_flag = 0
                            print("已找到这名学生,可以修改相关信息")
                            dictionary = putin(
                                id_repeated=1, id_repeated_others=1, id_except=d["id"])
                            after.append(str(dictionary))
                        else:
                            after.append(str(d))
            elif mode == '2':
                while True:
                    modify_name = input("\n请输入姓名：")
                    if modify_name != '':
                        break
                with open(student_info_txt, 'r', encoding='utf-8') as rfile:
                    for item in rfile:
                        d = dict(eval(item))
                        if d["name"] == modify_name:
                            modify_flag = 0
                            print("已找到这名学生,可以修改相关信息")
                            dictionary = putin(
                                id_repeated=1, id_repeated_others=1, id_except=d["id"])
                            after.append(str(dictionary))
                        else:
                            after.append(str(d))
            else:
                continue
            if modify_flag:
                print("库中无此学生信息\n")
            else:
                save(after, 0)
                print("修改成功\n")
            while True:
                modify_again = input("是否继续修改\ty/n\n")
                if modify_again in ["y", "n"]:
                    break
            if modify_again == "y":
                modify()
            else:
                break
    return


def reorder():
    if os.path.exists(student_info_txt):
        with open(student_info_txt, "r", encoding="utf-8") as rfile:
            new = []
            for item in rfile:
                d = dict(eval(item))
                new.append(d)
    else:
        print("\n暂未保存学生信息\n")
        return
    while True:
        try:
            reorder_mode = int(
                input(
                    "请选择排序方式:\t(输入行首数字)\n0.按总成绩排序\n1.按语文成绩排序\n2.按数学成绩排序\n3.按英语成绩排序\n4.按物理成绩排序\n")
            )
        except:
            print("\n输入有误请重新输入\n")
            continue
        if reorder_mode in [0, 1, 2, 3, 4]:
            break
        print("\n输入有误请重新输入\n")
    while True:
        reorder_mode_ad = int(input("\n选择升序请输入1\n选择降序请输入2\n"))
        if reorder_mode_ad == 1:
            reorder_mode_ad = False
            break
        elif reorder_mode_ad == 2:
            reorder_mode_ad = True
            break
        print("输入有误，请重新输入\n")
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
    print("\n排序完成，结果如下：\n")
    show_info(new)
    print()
    save(new, 0)


def total():
    if os.path.exists(student_info_txt):
        with open(student_info_txt, "r", encoding="utf-8") as rfile:
            student_list = rfile.readlines()
            if student_list != []:
                print(f"共有{len(student_list)}名学生\n")
                print()
            else:
                print("无学生信息\n")
                print()
    else:
        print("暂未保存学生信息\n")
        print()


def show():
    print()
    info_list = []
    if os.path.exists(student_info_txt):
        with open(student_info_txt, "r", encoding="utf-8") as rfile:
            for item in rfile:
                d = dict(eval(item))
                info_list.append(d)
            if info_list:
                print("数据库中信息如下：\n")
                show_info(info_list)
            else:
                print('无学生信息')
    else:
        print("\n暂未保存学生信息\n")
    print("\n—=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-—=-=-=-=-=-=-=-=-")


def save(lst, mode):
    if mode:  # mode为1则追加
        student_info = open(student_info_txt, "a", encoding="utf-8")
    else:  # mode为0则写入
        student_info = open(student_info_txt, "w", encoding="utf-8")
    for item in lst:  # 遍历列表中的字典(student_list中可能存在多位学生的信息，所以要遍历，而不是直接追加)
        student_info.write(str(item) + "\n")  # 将字典转换为字符串，再追加
    student_info.close()


def show_info(lst):
    tb = prettytable.PrettyTable()
    tb.field_names = ["ID", "姓名", "语文成绩", "数学成绩", "英语成绩", "物理成绩", "总成绩"]
    tb.align["ID"] = "l"
    tb.align["姓名"] = "l"
    tb.align["语文成绩"] = "r"
    tb.align["数学成绩"] = "r"
    tb.align["英语成绩"] = "r"
    tb.align["物理成绩"] = "r"
    tb.align["总成绩"] = "r"
    for item in lst:
        info = [item["id"],
                item["name"],
                item["chinese"],
                item["math"],
                item["english"],
                item["physics"],
                int(item["chinese"])
                + int(item["math"])
                + int(item["english"])
                + int(item["physics"])]
        tb.add_row(info)
    print(tb)


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


def putin(id_repeated=0, id_repeated_others=0, id_except=0):
    id_yn = 1   # 初始化学生信息是否输入成功的标记
    name_yn = 1
    chinese_yn = 1
    math_yn = 1
    english_yn = 1
    physics_yn = 1
    while True:
        if id_yn:
            id = input("\n请输入id:")
            if not id:  # 判断id是否不为空
                continue
            elif not id.isdecimal():    # 判断id是否不又十进制的数字组成
                print('仅能输入数字')
                continue
            if id_repeated:
                id_list = []  # 初始化储存id的列表
                with open(student_info_txt, "r", encoding="utf-8") as rfile:
                    for item in rfile:  # 遍历文件的每一个字典，结果为字符串
                        d = dict(eval(item))    # 将字符串转为字典
                        id_list.append(d["id"])  # 将id写入列表
                if id_repeated_others:
                    id_list.remove(id_except)
                if id in id_list:  # 判断id是否重复
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
        dictionary = {
            "id": id,
            "name": name,
            "chinese": chinese,
            "math": math,
            "english": english,
            "physics": physics,
        }
        return dictionary


if __name__ == "__main__":
    main()
