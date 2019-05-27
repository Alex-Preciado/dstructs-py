
class Stack:
	
	def __init__(self):
		self.items = []
		
	def push(self, item):
		'''
		Accepts and item as a paremeter and appends it to the end of the list
		
		Returns nothing
		
		Runtime for this method is O(1)
		'''
		self.items.append(item)	
	
	
	def pop(self):
		'''
		Removes and returns the last item from the list which is the top item of the Stack
		
		Runtime for this method is O(1)
		'''
		
		if self.items:
			return self.items.pop()
		else:
			return None
		
	def peek(self):
		pass
		
	def size(self):
		pass
	
	def is_empty(self):
		pass