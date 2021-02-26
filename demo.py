#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-26 21:24:13
@FilePath: /StudentSys/demo.py
@version:
@Descripttion:
'''
import wmi
import subprocess
import os


def Mysql_Service():
    services = wmi.WMI().Win32_Service(Name='mysql')
    if not services:
        # 创建mysql服务
        # 注意最后一个元素中的空格
        os.popen(''.join([os.getcwd(), '\\mysql\\bin', ' mysqld -install']))
        Mysql_Service()
    cmd = subprocess.Popen('net start mysql', shell=True)
    cmd.wait()
    # f = os.popen('net start mysql')
    print('MySQL服务已启动')


Mysql_Service()
