import unittest
from io import StringIO
import sys

def display_participants_info(participants):
    output = StringIO()
    sys.stdout = output

    print('Участники соревнований:')
    for elem in participants:
        print(elem['ФИО'], ' - ', elem['баллы'])

    winner_list = sorted(participants, key=lambda x: x['баллы'], reverse=True)[:3]
    print('\nТройка победителей:')
    for elem in winner_list:
        print(elem['ФИО'], ' - ', elem['баллы'])

    return output.getvalue()

class TestParticipantsInfo(unittest.TestCase):

    def test_display_participants_info(self):
        test_input = [
            {'ФИО': 'Алексей Иванович Боярышников', 'баллы': 100},
            {'ФИО': 'Иван Александрович Малых', 'баллы': 20},
            {'ФИО': 'Петр Борисович Третьяков', 'баллы': 40},
        ]

        expected_output = "Участники соревнований:\n" \
                          "Алексей Иванович Боярышников  -  100\n" \
                          "Иван Александрович Малых  -  20\n" \
                          "Петр Борисович Третьяков  -  40\n" \
                          "\nТройка победителей:\n" \
                          "Алексей Иванович Боярышников  -  100\n" \
                          "Петр Борисович Третьяков  -  40\n" \
                          "Иван Александрович Малых  -  20\n"

        result = display_participants_info(test_input)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
