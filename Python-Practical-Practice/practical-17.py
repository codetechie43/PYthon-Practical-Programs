sentence = input("Enter a sentence: ")
words = sentence.split()
sorted_words = sorted(words)

print("Sorted words in alphabetic order:")
for word in sorted_words:
    print(word)

