# Program 2: String Manipulation
# Shows common string operations on user input.

text = input("Type a sentence: ").strip()

print("Uppercase:   ", text.upper())
print("Lowercase:   ", text.lower())
print("Title case:  ", text.title())
print("Reversed:    ", text[::-1])          # slicing
print("First 5 chars:", text[:5])           # slicing
print("Word count:  ", len(text.split()))
print("Letter 'a' appears", text.lower().count("a"), "times")

word = input("Search for a word: ")
if word.lower() in text.lower():
    print(f"'{word}' found at position {text.lower().find(word.lower())}")
else:
    print(f"'{word}' not found.")

print("With dashes: " + "-".join(text.split()))   # concatenation/join
