grades = {
    "Анна": (5, 4, 5, 5),
    "Иван": (4, 4, 3, 5),
    "Олег": (3, 4, 3, 3),
    "Мария": (5, 5, 5, 4)
}
print(f"grades: {grades}")
bestGrade = float('-inf')

for key, value in grades.items():
    average = sum(value) / len(value)
    if bestGrade < average:
        bestGrade = average
    print(f"{key}: {average}")
print(f"bestGrade: {bestGrade}")