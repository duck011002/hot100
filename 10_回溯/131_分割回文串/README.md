# 131. 分割回文串 (Palindrome Partitioning)

**难度**：中等  
**专题**：[10_回溯](../)  
**原题链接**：<https://leetcode.cn/problems/palindrome-partitioning/>

---

## 📌 题目描述

给你一个字符串 `s`，请你将 `s` 分割成一些 子串，使每个子串都是 **回文串** 。返回 `s` 所有可能的分割方案。

---

## 🧪 示例

**示例 1：**

```
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
```

**示例 2：**

```
输入：s = "a"
输出：[["a"]]
```

---

## 📏 提示

- `1 <= s.length <= 16`
- `s` 仅由小写英文字母组成

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []

        def backtrack(start: int) -> None:
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if sub == sub[::-1]:
                    path.append(sub)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return res
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/palindrome-partitioning/) 在线判题，无需本地运行。
