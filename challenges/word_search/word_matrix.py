import numpy as np
import random

class WordMatrix:

    def __init__(self, rows, columns):
        """"""
        self.matrix = np.zeros((rows, columns), dtype=str)
        # self.matrix.size = (rows, columns)
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print(self.matrix)


    def randomize_matrix(self):
        """Fills blank spaces in matrix with random characters from alphabet."""

        for element in self.matrix:
            element = random.choice(self.alphabet)


if __name__ == "__main__":
    test_matrix = 0