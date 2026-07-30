# 024. 两两交换链表中的节点 (Swap Nodes in Pairs)

**难度**：中等  
**专题**：[07_链表](../)  
**原题链接**：<https://leetcode.cn/problems/swap-nodes-in-pairs/>

---

## 📌 题目描述

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

---

## 🧪 示例

**示例 1：**

*（原题此处有配图，见原题链接）*

```
输入：head = [1,2,3,4]
输出：[2,1,4,3]
```

**示例 2：**

```
输入：head = []
输出：[]
```

**示例 3：**

```
输入：head = [1]
输出：[1]
```

---

## 📏 提示

- 链表中节点的数目在范围 `[0, 100]` 内
- `0 <= Node.val <= 100`

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
        return dummy.next
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/swap-nodes-in-pairs/) 在线判题，无需本地运行。
