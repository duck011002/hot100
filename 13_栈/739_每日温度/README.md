# 739. 每日温度 (Daily Temperatures)

**难度**：中等  
**专题**：[13_栈](../)  
**原题链接**：<https://leetcode.cn/problems/daily-temperatures/>

---

## 📌 题目描述

给定一个整数数组 `temperatures` ，表示每天的温度，返回一个数组 `answer` ，其中 `answer[i]` 是指对于第 `i` 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 `0` 来代替。

---

## 🧪 示例

**示例 1：**

```
输入：temperatures = [73,74,75,71,69,72,76,73]
输出：[1,1,4,2,1,1,0,0]
```

**示例 2：**

```
输入：temperatures = [30,40,50,60]
输出：[1,1,1,0]
```

**示例 3：**

```
输入：temperatures = [30,60,90]
输出：[1,1,0]
```

---

## 📏 提示

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 单调递减栈：栈中保存尚未找到更高温度的下标
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        return answer
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/daily-temperatures/) 在线判题，无需本地运行。
