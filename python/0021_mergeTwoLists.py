from typing import Optional


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        return " -> ".join(str(x) for x in nodes)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self, val=0, next=None):
        return val


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next


if __name__ == '__main__':
    llist_1 = LinkedList()
    node_1_1 = ListNode(1)
    node_1_2 = ListNode(2)
    node_1_3 = ListNode(4)
    llist_1.head = node_1_1
    node_1_1.next = node_1_2
    node_1_2.next = node_1_3

    llist_2 = LinkedList()
    node_2_1 = ListNode(1)
    node_2_2 = ListNode(3)
    node_2_3 = ListNode(4)
    llist_2.head = node_2_1
    node_2_1.next = node_2_2
    node_2_2.next = node_2_3

    s = Solution()
    s.mergeTwoLists(node_1_1, node_2_1)
    print(llist_2)