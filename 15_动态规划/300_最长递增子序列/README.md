# 300. 最长递增子序列 (Longest Increasing Subsequence)

**难度**：中等  
**专题**：[15_动态规划](../)  
**原题链接**：<https://leetcode.cn/problems/longest-increasing-subsequence/>

---

## 📌 题目描述

给你一个整数数组 `nums` ，找到其中最长严格递增子序列的长度。

**子序列** 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，`[3,6,2,7]` 是数组 `[0,3,1,6,2,2,7]` 的子序列。

---

## 🧪 示例

**示例 1：**

```
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
```

**示例 2：**

```
输入：nums = [0,1,0,3,2,3]
输出：4
```

**示例 3：**

```
输入：nums = [7,7,7,7,7,7,7]
输出：1
```

---

## 📏 提示

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

**进阶**：你能将算法的时间复杂度降低到 `O(n log(n))` 吗?

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 贪心 + 二分：tails[i] 为长度 i+1 的递增子序列的最小结尾，O(n log n)
        import bisect
        tails = []
        for x in nums:
            pos = bisect.bisect_left(tails, x)
            if pos == len(tails):
                tails.append(x)
            else:
                tails[pos] = x
        return len(tails)
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/longest-increasing-subsequence/) 在线判题，无需本地运行。
