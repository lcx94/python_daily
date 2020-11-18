# -*- coding:utf-8 _*-
'''
@author: lcx
@file: test_check_minus.py
@time: 2020/11/18 9:42
@desc: 
'''
import cx_Oracle as cx

import os

os.environ['path'] = r'D:\navicat\Navicat Premium 12\instantclient_12_2'

conn = cx.connect('PATSTAT_GROUP2', 'D7zVwMR8', 'db.imcluster.cc:1521/patstat2020a')
# conn = cx.connect('administrator', 'password', '114.212.167.89:1521/patstat2020a')
cursor = conn.cursor()
cursor2 = conn.cursor()

def get_data():
    cursor.execute('SELECT APPLN_ID FROM PATSTAT2020A.AI_PAT_TITLE minus select distinct APPLN_ID from PATSTAT2020A.AI_FINAL')
    data = cursor.fetchone()
    print(data)


if __name__ == '__main__':
    get_data()
