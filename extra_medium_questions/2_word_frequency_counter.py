words = []
while True:
    word = input("Enter a word (or 'done'):").lower()
    if word == "done":
        break
    words.append(word)
search_word = input("Enter word to search:")
count = 0
i = 0

while i < len(words):
    if words[i] == search_word:
        count += 1
    i += 1
print(f"'{search_word}' appears {count} times")