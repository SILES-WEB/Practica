import unittest
from io import StringIO
import sys

def ceasar_encode(shift, line):
    result = ''
    for letter in line:
        if letter.isalpha():
            number = ord(letter) + shift % 32
            if number > 1103:
                number -= 32
            result += chr(number)
        else:
            result += letter
    return result

def process_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def encode_text_and_save(file_path):
    lines = process_text_file(file_path)
    with open('cipher_text.txt', 'a', encoding='utf-8') as out:
        for shift, line in enumerate(lines, 1):
            encoded_line = ceasar_encode(shift, line)
            out.write(encoded_line + '\n')

class TestCeasarEncode(unittest.TestCase):

    def setUp(self):
        self.test_input = [
            "This is a test message.",
            "Another line of text.",
            "And one more line!"
        ]
        with open('test_input.txt', 'w', encoding='utf-8') as file:
            for line in self.test_input:
                file.write(line + '\n')

    def tearDown(self):
        pass

    def test_ceasar_encode(self):
        expected_output = [
            "Uijt jt b uftu nfttbhf.",
            "Bopuifs mjof pg ufyu.",
            "Boe pof npsf mjof!"
        ]
        encode_text_and_save('test_input.txt')

        with open('cipher_text.txt', 'r', encoding='utf-8') as file:
            actual_output = [line.strip() for line in file.readlines()]

        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
