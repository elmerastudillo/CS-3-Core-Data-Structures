from hashtable import HashTable

# Indeed, CPython's sets are implemented as something like dictionaries 
# with dummy values (the keys being the members of the set), with some optimization(s) that exploit this lack of values

class Set(object):

	def __init__(self, elements=None):
		self.size = 0
		if elements is None:
			self.data = HashTable(4)
		else:
			self.data = HashTable(elements)


	def contains(self, element):
		"""return a boolean indicating whether element is in this set"""
		contain = self.data.contains(element)
		return contain


	def add(self, element):
		"""add element to this set, if not present already"""
		
		if element not in self.data.keys():
			self.data.set(element, None)
			self.size += 1
		else:
			raise ValueError("Element already exists in set")

	def remove(self, element):
		"""remove element from this set, if present, or else raise KeyError"""

		if element in self.data.keys():
			self.data.delete(element)
			self.size -= 1
		else:
			raise KeyError("Element not in set")

	def union(self, other_set):
		"""return a new set that is the union of this set and other_set"""
		new_set = self.data.keys()
		for element in other_set.keys():
			if self.data.keys().contains(element):
				continue
			else
				new_set.add(element)
		return Set(new_set)

	def intersection(self, other_set):
		"""return a new set that is the intersection of this set and other_set"""
		if other_set.keys and self.data is not None:
			new_set = Set()
			for element in other_set.keys():
				if self.data.keys().contains(element):
					new_set.add(element)
			return new_set
		else:
			return ValueError("Set is empty")

	def difference(self, other_set):
		"""return a new set that is the difference of this set and other_set"""
		if other_set and self.data is not None:
			new_set = Set()
			for element in self.data.keys():
				if other_set.keys().contains(element):
					self.data.remove(element)
			new_set = self.data.keys
			return new_set


	def is_subset(self, other_set):
		"""return a boolean indicating whether other_set is a subset of this set"""
		if other_set and self.data is not None:
			for element in other_set.keys():
				if self.data.keys().contains(element):
					continue
				else:
					return False
			return True


def test_set():
	new_set = Set()
	new_set.add("hi")
	new_set.add("why")
	new_set.add("where")
	new_set.add("anchovies")
	print(new_set.data)
	new_set.remove("hi")
	print(new_set.data)
	# print(new_set)

if __name__ == '__main__':
	test_set()
