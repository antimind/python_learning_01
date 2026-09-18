import csv
import io
import json
import pathlib
from pathlib import Path
from typing import Any

FILE_NAME_PRODUCTS = "products.json"
FILE_NAME_ORDERS = "orders.csv"
FILE_NAME_REPORT = "report.txt"
DIR_NAME = "reports"

def write_file(_path_dir:Path, _file_name, _data):
    _path = _path_dir.joinpath(_file_name)
    _path.write_text(_data, encoding="utf-8")

def read_file(_path_dir:Path, _file_name, is_json) -> dict[str, Any] | None:
    _path = _path_dir.joinpath(_file_name)
    if _path.is_file() and is_json:
        try:
            return json.loads(_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"File '{_file_name}' is not JSON.\n")
    elif _path.is_file() and not is_json:
        csv_reader = csv.reader(io.StringIO(_path.read_text(encoding="utf-8")))
        result = {}
        for row in csv_reader:
            if row[1].isdigit():
                result.update({row[0]: int(row[1])})
            else:
                print(f"Price for '{row[0]}' is not a number.\n")
        return result
    else:
        print(f"File '{_file_name}' not found.\n")
        return None

products_data = {
    "Ноутбук": 80000,
    "Мышь": 2000,
    "Монитор": 30000,
    "Клавиатура": 5000
}
orders_data = "Ноутбук,2\nМышь,10\nМонитор,3\nКлавиатура,4"

path_dir = pathlib.Path(DIR_NAME)
if not path_dir.exists():
    path_dir.mkdir(parents=True, exist_ok=True)

# Write products
write_file(path_dir, FILE_NAME_PRODUCTS, json.dumps(products_data, indent=4))
# Write orders
write_file(path_dir, FILE_NAME_ORDERS, orders_data)

# Read products
products = read_file(path_dir, FILE_NAME_PRODUCTS, True)
# Read orders
orders = read_file(path_dir, FILE_NAME_ORDERS, False)

if products is None or orders is None:
    exit(0)

print(f"Products: {products}\nOrders: {orders}\n")
report = ""
max_amount = {"name": "", "amount": float("-inf")}
for name, price in products.items():
    if name in orders.keys():
        amount = price * orders[name]
        report += f"{name}: {amount}\n"
        if max_amount["amount"] < amount:
            max_amount["name"] = name
            max_amount["amount"] = amount

report += (f"Total amount: {max_amount['amount']}\n"
           f"Max amount: {max_amount['name']}\n")

write_file(path_dir, FILE_NAME_REPORT, report)

print(f"Report file:\n{path_dir.joinpath(FILE_NAME_REPORT).read_text()}")