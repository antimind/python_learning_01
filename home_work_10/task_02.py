products = [
    "Хлеб",
    "Молоко",
    "Сыр",
    "Яблоки"
]

print(f"Products: {products}\n")

with open("text.txt", "w") as text_file:
    for product in products:
        text_file.write(f"{product}\n")

with open("text.txt", "r") as text_file:
    text_from_file = text_file.read()
    print(f"Text:\n{text_from_file}")