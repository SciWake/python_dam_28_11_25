"""
Напишите рекурсивную функцию, которая выводит строку в обратном порядке.
Данные
text = "hello"
Пример вывода
olleh
"""


def reverse_string(text: str, index: int = 0) -> str:
    if index == len(text):
        return ""

    return reverse_string(text, index + 1) + text[index]


text = "hello"
print(reverse_string(text))

    return reverse_string("hello", 0 + 1) + text[0] -> "" + "o" + "l" + "l" + "e" + "h"
        return reverse_string("hello", 1 + 1) + text[1] -> "" + "o" + "l" + "l" + "e"
            return reverse_string("hello", 2 + 1) + text[2] -> "" + "o" + "l" + "l"
                return reverse_string("hello", 3 + 1) + text[3] -> "" + "o" + "l"
                    return reverse_string("hello", 4 + 1) + text[4] -> "" + "o" 
                        return reverse_string("hello", 5) -> ""
