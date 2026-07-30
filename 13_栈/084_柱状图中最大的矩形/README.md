# 084. 柱状图中最大的矩形 (Largest Rectangle in Histogram)

**难度**：困难  
**专题**：[13_栈](../)  
**原题链接**：<https://leetcode.cn/problems/largest-rectangle-in-histogram/>

---

## 📌 题目描述

给定 `n` 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 `1` 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

---

## 🧪 示例

**示例 1：**

*（原题此处有配图，见原题链接）*

```
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
```

**示例 2：**

*（原题此处有配图，见原题链接）*

```
输入： heights = [2,4]
输出： 4
```

---

## 📏 提示

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调递增栈：出栈时以出栈柱子高度为矩形高，左右边界确定宽度
        stack = []
        res = 0
        heights = [0] + heights + [0]  # 首尾加哨兵，简化边界处理
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                mid = stack.pop()
                width = i - stack[-1] - 1
                res = max(res, heights[mid] * width)
            stack.append(i)
        return res
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/largest-rectangle-in-histogram/) 在线判题，无需本地运行。
