def ceasar_encode(shift, line):  # текст в линию
 
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
 
text = open('1.txt', 'r', encoding='utf-8').read().split() # для разделения по пробелам можно просто СПЛИТ
out = open('cipher_text.txt', 'a', encoding='utf-8')
 
ave_text = [line_from_text for line_from_text in text if line_from_text] # поправил плохой пример нэйминга
for shift, line_from_file in enumerate(ave_text, 1):
    out.write(ceasar_encode(shift, line_from_file) + '\n')
out.close()