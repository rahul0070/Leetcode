class LRUCache:
	def __init__(self, capacity):
		self.cache = {}
		self.hits = {}
		self.capacity = capacity
		self.maxVal = 0

	def get(self, key):
		if key in self.cache:
			self.maxVal += 1
			self.hits[key] = self.maxVal
			return self.cache[key]
		else:
			return -1

	def removeLRU(self):
		t = min(self.hits.items(), key=lambda x: x[1])
		self.hits.pop(t[0])
		self.cache.pop(t[0])

	def put(self, key, value):
		if key in self.cache or len(self.cache) < self.capacity:
			self.cache[key] = value
			self.maxVal += 1
			self.hits[key] = self.maxVal

		else:
			self.removeLRU()
			self.put(key, value)
		
