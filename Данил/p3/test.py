import unittest

def distribute_boxes(boxes):
    m = []
    s = []
    b = []

    for box in boxes:
        volume = box['длина'] * box['ширина'] * box['высота']
        if volume < 100:
            m.append(box)
        elif 100 <= volume < 500:
            s.append(box)
        else:
            b.append(box)

    return m, s, b

class TestBoxDistribution(unittest.TestCase):

    def test_box_distribution(self):
        test_boxes = [
            {'длина': 1, 'ширина': 1, 'высота': 1, 'вес': 1},
            {'длина': 5, 'ширина': 5, 'высота': 5, 'вес': 10},
            {'длина': 100, 'ширина': 100, 'высота': 100, 'вес': 100}
            # Добавьте другие коробки по аналогии, если нужно
        ]

        expected_m = [{'длина': 1, 'ширина': 1, 'высота': 1, 'вес': 1}]
        expected_s = [{'длина': 5, 'ширина': 5, 'высота': 5, 'вес': 10}]
        expected_b = [{'длина': 100, 'ширина': 100, 'высота': 100, 'вес': 100}]

        result_m, result_s, result_b = distribute_boxes(test_boxes)

        self.assertEqual(result_m, expected_m)
        self.assertEqual(result_s, expected_s)
        self.assertEqual(result_b, expected_b)

if __name__ == '__main__':
    unittest.main()
