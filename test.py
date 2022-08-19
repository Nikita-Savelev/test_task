
# Задание 1
def isEven(value): return value%2==0

def isEven1(value):
	if value & 1:       
		return False
	else:
		return True
# первый вариант более читаемый и лаконичный, второй возможно чуть более быстрый





# Задание 2 

# Вариант 1
class Node():
	def __init__(self, data, next_node, count):
		self.data = data
		self.next = next_node
		self.count = count


class CircularBuffer():
	def __init__(self, size):
		self.size = size
		self.first = None
		self.tail = None
		self.full_bufer = False

	def add(self, data):
		if self.first is None:
			node = Node(data, self.first, 1)
			self.first = node
			self.tail = node
			node.next = node
		else:
			if self.full_bufer:
				node = self.first
				for i in range(self.size):
					if node.count == 1:
						node.data = data
						node.count = self.tail.count
					else:
						node.count -= 1
					node = node.next
				self.full_bufer = True
			else:
				node = Node(data, self.first, self.tail.count + 1)
				self.tail.next = node
				self.tail = node
				if self.tail.count == self.size:
					self.full_bufer = True
		
	def get(self):
		data = self.first.data
		self.tail.next = self.first
		self.tail = self.first
		self.first = self.first.next
		return data

# Вариант 2
class CircularBuffer1():
	def __init__(self, size):
		self.size = size
		self.buf = []
		self.head = 0


	def add(self, data):
		if self.head is None:
			self.buf.append(data)
		else:
			if len(self.buf) == self.size:
				self.buf.pop(0)
				self.buf.append(data)
			else:
				self.buf.append(data)

	def get(self):
		data = self.buf[self.head]
		if self.head == len(self.buf) - 1:
			self.head = 0
		else:
			self.head += 1
		return data

# первый вариант реализации при добавлении элемента в заполненый буфер перезаписывает самый старый элемент и использует одни и те же пространства памяти, может быть более узко настроен
# второй вариант более читаемый, простой и быстрый(так как при добавлении элемента в заполненый буфер не проходит по каждому элементу), но использует разные адреса памяти так как добавление элемента не перезаписывает уже занятое место в памяти предыдущим элементом




# Задание 3

def sorting(array):
	if len(array) <= 1:
		return array
	else:
		mid = array.pop(0)
		less = []
		larger = []
		for item in array:
			if item < mid: 
				less.append(item)
			else:
				larger.append(item)
	return sorting(less) + [mid] +  sorting(larger)

# для выполнения задания 3 я выбрал алгоритм быстрой сортировки потому как в среднем он будет выполняться за время О(n log n)