from functools import reduce
# Преобразует студентов в строки с именем и оценкой.
Temeshova_format_students = lambda students: list(
    map(lambda student: (f'Имя: {student["name"]}, Оценка: {student["grade"]}'),students,)
)
# Оставляет студентов с оценкой строго выше 4.0.
Temeshova_filter_high_grade = lambda students: list(
    filter(lambda student: student["grade"] > 4.0, students)
)
# Вычисляет средний возраст переданных студентов с помощью reduce.
Temeshova_average_age = lambda students: (
    reduce(lambda total_age, student: total_age + student["age"],students,0,)/ len(students)
    if students
    else 0.0
)

print(
    "Строки с именами и оценками:",
    Temeshova_format_students(
        [
            {"name": "Анна", "age": 20, "grade": 4.5},
            {"name": "Борис", "age": 22, "grade": 3.8},
            {"name": "Виктор", "age": 19, "grade": 4.2},
            {"name": "Галина", "age": 21, "grade": 4.9},
            {"name": "Дмитрий", "age": 23, "grade": 3.5},
        ]
    ),
)
print(
    "Студенты с оценкой выше 4.0:",
    Temeshova_filter_high_grade(
        [
            {"name": "Анна", "age": 20, "grade": 4.5},
            {"name": "Борис", "age": 22, "grade": 3.8},
            {"name": "Виктор", "age": 19, "grade": 4.2},
            {"name": "Галина", "age": 21, "grade": 4.9},
            {"name": "Дмитрий", "age": 23, "grade": 3.5},
        ]
    ),
)
print(
    "Средний возраст отобранных студентов:",
    Temeshova_average_age(
        Temeshova_filter_high_grade(
            [
                {"name": "Анна", "age": 20, "grade": 4.5},
                {"name": "Борис", "age": 22, "grade": 3.8},
                {"name": "Виктор", "age": 19, "grade": 4.2},
                {"name": "Галина", "age": 21, "grade": 4.9},
                {"name": "Дмитрий", "age": 23, "grade": 3.5},
            ]
        )
    ),
)
