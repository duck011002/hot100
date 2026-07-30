# 128. 最长连续序列 (Longest Consecutive Sequence)

**难度**：中等  
**专题**：[01_哈希表](../)  
**原题链接**：<https://leetcode.cn/problems/longest-consecutive-sequence/>

---

## 📌 题目描述

给定一个未排序的整数数组 `nums` ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 `O(n)` 的算法解决此问题。

---

## 🧪 示例

**示例 1：**

```
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
```

**示例 2：**

```
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
```

**示例 3：**

```
输入：nums = [1,0,1,2]
输出：3
```

---

## 📏 提示

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:  # 只从序列起点开始数
                curr = num
                length = 1
                while curr + 1 in num_set:
                    curr += 1
                    length += 1
                longest = max(longest, length)
        return longest
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/longest-consecutive-sequence/) 在线判题，无需本地运行。
