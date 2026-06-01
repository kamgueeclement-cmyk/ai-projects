# AI Text Analyzer
# Author: Nouetakdie Kamgue Clement

text = input("Enter a text: ")

characters = len(text)

words = text.split()
word_count = len(words)

sentences = text.count(".") + text.count("!") + text.count("?")

frequency = {}

for word in words:
    word = word.lower().strip(".,!?;:")
    frequency[word] = frequency.get(word, 0) + 1

print("\nTEXT ANALYSIS")
print("-" * 30)
print("Characters:", characters)
print("Words:", word_count)
print("Sentences:", sentences)

print("\nMost Common Words:")

sorted_words = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

for word, count in sorted_words[:10]:
    print(word, ":", count)
