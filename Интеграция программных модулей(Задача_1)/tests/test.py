import unittest

# Поместим логику вашего кода в функцию для тестирования
def find_score_discrepancy(abiturients, attestat, postuplenie):
    raznica_05 = []
    raznica_1 = []
    raznica_2 = []

    for i in range(len(abiturients)):
        raznica = abs(attestat[i] - postuplenie[i])
        if raznica >= 0.5:
            raznica_05.append(abiturients[i])
        if raznica >= 1:
            raznica_1.append(abiturients[i])
        if raznica >= 2:
            raznica_2.append(abiturients[i])

    return raznica_05, raznica_1, raznica_2

class TestScoreDiscrepancy(unittest.TestCase):
    def setUp(self):
        self.abiturients = ["Анна", "Борис", "Вера", "Григорий", "Дарья", "Евгений", "Жанна", "Захар", "Ирина", "Кирилл", "Лариса", "Максим", "Надежда", "Олег", "Полина", "Роман", "Светлана", "Тимур", "Ульяна", "Федор"]
        self.attestat = [5.0, 4.9, 4.9, 4.6, 4.7, 4.4, 5.0, 4.3, 4.2, 4.1, 4.9, 4.8, 4.7, 4.0, 3.9, 4.4, 4.3, 4.2, 3.8, 5.0]
        self.postuplenie = [4.2, 4.3, 4.1, 4.2, 4.0, 3.1, 4.0, 3.8, 3.5, 4.0, 4.2, 4.1, 3.8, 3.7, 3.6, 3.5, 3.4, 3.3, 3.2, 3.0]

    def test_score_discrepancy(self):
        expected_raznica_05 = ['Анна', 'Борис', 'Вера', 'Дарья', 'Евгений', 'Жанна', 'Захар', 'Ирина', 'Лариса', 'Максим', 'Надежда', 'Роман', 'Светлана', 'Тимур','Ульяна','Федор']
        expected_raznica_1 = ['Евгений','Жанна','Федор']
        expected_raznica_2 = ['Федор']

        result_raznica_05, result_raznica_1, result_raznica_2 = find_score_discrepancy(self.abiturients, self.attestat, self.postuplenie)

        self.assertEqual(result_raznica_05, expected_raznica_05)
        self.assertEqual(result_raznica_1, expected_raznica_1)
        self.assertEqual(result_raznica_2, expected_raznica_2)

if __name__ == '__main__':
    unittest.main()

