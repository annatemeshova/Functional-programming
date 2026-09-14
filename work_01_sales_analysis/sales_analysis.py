# Разбирает строку CSV в список словарей.
Temeshova_parse_csv = lambda temeshova_data: [] if not temeshova_data.strip() else list(
    map(
        lambda temeshova_line: dict(
            zip(
                temeshova_data.splitlines()[0].split(","),
                temeshova_line.split(","),
            )
        ),
        filter(
            lambda temeshova_line: temeshova_line.strip(),
            temeshova_data.splitlines()[1:],
        ),
    )
)
# Считает общую выручку.
Temeshova_compute_revenue = lambda temeshova_rows: sum(
    map(
        lambda temeshova_row: float(temeshova_row["quantity"])
        * float(temeshova_row["price"]),
        temeshova_rows,
    ),
    0.0,
)
# Находит строку с максимальной выручкой.
Temeshova_top_item = lambda temeshova_rows: max(
    temeshova_rows,
    key=lambda temeshova_row: float(temeshova_row["quantity"])
    * float(temeshova_row["price"]),
) if temeshova_rows else None
