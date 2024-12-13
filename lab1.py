# Шифр Цезаря для русского и английского алфавитов + пробел
ALPHABET = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя '
DEFAULT_SHIFT = 10

print('Шифр Цезаря (Алфfвиты: Ru + Eng)')
n = int(input('Выберите сдвиг (по умолчанию: 10): ') or DEFAULT_SHIFT)
input_text = input('Введите сообщение: ')

encrypted_text = ''
for symbol in input_text:
    num = ALPHABET.find(symbol)
    difference = num + n - len(ALPHABET)
    if n > 0 and difference >= 0:
        encrypted_text += ALPHABET[difference]
    elif n < 0 and difference < -len(ALPHABET):
        encrypted_text += ALPHABET[len(ALPHABET) + num + n]
    else:
        encrypted_text += ALPHABET[num + n]

print('\nИсходный текст: ' + input_text)
print('Сдвиг: ' + str(n) + '\n')
print('Зашифрованный текст: ' + encrypted_text + '\n')

decrypted_text = ''
for symbol in encrypted_text:
    num = ALPHABET.find(symbol)
    difference = num - n - len(ALPHABET)
    if -n > 0 and difference >= 0:
        decrypted_text += ALPHABET[difference]
    elif -n < 0 and difference < -len(ALPHABET):
        decrypted_text += ALPHABET[len(ALPHABET) + num - n]
    else:
        decrypted_text += ALPHABET[num - n]

print('Расшифрованный текст: ' + decrypted_text)
