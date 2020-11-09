import unittest
from parshuffle import *

class ShuffleTestCase(unittest.TestCase):

    def test_shuffle(self):
        # TODO: How to handle data in tests?
        with open('../data/paragraphs.txt', 'r') as file:
            X = read_index(file)
            Y = shuffle(X)

        self.assertEqual(set(X), set(Y))

if __name__ == '__main__':
    unittest.main()
