# 019. 删除链表的倒数第 N 个结点 (Remove Nth Node From End of List)

**难度**：中等  
**专题**：[07_链表](../)  
**原题链接**：<https://leetcode.cn/problems/remove-nth-node-from-end-of-list/>

---

## 📌 题目描述

给你一个链表，删除链表的倒数第 `n` 个结点，并且返回链表的头结点。

---

## 🧪 示例

**示例 1：**

*（原题此处有配图，见原题链接）*

```
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
```

**示例 2：**

```
输入：head = [1], n = 1
输出：[]
```

**示例 3：**

```
输入：head = [1,2], n = 1
输出：[1]
```

---

## 📏 提示

- 链表中结点的数目为 `sz`
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

**进阶**：你能尝试使用一趟扫描实现吗？

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) 在线判题，无需本地运行。
