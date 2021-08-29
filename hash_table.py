class Node(object):
	def __init__(self, key):
		self.key = key
		self.next = self.prev = None

class ListDoublyLinked():
	def __init__(self):
		self.head = None
	def insert(self, value):
		newNode = Node(value)
		newNode.next = self.head
		if self.head != None:
			self.head.prev = newNode
		self.head = newNode
	def search(self, value):
		temp = self.head
		while temp != None:
			if temp.key == value:
				return temp
			temp = temp.next
		return None
	def delete(self, value):
		temp = self.search(value)
		if temp != None:
			if temp.prev != None:
				temp.prev.next = temp.next
			else:
				self.head = temp.next
			if temp.next != None:
				temp.next.prev = temp.prev
			del temp

class HashTable(object):
	def __init__(self):
		self.size = 10
		self.table = [ListDoublyLinked() for x in range(self.size)]
	def insert(self, value):
		(self.table[value % self.size]).insert(value)
	def search(self, value):
		return (self.table[value % self.size]).search(value)
	def delete(self, value):
		(self.table[value % self.size]).delete(value)