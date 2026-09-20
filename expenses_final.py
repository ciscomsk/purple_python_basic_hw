menu_items = [
    "Добавить расход",
    "Показать все расходы",
    "Показать сумму и средний расход",
    "Удалить расход по номеру",
    "Выход"
]

expenses = []


def add_expense(exp: list[int], amount: int) -> None:
    exp.append(amount)


def print_report(exp: list[int], sep: str = ", ") -> None:
    print(sep.join(str(s) for s in exp))


def delete_expense(exp: list[int], index: int) -> None:
    del exp[index]


def get_total(exp: list[int]) -> int:
    return sum(exp)


def get_average(exp: list[int]) -> float:
    return sum(exp) / len(exp)


while True:
    for i, item in enumerate(menu_items):
        print(f"{i + 1}: {item}")

    user_choice = -1
    while user_choice < 1 or user_choice > len(menu_items):
        user_choice = int(input("Enter your choice: "))
        if user_choice < 1 or user_choice > len(menu_items):
            print("Incorrect choice")

    match user_choice:
        case 1:
            value = int(input("Enter expense: "))
            add_expense(expenses, value)
        case 2:
            print_report(expenses)
        case 3:
            print(get_total(expenses))
            print(get_average(expenses))
        case 4:
            idx = int(input("Enter expense index: "))
            delete_expense(expenses, idx)
        case 5:
            exit()
