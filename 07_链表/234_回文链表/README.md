# 234. 回文链表 (Palindrome Linked List)

**难度**：简单  
**专题**：[07_链表](../)  
**原题链接**：<https://leetcode.cn/problems/palindrome-linked-list/>

---

## 📌 题目描述

给你一个单链表的头节点 `head` ，请你判断该链表是否为回文链表。如果是，返回 `true` ；否则，返回 `false` 。

---

## 🧪 示例

**示例 1：**

*（原题此处有配图，见原题链接）*

```
输入：head = [1,2,2,1]
输出：true
```

**示例 2：**

*（原题此处有配图，见原题链接）*

```
输入：head = [1,2]
输出：false
```

---

## 📏 提示

- 链表中节点数目在范围 `[1, 10^5]` 内
- `0 <= Node.val <= 9`

**进阶**：你能否用 `O(n)` 时间复杂度和 `O(1)` 空间复杂度解决此题？

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 快慢指针找中点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 反转后半部分
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        # 双指针比较
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/palindrome-linked-list/) 在线判题，无需本地运行。
