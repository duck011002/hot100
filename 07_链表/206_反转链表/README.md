# 206. 反转链表 (Reverse Linked List)

**难度**：简单  
**专题**：[07_链表](../)  
**原题链接**：<https://leetcode.cn/problems/reverse-linked-list/>

---

## 📌 题目描述

给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。

---

## 🧪 示例

**示例 1：**

```
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
```

**示例 2：**

```
输入：head = [1,2]
输出：[2,1]
```

**示例 3：**

```
输入：head = []
输出：[]
```

---

## 📏 提示

- 链表中节点的数目范围是 `[0, 5000]`
- `-5000 <= Node.val <= 5000`

**进阶**：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/reverse-linked-list/) 在线判题，无需本地运行。
