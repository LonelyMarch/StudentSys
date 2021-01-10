#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-01-10 13:53:39
@FilePath: /StudentSys/demo.py
'''


import prettytable as pt
database = "student_info.txt"
tb = pt.PrettyTable()
tb.field_names = ["ID", "姓名", "语文成绩", "数学成绩", "英语成绩", "物理成绩", "总成绩"]
tb.align["ID"] = "l"
tb.align["姓名"] = "l"
tb.align["语文成绩"] = "r"
tb.align["数学成绩"] = "r"
tb.align["英语成绩"] = "r"
tb.align["物理成绩"] = "r"
tb.align["总成绩"] = "r"
with open(database, "r", encoding="utf-8") as rfile:
    for item in rfile:
        d = dict(eval(item))
        info = [d["id"],
                d["name"],
                d["chinese"],
                d["math"],
                d["english"],
                d["physics"],
                int(d["chinese"])
                + int(d["math"])
                + int(d["english"])
                + int(d["physics"])]
        tb.add_row(info)
print(tb)
