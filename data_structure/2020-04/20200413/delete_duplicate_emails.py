# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: delete_duplicate_emails
Description:
Author: Liu Changxin
date: 2020/4/16
---------------------------------
Change Activity:
2020/4/16
"""

'''
delete from person
where
id not in (
select id from ( select min(id) as id from person group by email having count(email) > 1) as a) 
and
email in ( select email from ( select email from person group by email having count(email) > 1) as b) 

'''

'''
result:
Runtime: 1580 ms, faster than 12.35% of MySQL online submissions for Delete Duplicate Emails.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.
'''
