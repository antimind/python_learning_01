numbers = [10, -5, 7, -3, 15, 0, 8]
print("All numbers from 0 array")
for number in numbers:
    print(number)
print("Only numbers > 0")
for number in reversed(numbers):
    if number > 0:
        print(number)