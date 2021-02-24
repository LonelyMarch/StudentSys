#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-24 23:08:09
@FilePath: /StudentSys/sqlalchemy_demo.py
@version: 
@Descripttion: 
'''

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


DB_URL = 'mysql+pymysql://root:Hh070820@localhost:3306/studentsys?charset=utf8mb4'
engine = create_engine(DB_URL, echo=True)
base = declarative_base()


class info(base):
    __tablename = 'info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
