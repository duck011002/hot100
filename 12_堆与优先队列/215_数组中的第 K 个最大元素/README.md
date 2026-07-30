# 215. 数组中的第 K 个最大元素 (Kth Largest Element in an Array)

**难度**：中等  
**专题**：[12_堆与优先队列](../)  
**原题链接**：<https://leetcode.cn/problems/kth-largest-element-in-an-array/>

---

## 📌 题目描述

给定整数数组 `nums` 和整数 `k`，请返回数组中第 `k` 个最大的元素。

请注意，你需要找的是数组排序后的第 `k` 个最大的元素，而不是第 `k` 个不同的元素。

你必须设计并实现时间复杂度为 `O(n)` 的算法解决此问题。

---

## 🧪 示例

**示例 1：**

```
输入：[3,2,1,5,6,4], k = 2
输出：5
```

**示例 2：**

```
输入：[3,2,3,1,2,4,5,5,6], k = 4
输出：4
```

---

## 📏 提示

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 维护一个大小为 k 的小顶堆，堆顶即第 k 个最大元素
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/kth-largest-element-in-an-array/) 在线判题，无需本地运行。
