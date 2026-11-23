def Temeshova_recursive_sum(x):
    "Возвращает сумму элементов списка, не изменяя исходный список."
    if not x:
        return 0

    return x[0] + Temeshova_recursive_sum(x[1:])


print("Сумма [1, 2, 3, 4, 5]:", Temeshova_recursive_sum([1, 2, 3, 4, 5]))
print("Сумма пустого списка:", Temeshova_recursive_sum([]))
print("Сумма квадратов [1, 2, 3, 4, 5]:", Temeshova_recursive_sum(list(map(lambda x: x * x, [1, 2, 3, 4, 5]))))
