import re

sum_text = input("Enter text: ").strip().lower().replace("\\s+", ' ')

# v1 - naive
# if sum_text.count("руб") != 1:
#     print("Некорректный формат суммы")
#     exit()
#
# sum_parts = sum_text.split("руб")
# rub = sum_parts[0].strip()
# if len(rub) == 0:
#     print("Некорректный формат суммы")
#     exit()
#
# cop_part = sum_parts[1].strip()
# if len(cop_part) != 0 and cop_part.count("коп") != 1:
#     print("Некорректный формат суммы")
#     exit()
#
# cop = cop_part.split("коп")[0].strip()
# if len(cop) > 2:
#     print("Некорректный формат суммы")
#     exit()
#
# total = float(f"{rub}.{cop}")  # если cop_str = '' => float(xx.) - ок
# formatted_total = f"{total:.2f} ₽"
# print(formatted_total)

# v2 - re.fullmatch
clean_text = re.sub(r'\s+', ' ', sum_text)
pattern = r"(\d+) руб(?: (\d{1,2}) коп)?"
match = re.fullmatch(pattern, clean_text)

if not match:
    print("Некорректный формат суммы")
    exit()

rub = match.group(1)
cop = (match.group(2) or "").zfill(2)  # zfill(2) - если 1 цифра для копеек: 5 коп - будет 05 коп
total = f"{rub}.{cop}"
formatted_total = f"{float(total):.2f} ₽"
print(formatted_total)
