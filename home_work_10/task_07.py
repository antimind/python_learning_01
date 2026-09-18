import csv
import json

FILE_NAME_CSV = "students.csv"
FILE_NAME_JSON = "students.json"

csv_data = "Анна,5,4,5\nИван,4,3,4\nМария,5,5,5\nОлег,3,4,3"
list_data = []

with open(FILE_NAME_CSV, "w", encoding="utf-8") as csvfile:
    csvfile.write(csv_data)

with open(FILE_NAME_CSV, "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    print("CSV data:\n")
    for row in reader:
        print(f"- {row}\n")
        grades = list(map(int, (row[1:])))
        student_data = {"name": row[0], "grades": grades, "average": round(sum(grades)/len(grades), 1)}
        list_data.append(student_data)

print(f"Structured students: {list_data}\n")

with open(FILE_NAME_JSON, "w", encoding="utf-8") as json_file:
    json_file.write(json.dumps(list_data, ensure_ascii=False, indent=4))

with open(FILE_NAME_JSON, "r", encoding="utf-8") as json_file:
    json_data = json_file.read()

print(f"JSON data: {json_data}\n")

max_average = {"name": "", "average": float("-inf")}
for student_data in json.loads(json_data):
    if student_data["average"] > max_average["average"]:
        max_average["name"] = student_data["name"]
        max_average["average"] = student_data["average"]

print(f"Max average:\n"
      f"Name: {max_average["name"]}\n"
      f"Average: {max_average['average']}")