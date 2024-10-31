import matplotlib.pyplot as plt
def plot_symbol_frequencies(symbol_counts):
    """
    Строит график частот символов на основе данных из symbol_counts.
    """
    symbols = list(symbol_counts.keys())
    frequencies = list(symbol_counts.values())

    # Построение графика
    plt.figure(figsize=(12, 6))
    plt.bar(symbols, frequencies, color='skyblue')
    plt.xlabel("Символы")
    plt.ylabel("Частота")
    plt.title("Частота использования символов")
    plt.xticks(rotation=90)
    plt.show()
