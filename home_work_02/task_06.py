python_students = {"Анна", "Иван", "Олег", "Мария"}
web_students = {"Иван", "Мария", "Алексей"}
print(f"python_students: {python_students}"
      f"\nweb_students: {web_students}"
      f"\nboth: {python_students.intersection(web_students)}"
      f"\nonly python: {python_students.difference(web_students)}")