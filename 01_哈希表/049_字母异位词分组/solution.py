# -*- coding: utf-8 -*-
# 049. 字母异位词分组 (Group Anagrams) | 难度: 中等 | 专题: 01_哈希表
# https://leetcode.cn/problems/group-anagrams/
# 写完后直接将 class Solution 复制到 LeetCode 提交框在线判题，无需本地运行。

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for str in strs:
            mp[str] += 1
        return [[]]
