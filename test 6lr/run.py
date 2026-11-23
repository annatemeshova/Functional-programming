import dill

# Получает восстановленные функции и класс и выполняет примеры.
Temeshova_run = lambda Temeshova_order_totals, OptionalBox, Temeshova_find_order, Temeshova_identity_law, Temeshova_composition_law: (
    print(
        "Суммы заказов:",
        # tuple считывает итератор целиком: здесь извлекаются суммы для вывода.
        tuple(Temeshova_order_totals((
            {"id": 1, "total": 1500, "status": "new"},
            {"id": 2, "total": 2300, "status": "paid"},
            {"id": 3, "total": 0, "status": "cancelled"},
        ))),
    ),
    print("Преобразование значения:", OptionalBox(100).map(lambda x: x * 2)[0]),
    print("Преобразование None:", OptionalBox(None).map(lambda x: x * 2)[0]),
    print(
        "Найденный заказ:",
        Temeshova_find_order((
            {"id": 1, "total": 1500, "status": "new"},
            {"id": 2, "total": 2300, "status": "paid"},
        ), 2),
    ),
    print(
        "Отсутствующий заказ:",
        Temeshova_find_order(({"id": 1, "total": 1500, "status": "new"},), 99),
    ),
    print("Закон тождества:", Temeshova_identity_law(5)),
    print("Закон тождества для None:", Temeshova_identity_law(None)),
    print("Закон композиции:", Temeshova_composition_law(5)),
    print("Закон композиции для None:", Temeshova_composition_law(None))
)

# При прямом запуске читает файл и передаёт сохранённые объекты через *.
if __name__ == "__main__":
    (lambda stream: (
        Temeshova_run(*dill.load(stream)),
        stream.close(),
    ))(open(__file__.replace("run.py", "orders.bin"), "rb"))
