products = {
    "apple": 100,
    "banana": 80,
    "orange": 120
}
print(f"products: {products}")
product = input("Enter a product: ")
if product in products:
    print(f"The product {product} cost {products[product]}")
else:
    print(f"The product {product} doesn't exist")