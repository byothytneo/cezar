# Шифр Цезаря для русского алфавита + пробел

Шифр Цезаря - это тип подстановочного шифра, в котором каждая буква в исходном тексте смещается на определенное количество позиций по алфавиту. В данной реализации используется русский, включая пробел.

## Как он работает?

- **Определение алфавита**: В коде используется строка, содержащая символы русского алфавита, а также пробел.
- **Сдвиг по умолчанию**: По умолчанию используется значение сдвига 10, если пользователь не укажет другое значение.
- **Шифрование**: Каждый символ входного текста сдвигается на указанное количество позиций.
- **Дешифрование**: Зашифрованный текст затем сдвигается обратно на исходное количество позиций для восстановления оригинального текста.
- **Взлом**: : Для взлома шифра Цезаря можно использовать метод частотного анализа. Этот метод основывается на сравнении частот появления символов в зашифрованном тексте с частотами символов в обычном тексте.

# Примеры для тестирования

## Пример 1: Зашифровка
Шифр Цезаря
Выберите действие:
1 - Зашифровать
2 - Дешифровать
3 - Взломать
Введите номер действия: 1
Выберите сдвиг (по умолчанию: 10):
Введите сообщение для шифрования: привет

Исходный текст: привет
Сдвиг: 10

Зашифрованный текст: щътлоь

## Пример 2: Дешифровка
**Входные данные:**
- Введите номер действия: `2`
- Выберите сдвиг (по умолчанию: 10):` `
- Введите сообщение для расшифровки: `щътлоь`

**Ожидаемый результат:**
- Исходный текст: `щътлоь`
- Сдвиг: `10`
- Расшифрованный текст: `привет`

## Пример 3: Взлом
**Входные данные:**
- Введите номер действия: `3`
- Введите зашифрованное сообщение для взлома: `щътлоь`
  
**Ожидаемый результат:**
- Лучший сдвиг: `10`
- Расшифрованный текст: `привет`

## Пример 4: Взлом
**Входные данные:**
- Введите номер действия: `3`
- Введите зашифрованное сообщение для взлома: `оыюьмыкйжотджймчыюгжйзьнчыудплысагьлъ`
  
**Ожидаемый результат:**
- Лучший сдвиг: `29`
- Расшифрованный текст: `у вас получилось взломать шифр цезаря`

