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
    msg = sep.join(str(s) for s in exp) if exp else "Expenses is empty"
    print(msg)


def delete_expense(exp: list[int], index: int) -> None:
    if not exp:
        print("Expenses is empty")
        return
    while index < 0 or index > len(exp) - 1:
        print("Incorrect index")
        index = int(input("Enter expense index: "))

    del exp[index]


def get_total(exp: list[int]) -> int:
    # можно вывести сообщение
    return sum(exp)


def get_average(exp: list[int]) -> float:
    if not exp:
        print("Expenses is empty")
        return 0
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
            # можно здесь проверить список на пустоту
            print(get_total(expenses))
            print(get_average(expenses))
        case 4:
            # можно здесь проверить список на пустоту
            idx = int(input("Enter expense index: "))
            delete_expense(expenses, idx)
        case 5:
            exit()
