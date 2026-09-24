import sys

if len(sys.argv) < 3:
    print("Нужно 2 аргумента")
    exit()

# print(sys.argv)
# print(len(sys.argv))

action = sys.argv[1]
action_arg = sys.argv[2]

books: dict[str, str] = {}

books["Сияние"] = "Стивен Кинг"
books["Кладбище домашних животных"] = "Стивен Кинг"
books["Двадцать тысяч лье под водой"] = "Жюль Верн"

# print(books.items())
# print(list(books.items()))
# print(list(books.items())[0])

match action:
    case "filter":
        filtered = filter(lambda el: el[1] == action_arg, list(books.items()))
        mapped = map(lambda b: f"{b[0]} - {b[1]}", filtered)
        print(list(mapped))
    case "sort":
        sort_by = 0 if action_arg == "book" else 1  # а если добавится еще
        ordered = sorted(list(books.items()), key=lambda b: b[sort_by])
        mapped = map(lambda b: f"{b[0]} - {b[1]}", ordered)
        print(list(mapped))
    case _:
        print("Неизвестное действие")
