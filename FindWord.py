import re
import random
import nltk
from nltk.corpus import words

nltk.download('words')

# Save it to a list named list_words
list_words = words.words()
list_words = [word.lower() for word in list_words]
list_words = list(dict.fromkeys(list_words))

# Function to arrange the words
def ArrangeWord(list_words, characters_list, list_input, max_characters):

    pattern_parts = []
    for char in list_input.values():
        if char == '.':
            pattern_parts.append('[a-z]')
        else:
            pattern_parts.append(char)
    pattern = ''.join(pattern_parts)
    
    valid_chars = characters_list + ''.join(list_input.values())
    matching_words = []
    for word in list_words:
        if len(word) <= max_characters and re.search(pattern, word):
            if all(word.count(char) <= valid_chars.count(char) for char in set(word)):
                matching_words.append(word)
    return matching_words

# Input of characters we have
list_characters = input("Type your own unused letters (no space): ")

# Create a dictionary to save inputs
list_input = {}

# Input of how many maximum characters we need to arrange
max_characters = int(input("Type your maximum characters you expected: "))

# Input of what specific position of the character
for i in range(1, max_characters + 1):
    fix_position = input(f"Words Number {i}: ")
    list_input[f"fix_position{i}"] = fix_position

# Output
characters_list = list_characters.lower()
arranged_words = ArrangeWord(list_words, characters_list, list_input, max_characters)

arranged_words.sort(key=lambda x: (-len(x), x))

print("Arranged Words:")
for word in arranged_words:
    if len(word) > 1:
        print(word)