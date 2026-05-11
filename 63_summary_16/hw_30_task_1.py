"""
Комбинации одежды
Напишите функцию, которая принимает списки типов одежды,
цветов и размеров, а затем генерирует все возможные
комбинации в формате "Clothe - Color - Size".

Данные:
    clothes = ["T-shirt", "Jeans", "Jacket"]
    colors = ["Red", "Blue", "Black"]
    sizes = ["S", "M", "L"]
    Пример вывода:
    T-shirt - Red - S
    T-shirt - Red - M
    T-shirt - Red - L
    T-shirt - Blue - S
    ...
    Jacket - Black - L

"""

# Вариант 1
# def generate_combinations(clothes, colors, sizes):
#     for cloth in clothes:
#         for color in colors:
#             for size in sizes:
#                 yield f"{cloth} - {color} - {size}"


# clothes = ["T-shirt", "Jeans", "Jacket"]
# colors = ["Red", "Blue", "Black"]
# sizes = ["S", "M", "L"]

# for combo in generate_combinations(clothes, colors, sizes):
#     print(combo)


def generate_combinations(lists, index=0, current=None):
    if current is None:
        current = []

    if index == len(lists):
        yield " - ".join(current)
        return

    for item in lists[index]:
        current.append(item)
        yield from generate_combinations(lists, index + 1, current)
        current.pop()



clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

test = generate_combinations([clothes, colors, sizes])
# print(test.__next__())
# print(test.__next__())
# print(test.__next__())

for combo in generate_combinations([clothes, colors, sizes]):
    print(combo)


# index=0, current=[]
# ├─ "T-shirt"
# │  ├─ index=1, current=["T-shirt"]
# │  │  ├─ "Red"
# │  │  │  ├─ index=2, current=["T-shirt", "Red"]
# │  │  │  │  ├─ "S" → current=["T-shirt","Red","S"] → YIELD!
# │  │  │  │  ├─ "M" → current=["T-shirt","Red","M"] → YIELD!
# │  │  │  │  └─ "L" → current=["T-shirt","Red","L"] → YIELD!
# │  │  ├─ "Blue"
# │  │  │  ├─ index=2, current=["T-shirt", "Blue"]
# │  │  │  │  ├─ "S" → current=["T-shirt","Blue","S"] → YIELD!
# │  │  │  │  ├─ "M" → current=["T-shirt","Blue","M"] → YIELD!
# │  │  │  │  └─ "L" → current=["T-shirt","Blue","L"] → YIELD!
# │  │  └─ "Black"
# │  │     ├─ index=2, current=["T-shirt", "Black"]
# │  │     │  ├─ "S" → current=["T-shirt","Black","S"] → YIELD!
# │  │     │  ├─ "M" → current=["T-shirt","Black","M"] → YIELD!
# │  │     │  └─ "L" → current=["T-shirt","Black","L"] → YIELD!
# ├─ "Jeans"
# │  ├─ "Red"
# │  │  ├─ "S", "M", "L" → 3 комбинации
# │  ├─ "Blue"
# │  │  └─ "S", "M", "L" → 3 комбинации
# │  └─ "Black"
# │     └─ "S", "M", "L" → 3 комбинации
# └─ "Jacket"
#    ├─ "Red"
#    │  └─ "S", "M", "L" → 3 комбинации
#    ├─ "Blue"
#    │  └─ "S", "M", "L" → 3 комбинации
#    └─ "Black"
#       └─ "S", "M", "L" → 3 комбинации