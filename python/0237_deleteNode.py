class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return self.val


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    llist = LinkedList()
    node_1 = ListNode("a")
    node_2 = ListNode("b")
    node_3 = ListNode("c")
    node_4 = ListNode("d")

    llist.head = node_1
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    print(llist)

    s = Solution()
    s.deleteNode(node_3)
    print(llist)