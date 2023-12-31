class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        enqueued_node = Node(data)
        if self.rear is None:
            self.front = self.rear = enqueued_node
        else:
            self.rear.next = enqueued_node
            self.rear = enqueued_node

    def dequeue(self):
        if self.front is None:
            return None
        else:
            dequeued_node = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return dequeued_node.data