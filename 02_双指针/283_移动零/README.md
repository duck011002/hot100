# 283. 移动零 (Move Zeroes)

**难度**：简单  
**专题**：[02_双指针](../)  
**原题链接**：<https://leetcode.cn/problems/move-zeroes/>

---

## 📌 题目描述

给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

**请注意**，必须在不复制数组的情况下原地对数组进行操作。

---

## 🧪 示例

**示例 1：**

```
输入：nums = [0,1,0,3,12]
输出：[1,3,12,0,0]
```

**示例 2：**

```
输入：nums = [0]
输出：[0]
```

---

## 📏 提示

- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

**进阶**：你能尽量减少完成的操作次数吗？

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/move-zeroes/) 在线判题，无需本地运行。
