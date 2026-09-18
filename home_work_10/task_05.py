import json

FILE_NAME = "settings.json"

def write_settings(settings_data):
    with open(FILE_NAME, "w") as file:
        json.dump(settings_data, file, indent=4)

def read_settings() -> dict[str, object]:
    try:
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                print(f"File {FILE_NAME} is not JSON")
                exit(0)
    except FileNotFoundError:
        print(f"File not found: {FILE_NAME}")
        exit(0)


settings = {
    "theme": "dark",
    "language": "ru",
    "notifications": True
}

print(f"Settings: {settings}\n")

write_settings(settings)
settings_from_file = read_settings()

print(f"Settings from file: {settings_from_file}\n")

settings_from_file.update({"theme" : "dark", "font_size" : 16})
print(f"Updated settings from file: {settings_from_file}\n")
write_settings(settings_from_file)

print(f"Saved settings from file: {read_settings()}\n")
with open(FILE_NAME, "r") as file:
    print(f"JSON from file:\n{file.read()}")

