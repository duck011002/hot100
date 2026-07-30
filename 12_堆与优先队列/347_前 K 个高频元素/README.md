# 347. 前 K 个高频元素 (Top K Frequent Elements)

**难度**：中等  
**专题**：[12_堆与优先队列](../)  
**原题链接**：<https://leetcode.cn/problems/top-k-frequent-elements/>

---

## 📌 题目描述

给你一个整数数组 `nums` 和一个整数 `k` ，请你返回其中出现频率前 `k` 高的元素。你可以按 **任意顺序** 返回答案。

---

## 🧪 示例

**示例 1：**

```
输入：nums = [1,1,1,2,2,3], k = 2
输出：[1,2]
```

**示例 2：**

```
输入：nums = [1], k = 1
输出：[1]
```

---

## 📏 提示

- `1 <= nums.length <= 10^5`
- `k` 的取值范围是 `[1, 数组中不相同的元素的个数]`
- 题目数据保证答案唯一，换句话说，数组中前 `k` 个高频元素的集合是唯一的

**进阶**：你所设计算法的时间复杂度 **必须** 优于 `O(n log n)` ，其中 `n` 是数组大小。

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # 按出现频率取前 k 大，堆大小为 k，复杂度 O(n log k)
        return heapq.nlargest(k, count.keys(), key=count.get)
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/top-k-frequent-elements/) 在线判题，无需本地运行。
