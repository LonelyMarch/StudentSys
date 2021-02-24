#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-24 21:34:18
@FilePath: /StudentSys/demo.py
'''

import pymysql

# 创建连接
cnct = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='Hh070820',
                       db='studentsys',
                       charset='utf8mb4')

# 创建游标(查询数据返回为元组格式)
# cursor = conn.cursor()

# 创建游标(查询数据返回为字典格式)
cursor = cnct.cursor(pymysql.cursors.DictCursor)

# 1. 执行SQL,返回受影响的行数
effect_row1 = cursor.execute("select * from data")

# 2. 执行SQL,返回受影响的行数,一次插入多行数据
# effect_row2 = cursor.execute('insert into data values(%S)', [])

# 查询所有数据,返回数据为元组格式
result = cursor.fetchall()

# 增/删/改均需要进行commit提交,进行保存
cnct.commit()

# 关闭游标
cursor.close()

# 关闭连接
cnct.close()

print(result)
"""
[{'id': 6, 'name': 'boom'}, {'id': 5, 'name': 'jack'}, {'id': 7, 'name': 'lucy'}, {'id': 4, 'name': 'tome'}, {'id': 3, 'name': 'zff'}, {'id': 1, 'name': 'zhaofengfeng'}, {'id': 2, 'name': 'zhaofengfeng02'}]
"""
