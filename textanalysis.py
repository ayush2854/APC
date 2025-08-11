text = input("Enter a paragraph: ")

words = text.split()
print("Total number of words:", len(words))

word_freq = {}
for word in words:
    word = word.lower() 
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("\nWord frequencies:")
for word, count in word_freq.items():
    print(word, ":", count)

sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
print("\nTop 3 most frequent words:")
for word, count in sorted_words[:3]:
    print(word, ":", count)

vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1

print("\nNumber of vowels in the text:", vowel_count)