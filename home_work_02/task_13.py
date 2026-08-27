grades = {
    "Анна": (5, 4, 5, 5),
    "Иван": (4, 4, 3, 5),
    "Олег": (3, 4, 3, 3),
    "Мария": (5, 5, 5, 4)
}
print(f"grades: {grades}\nAverage:")
avgGrades = {}
for key, value in grades.items():
    avgGrades[key] = sum(value) / len(value)
    print(f"- {key}: {avgGrades[key]}")
bestGrade = max(avgGrades.values())
print(f"\nbestGrade: {bestGrade}\n\nBest students:")
for key, value in avgGrades.items():
    if value == bestGrade:
        print(f" - {key}: {value}")