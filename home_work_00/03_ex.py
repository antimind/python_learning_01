age = int(input("Enter your age: "))
if age < 18:
    print("Access forbidden!")
elif 18 <= age <= 65:
    print("Access granted!")
elif age > 65:
    print("Access granted! Discount available!")