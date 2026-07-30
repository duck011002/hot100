# 070. 爬楼梯 (Climbing Stairs)

**难度**：简单  
**专题**：[15_动态规划](../)  
**原题链接**：<https://leetcode.cn/problems/climbing-stairs/>

---

## 📌 题目描述

假设你正在爬楼梯。需要 `n` 阶你才能到达楼顶。

每次你可以爬 `1` 或 `2` 个台阶。你有多少种不同的方法可以爬到楼顶呢？

---

## 🧪 示例

**示例 1：**

```
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
```

**示例 2：**

```
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
```

---

## 📏 提示

- `1 <= n <= 45`

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1  # 分别表示爬到第 i-1、i 阶的方法数
        for _ in range(n - 1):
            a, b = b, a + b
        return b
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/climbing-stairs/) 在线判题，无需本地运行。
