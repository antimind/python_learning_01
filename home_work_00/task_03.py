from sys import maxsize

numbers = [12, 5, 8, 21, 3, 17]
print(numbers)
numbersSum = 0
maxNumber = numbers[0]
minNumber = numbers[0]
for number in numbers:
    numbersSum += number
    if number > maxNumber:
        maxNumber = number
    elif number < minNumber:
        minNumber = number
print(f"Sum: {numbersSum}, Max: {maxNumber}, Min: {minNumber}")