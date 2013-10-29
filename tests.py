import unittest
from frequency import most_frequent_words

class FrequencyTestCase(unittest.TestCase):

	def test_core_functionality(self):
		corpus = "cat cat bat tiger cat whale dolphin bat"
		n = 1

		self.assertEqual(['cat'], most_frequent_words(corpus, n))

if __name__ == '__main__':
	unittest.main()