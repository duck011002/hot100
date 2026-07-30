# 118. 杨辉三角 (Pascal's Triangle)

**难度**：简单  
**专题**：[15_动态规划](../)  
**原题链接**：<https://leetcode.cn/problems/pascals-triangle/>

---

## 📌 题目描述

给定一个非负整数 `numRows`，生成「杨辉三角」的前 `numRows` 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

*（原题此处有配图，见原题链接）*

---

## 🧪 示例

**示例 1：**

```
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**示例 2：**

```
输入: numRows = 1
输出: [[1]]
```

---

## 📏 提示

- `1 <= numRows <= 30`

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            prev = res[-1]
            row = [1] + [prev[j] + prev[j + 1] for j in range(len(prev) - 1)] + [1]
            res.append(row)
        return res
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/pascals-triangle/) 在线判题，无需本地运行。
