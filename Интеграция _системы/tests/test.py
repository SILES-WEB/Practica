import unittest

def sort_rows_ascending(matrix):
    for row in matrix:
        row.sort()

class TestSortRowsAscending(unittest.TestCase):
    def test_sort_rows(self):
        # Исходные данные
        matrix = [
            [4, 2, 7, 1],
            [9, 5, 3, 8],
            [6, 0, 2, 3]
        ]

        # Ожидаемый результат после сортировки
        expected_result = [
            [1, 2, 4, 7],
            [3, 5, 8, 9],
            [0, 2, 3, 6]
        ]

        # Вызываем функцию для сортировки строк
        sort_rows_ascending(matrix)

        # Проверяем, совпадает ли результат с ожидаемым результатом
        self.assertEqual(matrix, expected_result)

if __name__ == '__main__':
    unittest.main()
