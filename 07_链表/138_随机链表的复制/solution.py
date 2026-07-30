# -*- coding: utf-8 -*-
# 138. 随机链表的复制 (Copy List with Random Pointer) | 难度: 中等 | 专题: 07_链表
# https://leetcode.cn/problems/copy-list-with-random-pointer/
# 写完后直接将 class Solution 复制到 LeetCode 提交框在线判题，无需本地运行。

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pass
