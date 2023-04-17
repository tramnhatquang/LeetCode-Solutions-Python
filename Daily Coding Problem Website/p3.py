from Utility.TreeNode import TreeNode

"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
"""


def serialize(root: TreeNode):
	if root is None:
		return '#'
	return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))


def deserialize(data):
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
