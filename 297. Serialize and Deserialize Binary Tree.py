# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
	def serialize(self, root):
		if root is None:
			return '#'
		return '{} {} {}'.format(root.val, self.serialize(root.left), self.serialize(root.right))

	# time = space = O(n)
	def deserialize(self, data):
		def helper():
			val = next(vals)
			if val == '#':
				return None
			node = TreeNode(int(val))
			node.left = helper()
			node.right = helper()
			return node

		vals = iter(data.split())
		return helper()

	# time = space = O(n)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))