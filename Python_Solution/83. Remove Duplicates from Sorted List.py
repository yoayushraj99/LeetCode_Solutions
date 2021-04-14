# Easy

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        current_node = head
        while current_node:
            if current_node.next and current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return head
