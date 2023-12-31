class Stack:
    def __init__(self, size):
        self.size = size
        self.List = [None] * size
        self.top = 0

    def size(self):
        return self.top


    def is_empty(self):
        if self.top==0:
            return True
        else:
            return False

    def push(self, item):
        if self.top < self.size:
            self.List[self.top] = item
            self.top += 1

    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.List[self.top]

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.List[self.top - 1]
