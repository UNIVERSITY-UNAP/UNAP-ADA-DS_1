class Node(object):
	def __init__(self, key):
		self.key = key
		self.next = self.prev = None

class ListDoublyLinkedC():
	def __init__(self):
		self.nil = Node(None)
	def insert(self, value):
		newNode = Node(value)
		newNode.next = self.nil.next
		self.nil.next.prev = newNode
		self.nil.next = newNode
		newNode.prev = self.nil
	def search(self, value)->Node:
		temp = self.head
		while temp != self.nil:
			if temp.key == value:
				return temp
			temp = temp.next
		return None
	def delete(self, value):
		temp = self.search(value)
		temp.prev.next = temp.next
		temp.next.prev = temp.prev
		del temp