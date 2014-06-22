from mergesort import mergeSort
import random
import unittest

class mergeSortTest(unittest.TestCase):
  def setUp(self):
    self.numbers = range(100)

  def test_mergeSort(self):
    random.shuffle(self.numbers)
    self.assertEqual(mergeSort(self.numbers), range(len(self.numbers)))

if __name__ == '__main__':
    unittest.main()
