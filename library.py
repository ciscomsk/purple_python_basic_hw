books: dict[str, str] = {}

books["Сияние"] = "Стивен Кинг"
books["Кладбище домашних животных"] = "Стивен Кинг"
books["Двадцать тысяч лье под водой"] = "Жюль Верн"

for k in books:
    print(k)

for v in set(books.values()):
    print(v)
