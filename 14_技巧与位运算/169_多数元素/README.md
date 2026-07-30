# 169. 多数元素 (Majority Element)

**难度**：简单  
**专题**：[14_技巧与位运算](../)  
**原题链接**：<https://leetcode.cn/problems/majority-element/>

---

## 📌 题目描述

给定一个大小为 `n` 的数组 `nums` ，返回其中的多数元素。多数元素是指在数组中出现次数 **大于** `⌊ n/2 ⌋` 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

---

## 🧪 示例

**示例 1：**

```
输入：nums = [3,2,3]
输出：3
```

**示例 2：**

```
输入：nums = [2,2,1,1,1,2,2]
输出：2
```

---

## 📏 提示

- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

**进阶**：尝试设计时间复杂度为 `O(n)`、空间复杂度为 `O(1)` 的算法解决此问题。

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore 投票算法
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/majority-element/) 在线判题，无需本地运行。
