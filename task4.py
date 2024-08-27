def dis(price, discount):
    return price * (1 - discount / 100)

price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

final_price = dis(price, discount)
print(f"The final price after a {discount}% discount is: {final_price}")
