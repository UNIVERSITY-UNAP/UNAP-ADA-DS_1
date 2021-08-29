class Node:
	def __init__(self, val):
		self.left = self.right = -2
		self.val = val
class Three:
	def __init__(self):
		self.size = 20
		self.arr = [Node(0) for _ in range(self.size)]
		self.root = self.arr[0]
	def PushLeft(self, actual, val):
		if self.isEmpty(self.root):
			self.root.left = self.root.right = -1
			self.root.val = val
		else:
			i = 0
			while self.arr[i].left != -2 and i < self.size:
				i += 1
			self.arr[i].left = self.arr[i].right = -1
			self.arr[i].val = val
			actual.left = i
			
	def PushRight(self, actual, val):
		if self.isEmpty(self.root):
			self.root.left = self.root.right = -1
			self.root.val = val
		else:
			i = 0
			while self.arr[i].right != -2 and i < self.size:
				i += 1
			self.arr[i].left = self.arr[i].right = -1
			self.arr[i].val = val
			actual.right = i
	
	def Left(self, actual):
		if not self.isEmpty(actual) or not self.isLeaf(actual):
			return self.arr[actual.left]
	
	def Right(self, actual):
		if not self.isEmpty(actual) or not self.isLeaf(actual):
			return self.arr[actual.right]
	
	def isEmpty(self, actual):
		return actual.left == -2 and actual.right == -2

	def isLeaf(self, actual):
		return actual.left == -1 and actual.right == -1