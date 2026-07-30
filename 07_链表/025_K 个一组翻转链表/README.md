# 025. K 个一组翻转链表 (Reverse Nodes in k-Group)

**难度**：困难  
**专题**：[07_链表](../)  
**原题链接**：<https://leetcode.cn/problems/reverse-nodes-in-k-group/>

---

## 📌 题目描述

给你链表的头节点 `head` ，每 `k` 个节点一组进行翻转，请你返回修改后的链表。

`k` 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 `k` 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

---

## 🧪 示例

**示例 1：**

*（原题此处有配图，见原题链接）*

```
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
```

**示例 2：**

*（原题此处有配图，见原题链接）*

```
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
```

---

## 📏 提示

- 链表中的节点数目为 `n`
- `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`

**进阶**：你可以设计一个只用 `O(1)` 额外内存空间的算法解决此问题吗？

---

## 💡 解题思路与参考代码

<details>
<summary><b>点击展开参考代码 (独立思考后再看哦)</b></summary>

```python
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            # 检查剩余节点是否够 k 个
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            # 翻转当前组
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            # 接回前后
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
```

</details>

---

## ✍️ 练习方式

1. 在同目录 `solution.py` 的 `class Solution` 中作答（签名与 LeetCode 提交框完全一致）。
2. 写完后将 `class Solution` 部分复制到 [LeetCode 提交页](https://leetcode.cn/problems/reverse-nodes-in-k-group/) 在线判题，无需本地运行。
