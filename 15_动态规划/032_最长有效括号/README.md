# 032. 最长有效括号 (Longest Valid Parentheses)

**难度**：困难  
**专题**：[15_动态规划](../)  
**原题链接**：<https://leetcode.cn/problems/longest-valid-parentheses/>

---

## 📌 题目描述

给你一个只包含 `'('` 和 `')'` 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

---

## 🧪 示例

**示例 1：**

```
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
```

**示例 2：**

```
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
```

**示例 3：**

```
输入：s = ""
输出：0
```

---

## 📏 提示

- `0 <= s.length <= 3 * 10^4`
- `s[i]` 为 `'('` 或 `')'`

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n  # dp[i]: 以 s[i] 结尾的最长有效括号长度
        ans = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2
                    if i - dp[i - 1] - 2 >= 0:
                        dp[i] += dp[i - dp[i - 1] - 2]
                ans = max(ans, dp[i])
        return ans
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/longest-valid-parentheses/) 在线判题，无需本地运行。
