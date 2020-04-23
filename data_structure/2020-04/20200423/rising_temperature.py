# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: rising_temperature
Description:  Given a Weather table, write a SQL query to find all dates' Ids with higher temperature
compared to its previous (yesterday's) dates.

Example:
+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
For example, return the following Ids for the above Weather table:

+----+
| Id |
+----+
|  2 |
|  4 |
+----+

Author: Liu Changxin
date: 2020/4/23
---------------------------------
Change Activity:
2020/4/23
"""


sql = "select a.id as Id from Weather a join Weather b on DateDiff(a.recorddate, b.recorddate) = 1 where a.temperature > b.temperature"

"""
Result:
Runtime: 666 ms, faster than 25.12% of MySQL online submissions for Rising Temperature.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.
"""

"""
DateDiff(a.recorddate, b.recorddate) = 1 : 这句的意思是相邻的两天， datediff返回的是两个日期之间的时间

此题思路： 先建立虚拟的表 a, b
判断a, b之间相邻日期，a 的温度高于b的数据
生成a.id as Id 的新表作为输出

"""

