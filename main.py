import art
from collections import defaultdict
import matplotlib.pyplot as plt

print(art.text2art('shnyri_team'))

from collections import defaultdict
import matplotlib.pyplot as plt

def load_text(filename):
    """
    Загружает текст из файла и возвращает его в виде строки.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def analyze_text_symbols(text, keylout_dd):
    """
    Подсчитывает количество нажатий для каждого символа на основе текста и раскладки клавиатуры.
    Возвращает словарь, где ключи — символы, а значения — количество нажатий.
    """
    symbol_counts = defaultdict(int)

    # Создание множества всех символов из раскладки для быстрого поиска
    all_keys = set(key for groups in keylout_dd.values() for group in groups for key in group)

    # Пройтись по каждому символу текста и обновить счетчики
    for char in text:
        if char in all_keys:
            symbol_counts[char] += 1

    return symbol_counts



def main():
    # Определяем раскладку клавиатуры
    keylout_dd = {
        'lfi5': [('ё', 'TAB', 'Caps Lock', 'Shift', '1', 'й', 'ф', 'я'),
                 ('$', 'TAB', 'ESC', 'SHIFT', 'Super', '%', 'б', 'ч', 'ш')],
        'lfi4': [('2', 'ц', 'ы', 'ч'), ('7', 'ы', 'и', 'х')],
        'lfi3': [('3', 'у', 'в', 'с'), ('5', 'о', 'е', 'й')],
        'lfi2': [('4', 'к', 'а', 'м', '5', 'е', 'п', 'и'), ('3', '1', 'у', 'а', 'к', 'ь', ',', '_')],
        'lfi1': [('SPACE')],
        'rfi2': [('6', 'н', 'р', 'т', '7', 'г', 'о', 'ь'), ('9', 'ё', '.', '/', '0', '^', 'н', 'р')],
        'rfi3': [('8', 'ш', 'л', 'б'), ('2', 'д', 'т', 'м')],
        'rfi4': [('9', 'щ', 'д', 'ю'), ('4', 'я', 'с', 'ф')],
        'rfi5': [('0', 'з', 'ж', '?', '-', 'х', 'э', '=', 'BACKSPACE', 'ъ', '\\', 'Enter', 'Shift'),
                 ('6', 'г', 'в', 'п', '8', 'ж', 'з', 'щ', 'BACKSPACE', 'ц', 'ъ', 'Enter', 'Shift')]
    }

    # Загрузим текст из файла
    text = load_text("/content/voina-i-mir.txt")

    # Анализируем текст
    result = analyze_text_symbols(text, keylout_dd)

    # Выводим результаты
    for symbol, count in result.items():
        print(f"'{symbol}': {count} нажатий")


if __name__ == "__main__":
    main()
