numbers = [10, -5, 7, -3, 15, 0, 8]
print("\nAll numbers from 0 array: ", numbers)

result = []
for number in numbers:
    if number > 0:
        result.append(number)
print("\nOnly numbers > 0: ", result)