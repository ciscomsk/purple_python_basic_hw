category = input("Выберите категорию: ")

match category:
    case "напиток":
        drink = input("чай кофе сок")
        match drink:
            case "чай":
                print(10)
            case "кофе":
                print(10)
            case "сок":
                print(10)
            case _:
                print("такого напитка нет")
    case "суп":
        soup = input("борщ щи суп-пюре")
        match soup:
            case "борщ":
                print(40)
            case "щи":
                print(30)
            case "суп-пюре":
                print(50)
            case _:
                print("такого супа нет")
    case "десерт":
        desert = input("торт мороженое фрукты")
        match desert:
            case "торт":
                print(40)
            case "мороженое":
                print(30)
            case "фрукты":
                print(50)
            case _:
                print("такого десерта нет")
    case _:
        print("указана неверная категория")