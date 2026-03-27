from typing import TypedDict

data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]},
]


class User(TypedDict):
    name: str
    scores: list[int]


def total_scores(data: list[User]) -> int:
    return sum(sum(user["scores"]) for user in data)


result = total_scores(data)
print(f"Итоговый балл: {result}")
