grades = {
    "Анна": 5,
    "Иван": 4,
    "Олег": 3,
    "Мария": 5,
    "Алексей": 4,
    "Елена": 5,
    "Павел": 3,
    "Ирина": 4,
    "Сергей": 5,
    "Ольга": 2
}
print(f"grades: {grades}")
average = sum(grades.values()) / len(grades)
print(f"average: {average}")