class UnionFind:
	def __init__(self, items):
		'''
		Initialize the union-find data structure to have the set of items
		partitioned into singleton groups and set the rank of each item to 0.
		'''
		for i in list(items):
			self._parent = {v:v for v in items}
			self._rank = {v:0 for v in items}

	def union(self, u, v):
		'''
		If x and y were not in the same group, then merge these groups.  Returns
		True if and only if there were different groups before the merger.
		'''
		ru = self.find(u)
		rv = self.find(v)

		if ru == rv:
			return False
		# connects the lower ranked item pointed to the higher rank
		if self._rank[ru] < self._rank[rv]:
			self._parent[ru] = rv
		elif self._rank[ru] > self._rank[rv]:
			self._parent[rv] = ru
		else: # equal rank: connect items and increase rank of parent
			self._parent[ru] = rv
			self._rank[rv] += 1
		return True

	def find(self, u):
		'''
		Find the item that is representing the set containing u.  Do 'path
		compression' to guarantee low running time.
		'''
		if u != self._parent[u]:
			self._parent[u] = self.find(self._parent[u])
		return self._parent[u]