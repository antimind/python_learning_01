import json

user = {
    "name": "Анна",
    "age": 25,
    "city": "Казань",
    "active": True
}

print(f"user: {user}\n")

user_json = json.dumps(user, ensure_ascii=False, indent=4)
print(f"user_json: {user_json}\n")

user_obj = json.loads(user_json)
print(f"user_obj: {user_obj}\n"
      f"type(user_obj): {type(user_obj)}\n"
      f"- Name: {user_obj.get("name")}\n"
      f"- City: {user_obj.get("city")}")