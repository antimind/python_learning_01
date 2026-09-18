import csv

FILE_NAME = "sales.csv"

text = "Ноутбук,2,80000\nМышь,5,2000\nМонитор,3,30000\nКлавиатура,4,5000"

with open(FILE_NAME, "w", encoding="utf-8") as f:
    f.write(text)

max_quantity = {"item": "", "quantity": float('-inf')}
all_sales = 0

with open(FILE_NAME, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("All sales:\n")
    for row in reader:
        print(f"- {row}")
        if row[1].isdigit() and row[2].isdigit():
            all_sales += int(row[1]) * int(row[2])
        else:
            print(f"--- There is no quantity or amount in this line\n")
            continue
        if int(row[1]) > max_quantity["quantity"]:
            max_quantity["item"] = row[0]
            max_quantity["quantity"] = int(row[1])

print(f"\nAmount of sales: {all_sales}\n"
      f"Max quantity: {max_quantity['item']}\n"
      f"Quantity: {max_quantity['quantity']}\n")

