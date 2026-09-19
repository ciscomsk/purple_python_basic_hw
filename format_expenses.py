import re

sum_text = input("Enter text: ").strip().lower()

# naive
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

# re.fullmatch
pattern = r"(\d+) руб(?: (\d{2}) коп)?"
match = re.fullmatch(pattern, sum_text)

if not match:
    print("Некорректный формат суммы")
    exit()

rub = match.group(1)
cop = match.group(2) or ""
formatted_total = f"{float(rub + "." + cop):.2f} ₽"
print(formatted_total)
