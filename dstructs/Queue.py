class Queue:
	def __init__(self):
		self.items = []
		
	def enqueue(self,item):
		"""
			Takes an item and inserts it into the zeroth index of the list representing the Queue
			
			The runtime of this method is O(n) or linear time since inserting an item in the zeroth position of a list forces all other items to move to the next position.
		"""
		self.items.insert(0,item)
		
	def dequeue(self):
		if self.items:
			self.items.pop()
		else:
			return none
		
	def peek(self):
		
		
	def size(self):
		pass
		
	def is_empty(self):
		pass