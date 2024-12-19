ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
DEFAULT_SHIFT = 10
FREQUENCY_ORDER = 'оаеинтсрвлкмдпуяыьгзбчйхжюшцщэфё '

# Предполагаемые частоты русских букв в процентах (исходя из обычного текста)
EXPECTED_FREQUENCY = {
    'о': 0.090, 'а': 0.080, 'е': 0.072, 'и': 0.062, 'н': 0.053,
    'т': 0.053, 'с': 0.045, 'р': 0.040, 'в': 0.038, 'л': 0.035,
    'к': 0.028, 'м': 0.026, 'д': 0.025, 'п': 0.023, 'у': 0.021,
    'я': 0.018, 'ы': 0.016, 'ь': 0.014, 'г': 0.013, 'з': 0.011,
    'б': 0.010, 'ч': 0.009, 'й': 0.008, 'х': 0.007, 'ж': 0.007,
    'ю': 0.006, 'ш': 0.006, 'ц': 0.004, 'щ': 0.003, 'э': 0.003,
    'ф': 0.002, 'ё': 0.001
}

def encrypt_text(input_text, shift):
    encrypted_text = ''
    for symbol in input_text:
        num = ALPHABET.find(symbol)
        if num == -1:
            encrypted_text += symbol
            continue
            
        new_position = (num + shift) % len(ALPHABET)
        encrypted_text += ALPHABET[new_position]
    
    return encrypted_text

def decrypt_text(encrypted_text, shift):
    decrypted_text = ''
    for symbol in encrypted_text:
        num = ALPHABET.find(symbol)
        if num == -1:
            decrypted_text += symbol
            continue
            
        new_position = (num - shift) % len(ALPHABET)
        decrypted_text += ALPHABET[new_position]
    
    return decrypted_text

def frequency_analysis(text):
    frequency_dict = {}
    total_chars = 0
    for symbol in text:
        if symbol in ALPHABET:
            total_chars += 1
            if symbol in frequency_dict:
                frequency_dict[symbol] += 1
            else:
                frequency_dict[symbol] = 1
    
    for symbol in frequency_dict:
        frequency_dict[symbol] /= total_chars
    
    return frequency_dict

def score_text(text):
    frequency_dict = frequency_analysis(text)
    score = 0
    for char in EXPECTED_FREQUENCY:
        if char in frequency_dict:
            score += abs(frequency_dict[char] - EXPECTED_FREQUENCY[char])
        else:
            score += EXPECTED_FREQUENCY[char]
    return score

def crack_caesar_cipher(encrypted_text):
    best_shift = 0
    best_score = float('inf')
    
    for shift in range(len(ALPHABET)):
        decrypted_text = decrypt_text(encrypted_text, shift)
        score = score_text(decrypted_text)
        if score < best_score:
            best_score = score
            best_shift = shift
            
    decrypted_text = decrypt_text(encrypted_text, best_shift)
    print(f"\nЛучший сдвиг: {best_shift}\nРасшифрованный текст: {decrypted_text}")

def main():
    print('Шифр Цезаря')

    action = input("Выберите действие:\n1 - Зашифровать\n2 - Дешифровать\n3 - Взломать\nВведите номер действия: ")
    
    if action not in ['1', '2', '3']:
        print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")
        return

    if action == '1':
        n = int(input('Выберите сдвиг (по умолчанию: 10): ') or DEFAULT_SHIFT)
        input_text = input('Введите сообщение для шифрования: ')
        encrypted_text = encrypt_text(input_text, n)
        print('\nИсходный текст: ' + input_text)
        print('Сдвиг: ' + str(n) + '\n')
        print('Зашифрованный текст: ' + encrypted_text + '\n')

    elif action == '2':
        n = int(input('Выберите сдвиг (по умолчанию: 10): ') or DEFAULT_SHIFT)
        input_text = input('Введите сообщение для расшифровки: ')
        decrypted_text = decrypt_text(input_text, n)
        print('\nИсходный текст: ' + input_text)
        print('Сдвиг: ' + str(n) + '\n')
        print('Расшифрованный текст: ' + decrypted_text)

    elif action == '3':
        input_text = input('Введите зашифрованное сообщение для взлома: ')
        crack_caesar_cipher(input_text)

if __name__ == "__main__":
    main()
