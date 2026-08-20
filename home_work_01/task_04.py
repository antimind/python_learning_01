words = ["python", "java", "python", "go", "java", "javascript"]
excludeDuplicateWords = []
for word in words:
    if word not in excludeDuplicateWords:
        excludeDuplicateWords.append(word)
print(words)
print(excludeDuplicateWords)