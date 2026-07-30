# 079. 单词搜索 (Word Search)

**难度**：中等  
**专题**：[10_回溯](../)  
**原题链接**：<https://leetcode.cn/problems/word-search/>

---

## 📌 题目描述

给定一个 `m x n` 二维字符网格 `board` 和一个字符串单词 `word` 。如果 `word` 存在于网格中，返回 `true` ；否则，返回 `false` 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中"相邻"单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

---

## 🧪 示例

**示例 1：**

*（原题此处有配图，见原题链接）*

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
```

**示例 2：**

*（原题此处有配图，见原题链接）*

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
```

**示例 3：**

*（原题此处有配图，见原题链接）*

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
```

---

## 📏 提示

- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` 和 `word` 仅由大小写英文字母组成

**进阶**：你可以使用搜索剪枝的技术来优化解决方案，使其在 `board` 更大的情况下可以更快解决问题？

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r: int, c: int, k: int) -> bool:
            if board[r][c] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[r][c] = "#"  # 标记已访问
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < m and 0 <= nc < n and dfs(nr, nc, k + 1):
                    board[r][c] = word[k]
                    return True
            board[r][c] = word[k]  # 回溯还原
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/word-search/) 在线判题，无需本地运行。
