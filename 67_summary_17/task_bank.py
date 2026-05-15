"""Создать пример банковского счета"""

import random


class BankAccount:
    account_numbers = set()

    def __init__(self, first_name, last_name, phone_num):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_num = phone_num
        self.__user_balance = 0.00
        self.__account_number = self.__get_account_number()

    @classmethod
    def __get_account_number(cls):
        while True:
            account_number = "".join([str(random.randint(0, 9)) for _ in range(20)])
            if account_number not in cls.account_numbers:
                cls.account_numbers.add(account_number)
                return account_number

    def __str__(self):
        return (
            f'BankAccount(first_name="{self.first_name}", '
            f'last_name="{self.last_name}", '
            f'phone_num="{self.phone_num}", '
            f'balance="{self.__user_balance}", '
            f'account_number="{self.__account_number}")'
        )


user_1 = BankAccount("Sab", "Kon", "0125355486")
print(user_1)
