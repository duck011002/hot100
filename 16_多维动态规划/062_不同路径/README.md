# 062. 不同路径 (Unique Paths)

**难度**：中等  
**专题**：[16_多维动态规划](../)  
**原题链接**：<https://leetcode.cn/problems/unique-paths/>

---

## 📌 题目描述

一个机器人位于一个 `m x n` 网格的左上角（起始点在下图中标记为 "Start" ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 "Finish" ）。

问总共有多少条不同的路径？

---

## 🧪 示例

**示例 1：**

*（原题此处有配图，见原题链接）*

```
输入：m = 3, n = 7
输出：28
```

**示例 2：**

```
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
```

**示例 3：**

```
输入：m = 7, n = 3
输出：28
```

**示例 4：**

```
输入：m = 3, n = 3
输出：6
```

---

## 📏 提示

- `1 <= m, n <= 100`
- 题目数据保证答案小于等于 `2 * 10^9`

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 一维滚动数组：dp[j] 表示到达当前行第 j 列的路径数
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/unique-paths/) 在线判题，无需本地运行。
