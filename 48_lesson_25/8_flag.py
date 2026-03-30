"""
896. Monotonic Array
В этой задаче (уровень Easy) требуется определить,
является ли массив строго монотонным — то есть элементы
либо только не убывают, либо только не возрастают.
"""


def is_monotonic(nums: list[int]) -> bool:
    is_increasing = True
    is_decreasing = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            is_decreasing = False  # Нарушена монотонность убывания
        if nums[i] < nums[i - 1]:
            is_increasing = False  # Нарушена монотонность возрастания

    return is_increasing or is_decreasing


"""
2124. Check if All A's Appears Before All B's
В этой задаче на вход подается строка, состоящая только из символов a и b.
Нужно проверить, что все a стоят до всех b. """


def check_string_flag(s: str) -> bool:
    seen_b = False

    for char in s:
        if char == "b":
            seen_b = True
        elif char == "a" and seen_b:
            # Встретили 'a', хотя ранее уже был 'b'
            return False

    return True


def check_string(s: str) -> bool:
    for i in range(len(s) - 1):
        if s[i] == "b" and s[i + 1] == "a":
            return False

    return True


"""
125. Valid Palindrome
Нужно проверить, читается ли строка (очищенная от пробелов и знаков) 
одинаково слева направо и справа налево.
"""


# Решение с помощью флага
def is_palindrome_flag(s: str) -> bool:
    is_valid = True
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            is_valid = False
            break
        l += 1
        r -= 1

    return is_valid


# Решение с помощью двух указателей без флага
def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True
