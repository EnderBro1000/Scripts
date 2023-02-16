import unittest
from word_matrix import WordMatrix


class MyTestCase(unittest.TestCase):

    def has_spaces(self):
        for element in self.matrix:
            if element == "":
                return True
        return False

    def test_randomize_matrix(self):
        matrix = WordMatrix(5, 5)
        matrix.randomize_matrix()
        self.assertFalse(matrix.has_spaces())  # add assertion here


if __name__ == '__main__':
    unittest.main()
