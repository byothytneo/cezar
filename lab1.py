ALPHABET = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя '
DEFAULT_SHIFT = 10

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

def crack_caesar_cipher(encrypted_text):
    print("\nПопытки расшифровки с использованием всех возможных сдвигов:")
    for shift in range(-len(ALPHABET), len(ALPHABET)):
        decrypted_text = decrypt_text(encrypted_text, shift)
        print(f"Сдвиг {shift}: {decrypted_text}")

def main():
    print('Шифр Цезаря (Алфавиты: Ru + Eng)')

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
