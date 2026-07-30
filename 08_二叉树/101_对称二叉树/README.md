# 101. 对称二叉树 (Symmetric Tree)

**难度**：简单  
**专题**：[08_二叉树](../)  
**原题链接**：<https://leetcode.cn/problems/symmetric-tree/>

---

## 📌 题目描述

给你一个二叉树的根节点 `root` ， 检查它是否轴对称。

---

## 🧪 示例

**示例 1：**

*（原题此处有配图，见原题链接）*

```
输入：root = [1,2,2,3,4,4,3]
输出：true
```

**示例 2：**

*（原题此处有配图，见原题链接）*

```
输入：root = [1,2,2,null,3,null,3]
输出：false
```

---

## 📏 提示

- 树中节点数目在范围 `[1, 1000]` 内
- `-100 <= Node.val <= 100`

**进阶**：你可以运用递归和迭代两种方法解决这个问题吗？

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(a, b):
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            return mirror(a.left, b.right) and mirror(a.right, b.left)

        return mirror(root.left, root.right)
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/symmetric-tree/) 在线判题，无需本地运行。
