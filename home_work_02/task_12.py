warehouse_1 = {
    "apple": 10,
    "banana": 5,
    "orange": 7
}

warehouse_2 = {
    "banana": 8,
    "orange": 3,
    "pear": 6
}
print(f"warehouse_1: {warehouse_1}\nwarehouse_2: {warehouse_2}")
keys = list(warehouse_1.keys()) + list(warehouse_2.keys())
unionWarehouse = {}
for key in keys:
    if key in warehouse_1 and key in warehouse_2:
        unionWarehouse[key] = warehouse_1[key] + warehouse_2[key]
    elif key in warehouse_1:
        unionWarehouse[key] = warehouse_1[key]
    elif key in warehouse_2:
        unionWarehouse[key] = warehouse_2[key]
print(f"unionWarehouse: {unionWarehouse}")
