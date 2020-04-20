# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: reverse_vowels_of_string
Description: Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"
Author: Liu Changxin
date: 2020/4/20
---------------------------------
Change Activity:
2020/4/20
"""


def reverse_vowels(s):
    vowel = 'aeiou'
    vowel += vowel + vowel.upper()
    vowel_list = [v for v in vowel]
    s_list = [item for item in s]
    print('--vowel list is ---', vowel_list)
    print('==string list is ===', s_list)
    pre = 0
    back = len(s_list) - 1
    while pre < back:
        while pre < back and s_list[pre] not in vowel_list:
            pre += 1
        while pre < back and s_list[back] not in vowel_list:
            back -= 1
        if pre < back:
            s_list[pre], s_list[back] = s_list[back], s_list[pre]
            pre += 1
            back -= 1
    return ''.join(s_list)


if __name__ == '__main__':
    res = reverse_vowels('hello')
    print(res)
    '''
    result:
    Runtime: 192 ms, faster than 17.03% of Python online submissions for Reverse Vowels of a String.
    Memory Usage: 15 MB, less than 38.46% of Python online submissions for Reverse Vowels of a String.
    '''

