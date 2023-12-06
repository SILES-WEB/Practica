def replace_diagonals(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i][i] = 1  # Главная диагональ
        matrix[i][n - 1 - i] = 1  # Побочная диагональ
    return matrix

import unittest

class TestMatrixDiagonalReplacement(unittest.TestCase):

    def test_replace_diagonals(self):
        test_matrix = [
            [1, 2, 3],
            [2, 4, 6],
            [3, 6, 9]
        ]
        expected_result = [
            [1, 2, 1],
            [2, 1, 6],
            [1, 6, 1]
        ]
        
        result = replace_diagonals(test_matrix)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
