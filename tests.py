import unittest
from frequency import most_frequent_words

class FrequencyTestCase(unittest.TestCase):

	def setUp(self):
		"""Initialize a corpus to be used for tests."""
		self.corpus = "cat cat bat cat bat tiger cat whale tiger dolphin bat"

	def test_core_functionality(self):
		"""Make sure the most frequent words function returns what we expect it to."""
		self.assertEqual(['cat'], most_frequent_words(self.corpus, 1))
		self.assertEqual(['cat', 'bat'], most_frequent_words(self.corpus, 2))
		self.assertEqual(['cat', 'bat', 'tiger'], most_frequent_words(self.corpus, 3))

	def test_all_words(self):
		"""Make sure the function returns all the words if we tell it to return enough."""
		words = most_frequent_words(self.corpus, 5)
		self.assertIn('cat', words)
		self.assertIn('bat', words)
		self.assertIn('tiger', words)
		self.assertIn('whale', words)
		self.assertIn('dolphin', words)

	def test_more_words_than_total(self):
		"""Make sure the function doesn't break when we want more words than there are."""
		words = most_frequent_words(self.corpus, 7)
		self.assertIn('cat', words)
		self.assertIn('bat', words)
		self.assertIn('tiger', words)
		self.assertIn('whale', words)
		self.assertIn('dolphin', words)

	def test_edge_cases(self):
		"""Make sure the function errors on incorrect values, and works for oddly formatted corpora."""
		empty_corpus = ""
		self.assertRaises(ValueError, most_frequent_words, empty_corpus, 1)
		self.assertRaises(ValueError, most_frequent_words, empty_corpus, 100)
		self.assertRaises(ValueError, most_frequent_words, self.corpus, 0)

		one_word_corpus = "hello"
		self.assertEqual(['hello'], most_frequent_words(one_word_corpus, 1))
		self.assertEqual(['hello'], most_frequent_words(one_word_corpus, 10))

		odd_corpus = "hello hello   bees "
		self.assertEqual(['hello'], most_frequent_words(odd_corpus, 1))
		self.assertEqual(['hello', 'bees'], most_frequent_words(odd_corpus, 2))

if __name__ == '__main__':
	unittest.main()