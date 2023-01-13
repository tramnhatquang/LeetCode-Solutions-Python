def capitalize(string: str) -> str:
	"""
	Capitalize other characters in the string
	:param string:
	:type string:
	:return:
	:rtype:
	"""
	string_lst = list(string)
	for i in range(len(string_lst)):
		if i % 2 == 0:
			string_lst[i] = string_lst[i].upper()
		else:
			string_lst[i] = string_lst[i].lower()

	# print(''.join(string_lst))
	return ''.join(string_lst)


# time: O(n) = space


if __name__ == '__main__':
	assert capitalize('') == ''
	assert capitalize('ab') == 'Ab'
	assert capitalize('hello') == 'HeLlO'
	assert capitalize('qUaNg') == 'QuAnG'
	assert capitalize('qUaNg!!!') == 'QuAnG!!!'
