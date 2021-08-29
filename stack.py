class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class Stack(object):
	def __init__(self):
		self.top = None
	def push(self, value):
		newNode = Node(value)
		if self.top != None:
			newNode.next = self.top
		self.top = newNode
	def pop(self):
		if not self.isEmpty():
			temp = self.top
			self.top = self.top.next
			del temp
	def isEmpty(self):
		return self.top == None

def printPilaAsStr(S):
	tempNode = S.top
	stackAux = Stack()
	while tempNode != None:
		stackAux.push(tempNode.value)
		tempNode = tempNode.next
	tempNode2 = stackAux.top
	cad = ''
	while tempNode2 != None:
		cad += tempNode2.value
		tempNode2 = tempNode2.next
		if tempNode2 != None:
			cad += " "
	return cad