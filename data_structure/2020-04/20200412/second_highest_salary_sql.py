# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: second_highest_salary_sql
Description: Write a SQL query to get the second highest salary from the Employee table.
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

Author: Liu Changxin
date: 2020/4/16
---------------------------------
Change Activity:
2020/4/16
"""

'''
select max(Salary) as SecondHighestSalary from Employee where Salary < (select max(Salary) from Employee)
'''

'''
result:
Runtime: 1401 ms, faster than 5.03% of MySQL online submissions for Second Highest Salary.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.
'''