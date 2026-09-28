from dataclasses import dataclass
from enum import Enum
from typing import Generic, TypeVar, Union

TemeshovaT = TypeVar("TemeshovaT")
TemeshovaE = TypeVar("TemeshovaE")

class TemeshovaLoadState(Enum):
    "Состояние асинхронной загрузки данных."

    LOADING = "loading"
    SUCCESS = "success"
    ERROR = "error"

@dataclass(frozen=True)
class TemeshovaUser:
    "Неизменяемые данные пользователя."

    name: str
    age: int
    email: str

@dataclass(frozen=True)
class TemeshovaSuccess(Generic[TemeshovaT]):
    "Успешный результат со значением."

    value: TemeshovaT

@dataclass(frozen=True)
class TemeshovaFailure(Generic[TemeshovaE]):
    "Неуспешный результат с описанием ошибки."

    error: TemeshovaE

TemeshovaResult = Union[
    TemeshovaSuccess[TemeshovaT],
    TemeshovaFailure[TemeshovaE],
]

def Temeshova_users_result(
    users: list[TemeshovaUser],
) -> TemeshovaResult[list[TemeshovaUser], str]:
    "Возвращает пользователей или сообщение об ошибке для пустого списка."
    return TemeshovaSuccess(users) if users else TemeshovaFailure("Список пользователей пуст")

def Temeshova_load_users() -> TemeshovaResult[list[TemeshovaUser], str]:
    "Загружает демонстрационный список пользователей."
    return Temeshova_users_result(
        [
            TemeshovaUser("Анна", 20, "anna@example.com"),
            TemeshovaUser("Иван", 24, "ivan@example.com"),
        ]
    )

print("Проверка заполненного списка:", Temeshova_load_users())
print("Проверка пустого списка:", Temeshova_users_result([]))

print("===============")
print("LOADING =", TemeshovaLoadState.LOADING.value)
print("SUCCESS =", TemeshovaLoadState.SUCCESS.value)
print("ERROR =", TemeshovaLoadState.ERROR.value)
print("Количество состояний LoadState:", len(TemeshovaLoadState))
print("Мощность Result[list[User], str]: счётно бесконечна")
