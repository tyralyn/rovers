class bijectmap:
	def __init__(self):
		self.map1={}
		self.map2={}
	def remove(self, key):
		try:
			val= self.map1.pop(key)
			self.map2.pop(val)
		except KeyError:
			pass
		try:
			val= self.map2.pop(key)
			self.map1.pop(val)
		except KeyError:
			pass
	#takes a pair of items
	#if either of them exists the maps, replace
	#otherwise, just add them
	def add(self, key1, key2):
		self.remove(key1)
		self.remove(key2)
		self.map1[key1]=key2
		self.map2[key2]=key1

	def addDict(self, d):
		for item in d:
			self.add(item, d[item])
	def printMap(self):
		print (self.map1)
		print (self.map2)
	def get(self,key):
		if key in self.map1: 
			return self.map1[key] 
		elif key in self.map2:
			return self.map2[key]
		else:
			return None

