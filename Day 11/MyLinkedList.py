# https://leetcode.com/problems/design-linked-list/

class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
            
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.val = None
        self.next = None
        self.len = 0
        self.tail = None

    def update(self):
	    self.val = self.head.val
	    self.next = self.head.next

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        index += 1
        if index > self.len or index < 0:
            return -1
        head = self.head
        for i in range(index-1):
            head = head.next
        return head.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        head = self.head
        self.head = Node(val)
        self.head.next = head
        self.len += 1
        if not self.tail:
            self.tail = self.head
        self.update()


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.len, val)



    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        index += 1
        if self.len + 1 < index:
            return
        head = self.head
        if index == 1:
            self.head = Node(val)
            self.head.next = head
            self.len += 1
            return
        for i in range(index-2):
            head = head.next
        temp = head.next
        head.next = Node(val)
        head.next.next = temp
        if (index == self.len):
            self.tail = head.next
        self.len += 1
        self.update()


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        index += 1
        if self.len < index or index<0:
            return
        head = self.head
        if index == 1:
            self.head = self.head.next
            self.len -= 1
            return
        for i in range(index-2):
            head = head.next
        head.next = head.next.next
        if (index == self.len):
            self.tail = head
        self.len -= 1
        self.update()


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
