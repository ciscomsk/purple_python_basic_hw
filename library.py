books: dict[str, str] = {}

books["Сияние"] = "Стивен Кинг"
books["Кладбище домашних животных"] = "Стивен Кинг"

for k in books:
    print(k)

for v in set(books.values()):
    print(v)
