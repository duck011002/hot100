# 152. 乘积最大子数组 (Maximum Product Subarray)

**难度**：中等  
**专题**：[15_动态规划](../)  
**原题链接**：<https://leetcode.cn/problems/maximum-product-subarray/>

---

## 📌 题目描述

给你一个整数数组 `nums` ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 **32-位** 整数。

---

## 🧪 示例

**示例 1：**

```
输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
```

**示例 2：**

```
输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
```

---

## 📏 提示

- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- `nums` 的任何子数组的乘积都 **保证** 是一个 **32-位** 整数

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 同时维护以当前元素结尾的最大、最小乘积（负数相乘会翻转大小）
        ans = cur_max = cur_min = nums[0]
        for x in nums[1:]:
            candidates = (x, cur_max * x, cur_min * x)
            cur_max, cur_min = max(candidates), min(candidates)
            ans = max(ans, cur_max)
        return ans
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/maximum-product-subarray/) 在线判题，无需本地运行。
