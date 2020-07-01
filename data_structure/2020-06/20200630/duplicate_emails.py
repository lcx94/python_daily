# -*- coding:utf-8 _*-
'''
@author: lcx
@file: duplicate_emails.py
@time: 2020/7/1 9:32
@desc:
Write a SQL query to find all duplicate emails in a table named Person.
'''

'SELECT email FROM person GROUP BY email HAVING COUNT(1)>1'