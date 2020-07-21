# -*- coding:utf-8 _*-
'''
@author: lcx
@file: find_and_replace_in_string.py
@time: 2020/7/21 13:56
@desc:
Example1:
Input: S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
Output: "eeebffff"
Explanation: "a" starts at index 0 in S, so it's replaced by "eee".
"cd" starts at index 2 in S, so it's replaced by "ffff".
Example2:
Input: S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation: "ab" starts at index 0 in S, so it's replaced by "eee".
"ec" doesn't starts at index 2 in the original S, so we do nothing.
'''

def find_replace_string(S, indexes, sources, targets):
    for i in range(len(indexes)):
        current_source = sources[i]
        current_index = indexes[i]
        current_target = targets[i]
        if current_source == S[current_index:current_index+len(current_source)]:
            S = S.replace(current_source, current_target)
            position = len(current_target) - len(current_source)
            if i < len(indexes) - 1:
                index_back = []
                for j in range(i+1, len(indexes)):
                    if indexes[j] > current_index:
                        index_back.append(indexes[j]+position)
                    else:
                        index_back.append(indexes[j])
                indexes = indexes[:i+1] + index_back
                print(indexes)
    return S

def replace_2(S, indexes, sources, targets):
    info = sorted(zip(indexes, sources, targets))  # keep indexes in sorted order
    s = S[:info[0][0]]  # s stores our returned answer. Init it to the prefix of S that won't be touched
    for i in range(len(info)):
        val, source, target = info[i]
        t = 0
        if source == S[val: val + len(source)]:  # if our source matches the substring in S
            s += target  # then we are allowed to replace source with target
            t = len(source)
        s += S[t + val: info[i + 1][0] if i + 1 < len(info) else len(
            S)]  # append the piece of S between 2 consecutive find and and replace indexes
    return s


if __name__ == '__main__':
    res = find_replace_string(
        S='vmokgggqzp', indexes=[3, 5, 1], sources=["kg", "ggq", "mo"], targets=["s", "so", "bfr"])
    print(res)
