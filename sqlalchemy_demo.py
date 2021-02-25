#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-25 10:24:45
@FilePath: /StudentSys/sqlalchemy_demo.py
@version: 
@Descripttion: 
'''

from sqlalchemy import create_engine  # 26Kb
from sqlalchemy import Column, Integer, String, Float  # 103KB
from sqlalchemy.ext.declarative import declarative_base  # 29KB
from sqlalchemy.orm import sessionmaker, Session  # 133KB

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
session = sessionmaker(bind=engine)
session = Session()

zbw = Info(id=1, name='zbw', chinese=0, math=1, english=3, physics=4)
session.add(zbw)
session.commit()
