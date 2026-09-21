def Temeshova_split_words(text: str) -> list[str]:
    "Возвращает слова в нижнем регистре, считая пунктуацию разделителем."
    return "".join(map(lambda symbol: symbol if symbol.isalnum() else " ", text.lower())).split()


def Temeshova_count_word_frequencies(words: list[str]) -> dict[str, int]:
    "Возвращает частоты слов, не изменяя исходный список."
    return dict(zip(words, map(words.count, words)))


def Temeshova_top_word(freq: dict[str, int]):
    "Возвращает самое частое слово или None для пустого словаря."
    return max(freq, key=freq.__getitem__) if freq else None
