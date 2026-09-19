sum_text = input("Enter text: ").strip().lower()
if sum_text.count("руб") != 1:
    print("Некорректный формат суммы")
    exit()

sum_parts = sum_text.split("руб")
rub = sum_parts[0].strip()
if len(rub) == 0:
    print("Некорректный формат суммы")
    exit()

cop_part = sum_parts[1].strip()
if len(cop_part) != 0 and cop_part.count("коп") != 1:
    print("Некорректный формат суммы")
    exit()

cop = cop_part.split("коп")[0].strip()
if len(cop) > 2:
    print("Некорректный формат суммы")
    exit()

total = float(f"{rub}.{cop}")  # если cop_str = '' => float(xx.) - ок
formatted_total = f"{total:.2f} ₽"
print(formatted_total)
