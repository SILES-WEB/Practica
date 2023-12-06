import unittest

def find_min_max_passengers(routes):
    min_passengers = [float('inf')] * len(routes)
    max_passengers = [float('-inf')] * len(routes)

    for city in range(len(routes)):
        for route in range(len(routes[city])):
            passengers = routes[city][route]
            if passengers < min_passengers[city]:
                min_passengers[city] = passengers
            if passengers > max_passengers[city]:
                max_passengers[city] = passengers

    return min_passengers, max_passengers

class TestFindMinMaxPassengers(unittest.TestCase):
    def test_find_min_max_passengers(self):
        routes = [
            [10, 20, 15],  # Город 1
            [25, 18, 30],  # Город 2
            [12, 22, 17]   # Город 3
        ]

        min_expected = [10, 18, 12]
        max_expected = [20, 30, 22]

        min_passengers, max_passengers = find_min_max_passengers(routes)

        self.assertEqual(min_passengers, min_expected)
        self.assertEqual(max_passengers, max_expected)

if __name__ == '__main__':
    unittest.main()
