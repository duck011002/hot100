# 005. 最长回文子串 (Longest Palindromic Substring)

**难度**：中等  
**专题**：[16_多维动态规划](../)  
**原题链接**：<https://leetcode.cn/problems/longest-palindromic-substring/>

---

## 📌 题目描述

给你一个字符串 `s`，找到 `s` 中最长的回文子串。

---

## 🧪 示例

**示例 1：**

```
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
```

**示例 2：**

```
输入：s = "cbbd"
输出："bb"
```

---

## 📏 提示

- `1 <= s.length <= 1000`
- `s` 仅由数字和英文字母组成

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心扩展：分别以单字符、双字符为中心向两侧扩展
        def expand(l: int, r: int) -> None:
            nonlocal start, max_len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > max_len:
                start, max_len = l + 1, r - l - 1

        start, max_len = 0, 0
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        return s[start:start + max_len]
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/longest-palindromic-substring/) 在线判题，无需本地运行。
