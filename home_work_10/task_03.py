import os
import pathlib

dir_path = os.path.join("reports", "2026", "september")
path = pathlib.Path(dir_path)

try:
    path.mkdir(parents=True, exist_ok=False)
    print(f"Directory '{path}' created\n")
except FileExistsError:
    print(f"Directory '{path}' already exists\n")

file_path = pathlib.Path(dir_path, "report.txt")
path = pathlib.Path(file_path)
path.write_text("Report created")

print(f"- File name: {path.name}\n- Parent directory: {path.parent}\n"
      f"- Is exists: {path.exists()}\n- Is file: {path.is_file()}"
      f"- Absolute path: {path.absolute()}")




