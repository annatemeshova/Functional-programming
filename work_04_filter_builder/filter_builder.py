from functools import partial

# Возвращает каррированный фильтр по ключу и значению.
Temeshova_filter_by = lambda key: lambda value: lambda items: list(
    filter(lambda item: item[key] == value, items)
)

# Фиксирует ключ category с помощью partial.
Temeshova_filter_by_category = partial(
    lambda filter_function, value: filter_function("category")(value),
    Temeshova_filter_by,
)

# Возвращает предикат сравнения с заданной границей.
Temeshova_greater_than = lambda threshold: lambda x: x > threshold

# Применяет каррированный предикат вместе с filter.
Temeshova_filter_greater_than = lambda threshold: lambda items: list(
    filter(Temeshova_greater_than(threshold), items)
)

print(
    "Фильтр по ключу category, значение fruit:",
    Temeshova_filter_by("category")("fruit")(
        [
            {"name": "apple", "category": "fruit"},
            {"name": "carrot", "category": "vegetable"},
            {"name": "banana", "category": "fruit"},
        ]
    ),
)
print(
    "Фильтр по категории vegetable через partial:",
    Temeshova_filter_by_category("vegetable")(
        [
            {"name": "apple", "category": "fruit"},
            {"name": "carrot", "category": "vegetable"},
            {"name": "banana", "category": "fruit"},
        ]
    ),
)
print("Число 6 больше 5:", Temeshova_greater_than(5)(6))
print("Число 5 больше 5:", Temeshova_greater_than(5)(5))
print("Число 2 больше 5:", Temeshova_greater_than(5)(2))
print(
    "Числа больше 5:",
    Temeshova_filter_greater_than(5)([1, 6, 8, 2, 9]),
)
