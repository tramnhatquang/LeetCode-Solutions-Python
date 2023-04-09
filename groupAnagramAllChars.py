import collections


def cleanSpecialChars(s):
	return ''.join([char.lower() for char in s if char.isalpha()])


def groupAnagramAllCharacters(list_words):
	map = collections.defaultdict(list)
	for word in list_words:
		clean_word = cleanSpecialChars(word)
		map[tuple(sorted(clean_word))].append(word)

	res = []
	for k, v in map.items():
		if len(v) >= 2:
			res.append(v)
	print(f'Res: {res}')
	return res


from unittest import TestCase


class Test(TestCase):

	def test_group_anagram_all_characters(self):
		self.assertTrue(groupAnagramAllCharacters(['eat', 'Ate.', 'ATE', 'tea!!!', 'horse', 'pipE']),
		                [['eat', 'Ate.', 'ATE', 'tea!!!']])
