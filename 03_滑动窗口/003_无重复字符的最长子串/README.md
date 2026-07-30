# 003. 无重复字符的最长子串 (Longest Substring Without Repeating Characters)

**难度**：中等  
**专题**：[03_滑动窗口](../)  
**原题链接**：<https://leetcode.cn/problems/longest-substring-without-repeating-characters/>

---

## 📌 题目描述

给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长子串** 的长度。

---

## 🧪 示例

**示例 1：**

```
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

**示例 2：**

```
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

**示例 3：**

```
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

---

## 📏 提示

- `0 <= s.length <= 5 * 10^4`
- `s` 由英文字母、数字、符号和空格组成

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        ans = 0
        for right, ch in enumerate(s):
            while ch in window:
                window.remove(s[left])
                left += 1
            window.add(ch)
            ans = max(ans, right - left + 1)
        return ans
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) 在线判题，无需本地运行。
