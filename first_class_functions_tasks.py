# -*- coding: utf-8 -*-
"""
Функції першого класу у Python

У файлі виконано 14 завдань:
- присвоєння функції змінній;
- збереження функцій у списках і словниках;
- передача функцій як аргументів;
- повернення функцій з інших функцій;
- closure;
- pipeline;
- rule engine;
- functional calculator engine.
"""


def print_title(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


# =============================================================================
# Завдання 1. Присвоєння функції змінній
# =============================================================================

print_title("Завдання 1. Присвоєння функції змінній")


def square(x):
    return x * x


f = square

print("f(5) =", f(5))

print("\nПояснення:")
print("У Python функції є об'єктами першого класу.")
print("Це означає, що функцію можна зберігати у змінній, передавати як аргумент")
print("і повертати з іншої функції.")
print("Змінна f зберігає посилання на об'єкт функції square, а не результат її виконання.")


# =============================================================================
# Завдання 2. Список функцій
# =============================================================================

print_title("Завдання 2. Список функцій")


def add_one(x):
    return x + 1


def double(x):
    return x * 2


operations_list = [add_one, double, square]

number = 10
results = [operation(number) for operation in operations_list]

print("Число:", number)
print("Результати застосування всіх функцій:", results)

print("\nОкремий вивід:")
for operation in operations_list:
    print(f"{operation.__name__}({number}) =", operation(number))

print("\nПояснення:")
print("Функції можна зберігати у списку так само, як числа, рядки або словники.")


# =============================================================================
# Завдання 3. Універсальна функція
# =============================================================================

print_title("Завдання 3. Універсальна функція")


def apply(func, x):
    return func(x)


print("apply(square, 5) =", apply(square, 5))
print("apply(double, 5) =", apply(double, 5))

print("\nПояснення:")
print("apply приймає функцію func як параметр і застосовує її до x.")


# =============================================================================
# Завдання 4. Калькулятор через функції
# =============================================================================

print_title("Завдання 4. Калькулятор через функції")


def calculate(operation, a, b):
    return operation(a, b)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


print("Додавання:", calculate(add, 10, 5))
print("Множення:", calculate(multiply, 10, 5))
print("Віднімання:", calculate(subtract, 10, 5))

print("\nПояснення:")
print("calculate отримує поведінку через функцію operation.")
print("Тому одна функція calculate може виконувати різні операції.")


# =============================================================================
# Завдання 5. Map-подібна функція
# =============================================================================

print_title("Завдання 5. Map-подібна функція")


def map_custom(func, data):
    result = []
    for item in data:
        result.append(func(item))
    return result


print("map_custom(lambda x: x*x, [1, 2, 3]) =", map_custom(lambda x: x * x, [1, 2, 3]))
print("map_custom(double, [1, 2, 3]) =", map_custom(double, [1, 2, 3]))

print("\nПояснення:")
print("map_custom застосовує передану функцію до кожного елемента списку.")


# =============================================================================
# Завдання 6. Генератор функцій
# =============================================================================

print_title("Завдання 6. Генератор функцій")


def multiplier(n):
    def inner(x):
        return x * n

    return inner


times3 = multiplier(3)
times5 = multiplier(5)

print("times3(5) =", times3(5))
print("times5(5) =", times5(5))
print("map_custom(times3, [1, 2, 3, 4]) =", map_custom(times3, [1, 2, 3, 4]))

print("\nПояснення:")
print("multiplier повертає нову функцію inner.")
print("Це приклад того, що функція може бути результатом роботи іншої функції.")


# =============================================================================
# Завдання 7. Closure
# =============================================================================

print_title("Завдання 7. Closure")


def make_adder(n):
    def inner(x):
        return x + n

    return inner


add10 = make_adder(10)
add100 = make_adder(100)

print("add10(5) =", add10(5))
print("add100(5) =", add100(5))

print("\nПояснення:")
print("Closure, або замикання, — це ситуація, коли внутрішня функція")
print("зберігає доступ до змінних зовнішньої функції навіть після завершення")
print("роботи зовнішньої функції.")
print("У цьому прикладі add10 пам'ятає n = 10.")


# =============================================================================
# Завдання 8. Таблиця операцій
# =============================================================================

print_title("Завдання 8. Таблиця операцій")


def safe_divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль"
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": safe_divide,
}

print('operations["+"](2, 3) =', operations["+"](2, 3))
print('operations["-"](10, 4) =', operations["-"](10, 4))
print('operations["*"](6, 7) =', operations["*"](6, 7))
print('operations["/"](20, 5) =', operations["/"](20, 5))
print('operations["/"](20, 0) =', operations["/"](20, 0))

print("\nПояснення:")
print("Словник operations працює як таблиця вибору операції.")
print("Ключ — це символ операції, значення — відповідна функція.")


# =============================================================================
# Завдання 9. Динамічний вибір алгоритму
# =============================================================================

print_title("Завдання 9. Динамічний вибір алгоритму")


def sort_asc(data):
    return sorted(data)


def sort_desc(data):
    return sorted(data, reverse=True)


strategies = {
    "asc": sort_asc,
    "desc": sort_desc,
}

sort_data = [5, 1, 4, 2, 3]

selected_strategy = "asc"
print("Початкові дані:", sort_data)
print("Стратегія asc:", strategies[selected_strategy](sort_data))

selected_strategy = "desc"
print("Стратегія desc:", strategies[selected_strategy](sort_data))

print("\nПояснення:")
print("Алгоритм сортування обирається динамічно через ключ словника strategies.")


# =============================================================================
# Завдання 10. Побудова pipeline
# =============================================================================

print_title("Завдання 10. Побудова pipeline")


def pipeline(data, steps):
    result = data
    for step in steps:
        result = step(result)
    return result


pipeline_result = pipeline(
    [1, 2, 3, 4],
    [
        lambda x: [i for i in x if i % 2 == 0],
        lambda x: [i * i for i in x],
    ],
)

print("pipeline result =", pipeline_result)

print("\nПояснення:")
print("pipeline послідовно застосовує список функцій steps до даних.")
print("Результат одного кроку стає вхідними даними для наступного кроку.")


# =============================================================================
# Завдання 11. Обробка даних
# =============================================================================

print_title("Завдання 11. Обробка даних")

numbers = [1, 2, 3, 4, 5]


def process(data, func):
    result = []
    for item in data:
        result.append(func(item))
    return result


print("numbers =", numbers)
print("process(numbers, double) =", process(numbers, double))
print("process(numbers, square) =", process(numbers, square))
print("process(numbers, lambda x: x + 100) =", process(numbers, lambda x: x + 100))

print("\nПояснення:")
print("process є універсальною функцією обробки даних.")
print("Конкретна логіка передається через параметр func.")


# =============================================================================
# Завдання 12. Обробка транзакцій
# =============================================================================

print_title("Завдання 12. Обробка транзакцій")

transactions = [100, 200, 300]


def apply_tax(amount):
    return amount * 1.20


def apply_discount(amount):
    return amount * 0.90


def process_transactions(transactions, operation):
    return [operation(transaction) for transaction in transactions]


print("Початкові транзакції:", transactions)
print("Після податку 20%:", process_transactions(transactions, apply_tax))
print("Після знижки 10%:", process_transactions(transactions, apply_discount))

print("\nПояснення:")
print("Функції apply_tax і apply_discount передаються як параметри.")
print("Тому process_transactions можна використовувати для різних правил обробки.")


# =============================================================================
# Завдання 13. Rule Engine
# =============================================================================

print_title("Завдання 13. Rule Engine")

rules = [
    lambda x: x + 10,
    lambda x: x * 2,
    lambda x: x - 5,
]


def apply_rules(value, rules):
    result = value
    for rule in rules:
        result = rule(result)
    return result


print("apply_rules(10, rules) =", apply_rules(10, rules))
print("Пояснення обчислення: 10 + 10 = 20; 20 * 2 = 40; 40 - 5 = 35")

print("\nПояснення:")
print("Rule Engine — це підхід, коли набір правил зберігається як список функцій.")
print("Кожне правило послідовно змінює поточне значення.")


# =============================================================================
# Завдання 14. Functional Calculator Engine
# =============================================================================

print_title("Завдання 14. Functional Calculator Engine")


def square_one_arg(x):
    return x * x


engine = {
    "add": add,
    "mul": multiply,
    "square": square_one_arg,
}

print('engine["add"](2, 3) =', engine["add"](2, 3))
print('engine["mul"](4, 5) =', engine["mul"](4, 5))
print('engine["square"](6) =', engine["square"](6))

print("\nДоступні операції engine:")
print(list(engine.keys()))

print("\nПояснення:")
print("engine — це функціональний калькулятор, де операції збережені у словнику.")
print("Кожна команда відповідає певній функції.")


# =============================================================================
# Загальний висновок
# =============================================================================

print_title("Загальний висновок")

print("Функції першого класу — це функції, з якими можна працювати як зі звичайними")
print("значеннями: присвоювати змінним, зберігати у списках і словниках, передавати")
print("як аргументи та повертати з інших функцій.")
print()
print("У Python функції є об'єктами першого класу, тому можна будувати гнучкі")
print("системи обробки даних, калькулятори, rule engine, pipeline та динамічний")
print("вибір алгоритмів.")
