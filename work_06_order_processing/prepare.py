import dill

# Отложенное вычисление: map создаёт итератор, а total извлекается при запросе элемента.
Temeshova_order_totals = lambda orders: map(lambda order: order["total"], orders)


class OptionalBox(tuple):
    # Неизменяемый кортеж с одним элементом: значением или None.
    __slots__ = ()

    # Создаёт кортеж (value,); запятая обозначает один элемент.
    __new__ = lambda cls, value: tuple.__new__(cls, (value,))

    # Применяет function к значению и возвращает новую коробку; None пропускает.
    map = lambda self, function: OptionalBox(
        function(self[0]) if self[0] is not None else None
    )


# Внутри map: filter ищет по id, next берёт первый заказ или None.
# [0] извлекает первый элемент кортежа.
Temeshova_find_order = lambda orders, order_id: OptionalBox(orders).map(
    lambda items: next(filter(lambda order: order["id"] == order_id, items), None)
)[0]

# Проверяет, что map с lambda x: x сохраняет исходное значение.
Temeshova_identity_law = lambda value: (
    OptionalBox(value).map(lambda x: x)[0] == OptionalBox(value)[0]
)

# Проверяет равенство: два map (+10, затем *2) и один map с обеими операциями.
Temeshova_composition_law = lambda value: (
    OptionalBox(value).map(lambda x: x + 10).map(lambda x: x * 2)[0]
    == OptionalBox(value).map(lambda x: (x + 10) * 2)[0]
)


# Сохраняет функции и класс в двоичный файл рядом с программой.
# stream — параметр для открытого файла, отдельной переменной с данными нет.
if __name__ == "__main__":
    (lambda stream: (
        dill.dump((Temeshova_order_totals, OptionalBox, Temeshova_find_order, Temeshova_identity_law, Temeshova_composition_law), stream, recurse=True),
        stream.close(),
    ))(open(__file__.replace("prepare.py", "orders.bin"), "wb"))
