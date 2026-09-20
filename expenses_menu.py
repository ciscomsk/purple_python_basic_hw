# выводить номера пунктов и выбирать из них
menu_items = [
    "Добавить расход",
    "Показать все расходы",
    "Показать сумму и средний расход",
    "Удалить расход по номеру",
    "Выход"
]

while True:
    for item in menu_items:
        print(item)

    user_choice = ""
    while user_choice not in menu_items:
        user_choice = input("Enter your choice: ")
        if user_choice not in menu_items:
            print("Incorrect choice")

    if user_choice == "Выход":
        break
