# -*- coding: utf-8 -*-
# 001. 两数之和 (Two Sum) | 难度: 简单 | 专题: 01_哈希表
# https://leetcode.cn/problems/two-sum/
# 写完后直接将 class Solution 复制到 LeetCode 提交框在线判题，无需本地运行。

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[nums[i]] = i
