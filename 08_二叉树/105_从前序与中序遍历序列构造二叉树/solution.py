# -*- coding: utf-8 -*-
# 105. 从前序与中序遍历序列构造二叉树 (Construct Binary Tree from Preorder and Inorder Traversal) | 难度: 中等 | 专题: 08_二叉树
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 写完后直接将 class Solution 复制到 LeetCode 提交框在线判题，无需本地运行。

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass
