sales = {
    "Ноутбук": 7,
    "Мышь": 25,
    "Клавиатура": 14,
    "Монитор": 9,
    "Наушники": 18
}
prices = {
    "Ноутбук": 85000,
    "Мышь": 3500,
    "Клавиатура": 7200,
    "Монитор": 32000,
    "Наушники": 11500
}
print(f"sales: {sales}\nprices: {prices}\n")
saleRevenue = {}
totalRevenue = 0
maxRevenue = float("-inf")
maxSales = max(sales.values())
for key, value in sales.items():
    saleRevenue[key] = sales[key] * prices[key]
    if saleRevenue[key] > maxRevenue:
        maxRevenue = saleRevenue[key]
    totalRevenue += saleRevenue[key]
print(f"Total revenue: {totalRevenue}\n")
for key, value in saleRevenue.items():
    if sales[key] == maxSales:
        print(f" - Max sales: '{key}'\n   Items: {value}\n")
    if value == maxRevenue:
        print(f" - Max revenue: '{key}'\n   Revenue: {value}\n")