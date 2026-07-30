# 076. 最小覆盖子串 (Minimum Window Substring)

**难度**：困难  
**专题**：[04_子串](../)  
**原题链接**：<https://leetcode.cn/problems/minimum-window-substring/>

---

## 📌 题目描述

给你一个字符串 `s` 、一个字符串 `t` 。返回 `s` 中涵盖 `t` 所有字符的最小子串。如果 `s` 中不存在涵盖 `t` 所有字符的子串，则返回空字符串 `""` 。

**注意：**

- 对于 `t` 中重复字符，我们寻找的子字符串中该字符数量必须不少于 `t` 中该字符数量。
- 如果 `s` 中存在这样的子串，我们保证它是唯一的答案。

---

## 🧪 示例

**示例 1：**

```
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
```

**示例 2：**

```
输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
```

**示例 3：**

```
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
```

---

## 📏 提示

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` 和 `t` 由英文字母组成

**进阶**：你能设计一个在 `o(m+n)` 时间内解决此问题的算法吗？

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)          # 窗口中还缺少的字符总数
        left = 0
        best_left, best_right = 0, -1  # 记录最优窗口 [best_left, best_right]
        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            if missing == 0:      # 窗口已覆盖 t，收缩左边界
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if best_right == -1 or right - left < best_right - best_left:
                    best_left, best_right = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[best_left:best_right + 1]
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/minimum-window-substring/) 在线判题，无需本地运行。
