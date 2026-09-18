text = "Python используется для веб-разработки.\nPython подходит для автоматизации.\nИзучать Python интересно."
line_count = 0
with open("article.txt", "w", encoding='utf_8') as file:
    file.write(text)

with open("article.txt", "r", encoding='utf_8') as file:
    text_from_file = file.read()

    for line in file:
        line_count += 1

    print(f"All text:\n{text_from_file}\n\n")
    print(f"Count of strings: {line_count},\nCount of chars: {len(text_from_file)}")
