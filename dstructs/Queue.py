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
		"""
			Returns and remotes the front-most item of the Queue which is represented by the last item in the list.
			
			The runtime of this method is O(1).
		"""
		if self.items:
			self.items.pop()
		else:
			return none
	
	
	def peek(self):
		"""
			Return the last item on the list representing the front-most item in the Queue
			
			The runtime for this method is O(1)
		"""
		if self.items:
			return self.items[-1]
		else:
			return None
	
	
	def size(self):
		"""
			Method to return the lenght of the list representing the stack
			
			Runtime for this method is O(1)
		"""
		return len(self.items)
		
		
	def is_empty(self):
		"""
			Method to check if the stack list is empty
			
			Runtime for this method is O(1)
		"""	
		return self.items == []