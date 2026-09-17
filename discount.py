price = int(input("Enter price: "))  # можно float()
discount_percent = int(input("Enter discount: "))
discounted_price = price - price * discount_percent / 100
print(discounted_price)
