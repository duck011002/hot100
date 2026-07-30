# 022. 括号生成 (Generate Parentheses)

**难度**：中等  
**专题**：[10_回溯](../)  
**原题链接**：<https://leetcode.cn/problems/generate-parentheses/>

---

## 📌 题目描述

数字 `n` 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 **有效的** 括号组合。

---

## 🧪 示例

**示例 1：**

```
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
```

**示例 2：**

```
输入：n = 1
输出：["()"]
```

---

## 📏 提示

- `1 <= n <= 8`

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, path = [], []

        def backtrack(left: int, right: int) -> None:
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            if left < n:
                path.append("(")
                backtrack(left + 1, right)
                path.pop()
            if right < left:
                path.append(")")
                backtrack(left, right + 1)
                path.pop()

        backtrack(0, 0)
        return res
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/generate-parentheses/) 在线判题，无需本地运行。
