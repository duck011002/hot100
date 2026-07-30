# 094. 二叉树的中序遍历 (Binary Tree Inorder Traversal)

**难度**：简单  
**专题**：[08_二叉树](../)  
**原题链接**：<https://leetcode.cn/problems/binary-tree-inorder-traversal/>

---

## 📌 题目描述

给定一个二叉树的根节点 `root` ，返回 **它的中序遍历** 。

---

## 🧪 示例

**示例 1：**

*（原题此处有配图，见原题链接）*

```
输入：root = [1,null,2,3]
输出：[1,3,2]
```

**示例 2：**

```
输入：root = []
输出：[]
```

**示例 3：**

```
输入：root = [1]
输出：[1]
```

---

## 📏 提示

- 树中节点数目在范围 `[0, 100]` 内
- `-100 <= Node.val <= 100`

**进阶**：递归算法很简单，你可以通过迭代算法完成吗？

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/binary-tree-inorder-traversal/) 在线判题，无需本地运行。
