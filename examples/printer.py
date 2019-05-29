import random

class PrinterQueue:

	def __init__(self):
		self.items = []
	
	def enqueue(self, item):
		self.items.insert(0, item)
		
	def dequeue(self):
		if self.items:
			self.items.pop()
		else:
			return None
		
	def peek(self):
		if self.items:
			return self.items[-1]
		else:
			return None
		
	def size(self):
		return len(self.items)
		
		
	def is_empty(self):
		return self.items == []


class Job:
	
	def __init__(self):
		self.pages = random.randint(1, 11)
		
	def print_page(self):
		if self.pages > 0:
			self.pages -= 1
	
	def check_complete(self):
		if pages == 0:
			return True
		else:
			return False


class Printer:
	
	def __init__(self):
		self.current_job = None
		
	def get_job(self, printer_queue):
		if printer_queue.is_empty():
			print("No more jobs to print!")
		else:
			printer_queue.dequeue()
		
	def print_job(self, job):
		while job.pages > 0:
			job.print_page()
			
		if job.check_complete:
			print("Job Printed!")
		
		
		
		
		
		
