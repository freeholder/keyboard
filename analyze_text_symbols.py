from collections import defaultdict

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
