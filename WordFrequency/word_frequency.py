import collections

with open('words.txt', 'r') as f:
    content = f.read()

words = content.split()

word_counts = collections.Counter(words)

sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

for word, count in sorted_word_counts:
    print(f"{word} {count}")