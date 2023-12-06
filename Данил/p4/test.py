import unittest
from io import StringIO
import sys

def calculate_sum_of_digits(number):
    s = int(number[0]) + int(number[1]) + int(number[2])
    return s % 2 == 0

class TestSumOfDigits(unittest.TestCase):
    
    def test_even_sum(self):
        test_input = "246"
        expected_output = "Сумма цифр числа 246 является четной.\n"

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            number = test_input
            s = calculate_sum_of_digits(number)
            if s:
                print(f"Сумма цифр числа {number} является четной.")
            else:
                print(f"Сумма цифр числа {number} является нечетной.")
            output = out.getvalue()
            self.assertEqual(output, expected_output)
        finally:
            sys.stdout = saved_stdout

    def test_odd_sum(self):
        test_input = "135"
        expected_output = "Сумма цифр числа 135 является нечетной.\n"

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            number = test_input
            s = calculate_sum_of_digits(number)
            if s:
                print(f"Сумма цифр числа {number} является четной.")
            else:
                print(f"Сумма цифр числа {number} является нечетной.")
            output = out.getvalue()
            self.assertEqual(output, expected_output)
        finally:
            sys.stdout = saved_stdout

    def test_invalid_input(self):
        test_input = "abc"
        expected_output = "Ошибка ввода. Пожалуйста, введите трехзначное число.\n"

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            number = test_input
            if len(number) != 3 or not number.isdigit():
                print("Ошибка ввода. Пожалуйста, введите трехзначное число.")
            output = out.getvalue()
            self.assertEqual(output, expected_output)
        finally:
            sys.stdout = saved_stdout

if __name__ == "__main__":
    unittest.main()
