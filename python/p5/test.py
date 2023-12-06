from io import StringIO
import sys
import unittest  # Добавлен импорт модуля unittest
from unittest.mock import patch

def create_table(size):
    table_output = StringIO()
    sys.stdout = table_output

    for row in range(1, size + 1):
        for col in range(1, size + 1):
            if row % 2 == 0:
                print(row, end='\t')
            else:
                print(col, end='\t')
        print()

    sys.stdout = sys.__stdout__
    return table_output.getvalue().strip()

class TestCreateTable(unittest.TestCase):
    def test_table_output(self):
        test_cases = [
            {
                "input": 3,
                "expected_output": "1\t2\t3\n1\t2\t3\n3\t3\t3"
            },
            {
                "input": 5,
                "expected_output": "1\t2\t3\t4\t5\n1\t2\t3\t4\t5\n3\t4\t5\t4\t5\n3\t4\t5\t4\t5\n5\t5\t5\t5\t5"
            },
            # Add more test cases as needed
        ]

        for test_case in test_cases:
            with patch('builtins.input', return_value=test_case['input']), patch('sys.stdout', new_callable=StringIO) as fake_output:
                create_table(test_case['input'])
                self.assertEqual(fake_output.getvalue().strip(), test_case['expected_output'])

if __name__ == "__main__":
    unittest.main()