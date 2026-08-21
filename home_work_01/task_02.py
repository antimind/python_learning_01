colors = ["красный", "зелёный", "синий", "жёлтый"]
print(colors)
if "зелёный" in colors:
    index = colors.index("зелёный")
    colors[index] = "белый"
if "жёлтый" in colors:
    index = colors.index("жёлтый")
    colors.pop(index)
print(colors)
