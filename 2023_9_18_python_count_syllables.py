# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

# Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')

# Count the words
words = len(text.split())

# Func to count the syllables in a word
def count_syllables(word):
    vowels = "aeiou"
    prev_char = ""
    syllables = 0
    for char in word:
        char = char.lower()
        if char in vowels and prev_char not in vowels:
            syllables += 1
        prev_char = char         # keep it moving
    for ending in ['es', 'ed', 'e']: 
    	if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1
    if syllables == 0:
        syllables = 1             # at least 1 for any word
    return syllables
        
# simple loop over all text, count as we go
syllables = 0
for word in text.split():
    syllables += count_syllables(word)


# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * \
                  (syllables / words) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables") 
