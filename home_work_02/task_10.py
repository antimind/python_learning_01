products = {
    "Ноутбук": 85000,
    "Мышь": 3500,
    "Клавиатура": 7200,
    "Монитор": 32000,
    "Soft": 130999,
    "Наушники": 11500
}
print(f"products: {products}")
mostExpensive = {
    "name": "",
    "price": float('-inf')
}
for name, price in products.items():
    if price > mostExpensive["price"]:
        mostExpensive["name"] = name
        mostExpensive["price"] = price
    print(f"  debug-----=== name: {name}, price: {price}")
print(f"mostExpensive: {mostExpensive}")