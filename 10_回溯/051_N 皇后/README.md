# 051. N 皇后 (N-Queens)

**难度**：困难  
**专题**：[10_回溯](../)  
**原题链接**：<https://leetcode.cn/problems/n-queens/>

---

## 📌 题目描述

按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

**n 皇后问题** 研究的是如何将 `n` 个皇后放置在 `n×n` 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 `n` ，返回所有不同的 **n 皇后问题** 的解决方案。

每一种解法包含一个不同的 **n 皇后问题** 的棋子放置方案，该方案中 `'Q'` 和 `'.'` 分别代表了皇后和空位。

---

## 🧪 示例

**示例 1：**

*（原题此处有配图，见原题链接）*

```
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
```

**示例 2：**

```
输入：n = 1
输出：[["Q"]]
```

---

## 📏 提示

- `1 <= n <= 9`

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queens = [-1] * n  # queens[r] = 皇后所在列
        cols, diag1, diag2 = set(), set(), set()

        def backtrack(r: int) -> None:
            if r == n:
                res.append(["." * q + "Q" + "." * (n - q - 1) for q in queens])
                return
            for c in range(n):
                if c in cols or r + c in diag1 or r - c in diag2:
                    continue
                queens[r] = c
                cols.add(c)
                diag1.add(r + c)
                diag2.add(r - c)
                backtrack(r + 1)
                cols.remove(c)
                diag1.remove(r + c)
                diag2.remove(r - c)

        backtrack(0)
        return res
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/n-queens/) 在线判题，无需本地运行。
