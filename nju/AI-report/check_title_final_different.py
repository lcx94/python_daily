# -*- coding:utf-8 _*-
'''
@author: lcx
@file: check_title_final_different.py
@time: 2020/11/17 9:21
@desc:  AI专利报告 title 表和 final 表数据差集
'''

import  cx_Oracle as cx

import os

os.environ['path'] = r'D:\navicat\Navicat Premium 12\instantclient_12_2'

conn = cx.connect('PATSTAT_GROUP2', 'D7zVwMR8', 'db.imcluster.cc:1521/patstat2020a')
# conn = cx.connect('administrator', 'password', '114.212.167.89:1521/patstat2020a')
cursor = conn.cursor()
cursor2 = conn.cursor()


def get_subtraction():
    cursor.execute('SELECT distinct APPLN_ID from PATSTAT2020A.AI_FINAL')
    data = cursor.fetchone()
    print('start')
    print(data)
    count = 0
    while data is not None:
        insert_sql = 'INSERT INTO PATSTAT2020A.LIUCHANGXIN_AI_SUBTRACTION(APPLN_ID) VALUES ({})'.format(data[0])
        cursor2.execute(insert_sql)
        count += 1
        print('-------insert data --------{}-------'.format(str(count)))
        # 1000条存储一次
        if count % 1000 == 0:
            conn.commit()
        data = cursor.fetchone()
    print('end')

def get_data():
    cursor.execute('SELECT * FROM PATSTAT2020A.AI_PAT_TITLE ')
    data = cursor.fetchone()
    while data is not None:
        get_difference(data[0], data[1])
        data = cursor.fetchone()


total_count = 0
count = 0
def get_difference(id, title):
    global count
    global total_count
    total_count += 1
    print('======total check ========{}=====current id is {}===='
          .format(str(total_count), str(id)))
    cursor2.execute('SELECT APPLN_ID FROM PATSTAT2020A.LIUCHANGXIN_AI_SUBTRACTION where APPLN_ID = {}'.format(id))
    res = cursor2.fetchone()
    if res is None:
        count += 1
        print('-----find loss data -----{}---'.format(str(count)))
        with open('loss_title.txt', 'a', encoding='UTF-8') as f:
            f.writelines(title + '\n')
    else:
        print('---------------exist data -----------')
        print(res)


if __name__ == '__main__':
    get_subtraction()
