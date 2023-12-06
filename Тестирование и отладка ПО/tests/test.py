import unittest
from io import StringIO
from unittest.mock import patch

def function_Y(X):
    return X**2 - 4*X + 4

def iterate_function(X0, h, characteristic_point):
    result = []
    X = X0
    Y = function_Y(X)

    while Y >= characteristic_point:
        result.append((X, Y))
        X += h
        Y = function_Y(X)

    return result

class TestIterateFunction(unittest.TestCase):
    def test_iterate_function(self):
        test_input = [
            (0, 1, -1),   # Test Case 1
            (1, 0.5, 10), # Test Case 2
            (-3, 0.1, -20) # Test Case 3
        ]
        expected_output = [
            [(0, 4), (1, 1), (2, 0)], # Test Case 1
            [(1, 1), (1.5, 0.25), (2, 0)], # Test Case 2
            [(-3, 25), (-2.9, 22.41), (-2.8, 20.84)] # Test Case 3
        ]

        for i, test in enumerate(test_input):
            X0, h, characteristic_point = test
            expected = expected_output[i]

            with patch('builtins.input', side_effect=[str(X0), str(h), str(characteristic_point)]):
                captured_output = StringIO()
                with patch('sys.stdout', captured_output):
                    iterate_function(X0, h, characteristic_point)

                output = captured_output.getvalue().splitlines()
                output_values = [tuple(map(float, line.split('= ')[1].split(', Y = '))) for line in output]

                self.assertEqual(output_values, expected)

if __name__ == '__main__':
    unittest.main()
