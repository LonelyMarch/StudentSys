#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-25 20:00:34
@FilePath: /StudentSys/sqlalchemy_demo.py
@version: 
@Descripttion: 
'''

import prettytable
import os

from sqlalchemy import create_engine  # 26Kb
from sqlalchemy import Column, Integer, String, Float  # 103KB
from sqlalchemy.ext.declarative import declarative_base  # 29KB
from sqlalchemy.orm import sessionmaker, Session  # 133KB

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
# 创建映射表 ↓↓↓

DB_URL = 'mysql+pymysql://root:Hh070820@localhost:3306/studentsys?charset=utf8mb4'  # 绑定数据库地址
engine = create_engine(DB_URL, echo=True)  # 创建引擎,echo参数控制是否输出日志
Base = declarative_base()  # 创建映射用的基类


class Info(Base):
    __tablename__ = 'info'  # 映射的表名
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)  # 创建字段
    name = Column(String(64), nullable=False)
    chinese = Column(Float)
    math = Column(Float)
    english = Column(Float)
    physics = Column(Float)


Base.metadata.create_all(engine)  # 创建映射

# SQLAlchemy 在操作数据库时需要用到 Session，通过 sessionmaker 方法获取
# session = sessionmaker(bind=engine)
# session = Session()

# zbw = Info(id=1, name='zbw', chinese=0, math=1, english=3, physics=4)
# session.add(zbw)
# session.commit()

# 创建映射表 ↑↑↑
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

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
