from typing import Callable
import re

def generator_numbers(text: str):
    # регуляр 27.45
    pattern = r"\d+.\d+"
    result = re.findall(pattern, text)
    # ленивий возврат
    for num1 in result:
        yield float(num1)

def sum_profit(text: str, func: Callable):
    sum = 0
    # генератор з тексту
    for num1 in func(text):
        sum = sum + num1
    return sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")