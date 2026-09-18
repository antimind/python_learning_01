import pathlib

dir_path = pathlib.Path("reports", "2026", "september")

try:
    dir_path.mkdir(parents=True, exist_ok=False)
    print(f"Directory '{dir_path}' created\n")
except FileExistsError:
    print(f"Directory '{dir_path}' already exists\n")

file_path = dir_path.joinpath("report.txt")
file_path.write_text("Report created")

print(f"- File name: {file_path.name}\n- Parent directory: {file_path.parent}\n"
      f"- Is exists: {file_path.exists()}\n- Is file: {file_path.is_file()}"
      f"- Absolute path: {file_path.absolute()}")




