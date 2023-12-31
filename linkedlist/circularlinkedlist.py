class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def InsertAtIndex(self, data, index):
        if index < 0 or index > self.size:
            return

    new_node = Node(data)
    if index == 0:
        if self.head is None:
            self.head = new_node
            new_node.next = new_node  
        else:
            new_node.next = self.head
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            self.head = new_node
    else:
    
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node

        self.size += 1

    def InsertAtBegin(self, data):
        self.InsertAtIndex(data, 0)

    def InsertAtEnd(self, data):
        self.InsertAtIndex(data, self.size)

    def UpdateNode(self, data, index):
        if index < 0 or index >= self.size:
            return

        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        cur.data = data

    def RemoveNodeAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        if self.size == 1:
            removed_data = self.head.data
            self.head = None
        elif index == 0:
            removed_data = self.head.data
            self.head.data = self.head.next.data
            self.head.next = self.head.next.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            removed_data = cur.next.data
            cur.next = cur.next.next

        self.size -= 1
        return removed_data

    def RemoveNodeAtBegin(self):
        return self.RemoveNodeAtIndex(0)

    def RemoveNodeAtEnd(self):
        return self.RemoveNodeAtIndex(self.size - 1)

    def SizeOfList(self):
        return self.size

    def Concatenate(self, other_list):
        if not isinstance(other_list, CircularLinkedList):
            return

        if self.size == 0:
            self.head = other_list.head
        elif other_list.size > 0:
            cur = self.head.next
            self.head.next = other_list.head.next
            other_list.head.next = cur

        self.size += other_list.size

    def Invert(self):
        if self.size > 1:
            prev = None
            cur = self.head
            next_node = None

            for _ in range(self.size):
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node

            self.head = prev
