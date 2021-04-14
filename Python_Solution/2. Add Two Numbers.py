# Medium

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def traverse(self, l) -> list:
        array = []
        while l:
            val = str(l.val)
            array.append(val)
            l = l.next
        return array

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        array1 = self.traverse(l1)
        array2 = self.traverse(l2)

        x1 = int("".join(array1)[::-1])
        x2 = int("".join(array2)[::-1])

        sum = str(x1 + x2)[::-1]

        new_listnode = ListNode()

        current_node = new_listnode

        for i in range(len(sum)):
            current_node.val = int(sum[i])
            if i < len(sum) - 1:
                current_node.next = ListNode()
            current_node = current_node.next

        return new_listnode
