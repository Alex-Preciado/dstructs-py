class Deque:
	
	def __init__(self):
		self.items = []

	def add_front(self, item):
		"""
			Inserts an item into the 0th index of the list representing the Deque.
			
			Runtime of this method is linear, or O(n), because every time an item is inserted at the front of the list, all other items are shifted on position to the right.
		"""
		self.items.insert(0,item)
		
	def add_rear(self, item):
		"""
			Appends an item at the end of the list representing the Deque.
			
			Runtime of this method is O(1).
		"""
		self.items.append(item)
		
	def remove_front(self):
		"""
			Removes the first item of the list representing the Deque.
			
			Runtime of this method is linear, or O(n), as each item has to be shifted one position to the left when we remove the first item of the list.
		"""
		if self.items:
			return self.items.pop(0)
		else:
			return None
		
	def remove_rear(self):
		"""
			Removes the last item of the list representing the Deque.
			
			Runtime of this method is O(1) because this only removes the last item leaving the rest intact.
		"""
	
		if self.items:
			return self.items.pop( )
		else:
			return None
	
	def peek_front(self):
		"""
			Returns the first item of the list representing the Deque.

			Runtime of this method is O(1).
		"""
		if self.items:
			return self.items[0]
		else:
			return None
		
	def peek_rear(self):
		"""
			Returns the last item of the list representing the Deque.

			Runtime of this method is O(1).
		"""

		if self.items:
			return self.items[-1]
		else:
			return None
	
	def size(self):
		"""
			Method to return the lenght of the list representing the Deque.
			
			Runtime for this method is O(1)
		"""
		return len(self.items)
		
		
	def is_empty(self):
		"""
			Method to check if the Deque's list is empty.
			
			Runtime for this method is O(1)
		"""	
		return self.items == []