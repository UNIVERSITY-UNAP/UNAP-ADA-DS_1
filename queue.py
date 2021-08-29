class Node:
    def __init__(self, value):
        self.value = value
        self.next = self.prev = None

class Queue:
    def __init__(self):
        self.head = self.tail = None
    def enqueue(self, val):
        newNode = Node(val)
        if not self.isEmpty():
            newNode.next = self.tail
        else:
            self.head = newNode
        self.tail = newNode
    def dequeue(self):
        if not self.isEmpty():
            temp = self.head
            if self.tail == self.head:
                self.tail = self.head = None
            else:
                self.head = self.head.prev
                self.head.next = None
            del temp
    def isEmpty(self):
        self.tail == None and self.head == None
    def size(self):
        temp = self.tail
        cont = 0
        while temp != None:
            temp = temp.next
            cont += 1
        return cont