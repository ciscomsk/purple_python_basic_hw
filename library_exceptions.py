import sys


class LibraryException(Exception):
    pass


class EmptyFilterError(LibraryException):
    pass


class InvalidCommandError(LibraryException):
    pass


class InvalidSortParameterError(LibraryException):
    pass


if len(sys.argv) < 3:
    print("Нужно 2 аргумента")
    exit()

command = sys.argv[1]
command_arg = sys.argv[2]

books: dict[str, str] = {}

books["Сияние"] = "Стивен Кинг"
books["Кладбище домашних животных"] = "Стивен Кинг"
books["Двадцать тысяч лье под водой"] = "Жюль Верн"

try:
    match command:
        case "filter":
            if not command_arg.strip():
                raise EmptyFilterError("Пустой фильтр")
            filtered = filter(lambda el: el[1] == command_arg, list(books.items()))
            mapped = map(lambda b: f"{b[0]} - {b[1]}", filtered)
            print(list(mapped))
        case "sort":
            match command_arg:
                case "book":
                    sort_by = 0
                case "author":
                    sort_by = 1
                case _:
                    raise InvalidSortParameterError("Неверный параметр для сортировки")

            ordered = sorted(list(books.items()), key=lambda b: b[sort_by])
            mapped = map(lambda b: f"{b[0]} - {b[1]}", ordered)
            print(list(mapped))
        case _:
            raise InvalidCommandError("Неизвестная команда")
except (EmptyFilterError, InvalidSortParameterError, InvalidCommandError) as e:
    # print(e)
    print(f"{type(e).__name__}: {e}")
