text = input("Enter text: ").strip().lower()

if text.count("руб") != 1:
    print("Некорректный формат суммы")
    exit()

text_parts = text.split("руб")
rub_part = text_parts[0].strip()
cop_part = text_parts[1].strip()
has_cop = text_parts[1].count("коп") == 1
total = float(rub_part) if not has_cop else float(f"{rub_part}.{cop_part.split("коп")[0].strip()}")
formatted_total = f"{total:.2f} ₽"
print(formatted_total)