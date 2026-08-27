words = (
    "python",
    "java",
    "python",
    "go",
    "java",
    "python",
    "javascript",
    "go"
)
wordCount = {}
for word in words:
    wordCount[word] = wordCount.get(word, 0) + 1
print(f"words: {words}\nwordCount: {wordCount}")