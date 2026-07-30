# 438. 找到字符串中所有字母异位词 (Find All Anagrams in a String)

**难度**：中等  
**专题**：[03_滑动窗口](../)  
**原题链接**：<https://leetcode.cn/problems/find-all-anagrams-in-a-string/>

---

## 📌 题目描述

给定两个字符串 `s` 和 `p`，找到 `s` 中所有 `p` 的 **异位词** 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

---

## 🧪 示例

**示例 1：**

```
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
```

**示例 2：**

```
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
```

---

## 📏 提示

- `1 <= s.length, p.length <= 3 * 10^4`
- `s` 和 `p` 仅包含小写字母

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if n < m:
            return []
        res = []
        p_count = Counter(p)
        window = Counter(s[:m])
        if window == p_count:
            res.append(0)
        for right in range(m, n):
            window[s[right]] += 1
            left_ch = s[right - m]
            window[left_ch] -= 1
            if window[left_ch] == 0:
                del window[left_ch]
            if window == p_count:
                res.append(right - m + 1)
        return res
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) 在线判题，无需本地运行。
