import art
from collections import defaultdict
import matplotlib.pyplot as plt
import analyze_text_symbols
import plot_symbol_frequencies
import keyboard
import load_text

def main():

    # Загрузим текст из файла
    text = load_text("/home/true_jatu/keyboard_vizov/voina-i-mir.txt")

    # Анализируем текст
    result = analyze_text_symbols(text, keyboard.keylout_dd)

        # Выводим результаты
    for symbol, count in result.items():
        print(f"'{symbol}': {count} нажатий")

    # Построение графика частот символов
    plot_symbol_frequencies(result)

if __name__ == "__main__":
    main()
