python_group = {"Анна", "Иван", "Мария", "Олег", "Алексей"}
django_group = {"Иван", "Мария", "Сергей", "Алексей"}
docker_group = {"Мария", "Алексей", "Павел", "Иван"}

print(f"python_group: {python_group}\ndjango_group: {django_group}\ndocker_group: {docker_group}"
      f"All courses: {python_group & django_group & docker_group}\n"
      f"All students: {python_group & django_group & docker_group}\n"
      f"Only python: {python_group - django_group - docker_group}")