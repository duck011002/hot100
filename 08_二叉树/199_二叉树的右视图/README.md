# 199. 二叉树的右视图 (Binary Tree Right Side View)

**难度**：中等  
**专题**：[08_二叉树](../)  
**原题链接**：<https://leetcode.cn/problems/binary-tree-right-side-view/>

---

## 📌 题目描述

给定一个二叉树的 **根节点** `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

---

## 🧪 示例

**示例 1：**

*（原题此处有配图，见原题链接）*

```
输入：root = [1,2,3,null,5,null,4]
输出：[1,3,4]
```

**示例 2：**

*（原题此处有配图，见原题链接）*

```
输入：root = [1,2,3,4,null,null,null,5]
输出：[1,3,4,5]
```

**示例 3：**

```
输入：root = [1,null,3]
输出：[1,3]
```

**示例 4：**

```
输入：root = []
输出：[]
```

---

## 📏 提示

- 二叉树的节点个数的范围是 `[0,100]`
- `-100 <= Node.val <= 100`

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res, queue = [], deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/binary-tree-right-side-view/) 在线判题，无需本地运行。
