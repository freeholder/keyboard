from collections import defaultdict

def analyze_finger_loads(text, keylout_dd, keylout_shift):
    """
    Подсчитывает нагрузку на каждый палец на основе текста и раскладок клавиатуры.
    Возвращает два словаря, где ключи — пальцы, а значения — суммарное количество нажатий.
    """
    finger_loads_ycu = defaultdict(int)  # Для ЙЦУКЕН
    finger_loads_vyzov = defaultdict(int)  # Для ВЫЗОВ

    # Объединение символов с их частотами
    symbol_counts = analyze_text_symbols(text, keylout_dd, keylout_shift)
    
    # Распределение символов по пальцам для обеих раскладок
    for finger, layouts in keylout_dd.items():
        # Если для пальца есть только одна раскладка, то добавляем пустую раскладку для второй
        if len(layouts) == 1:
            symbols_ycu = layouts[0]
            symbols_vyzov = []
        else:
            symbols_ycu, symbols_vyzov = layouts
        
        # Считаем частоты для каждой раскладки
        for symbol in symbols_ycu:
            finger_loads_ycu[finger] += symbol_counts.get(symbol, 0)
        for symbol in symbols_vyzov:
            finger_loads_vyzov[finger] += symbol_counts.get(symbol, 0)

    return finger_loads_ycu, finger_loads_vyzov


def analyze_text_symbols(text, keylout_dd, keylout_shift):
    """
    Подсчитывает количество нажатий для каждого символа на основе текста и раскладок клавиатуры.
    Возвращает словарь, где ключи — символы, а значения — количество нажатий.
    """
    symbol_counts = defaultdict(int)

    # Создание множества всех символов из раскладки для быстрого поиска
    all_keys = set(key for groups in keylout_dd.values() for group in groups for key in group)
    shift_keys = set(key for groups in keylout_shift.values() for group in groups for key in group)

    # Пройтись по каждому символу текста и обновить счетчики
    for char in text:
        if char in all_keys or char in shift_keys:
            symbol_counts[char] += 1

    return symbol_counts
