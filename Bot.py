import string
from collections import Counter

# Read words from the file, removing leading/trailing whitespaces
with open("Every Word (No Letters Or Symbols).txt", "r") as File:
    Words = [line.strip() for line in File]

# Get compulsory letter from user input and convert to lowercase
Compulsory_Letter = input("What is the compulsory letter? ").lower()

# Get all possible letters from user input and convert to lowercase
Possible_Letters = input("Give all possible letters. ").lower()

# Convert the string of possible letters to a list
Possible_Letters = list(Possible_Letters)

# Append the compulsory letter to the list of possible letters
Possible_Letters.append(Compulsory_Letter)

# Count the frequency of each letter in the list
Letter_Frequencies = Counter(Possible_Letters)

# Convert the list of possible letters to a set
Possible_Letters = set(Possible_Letters)

# Create a set of Impossible Letters by subtracting Possible_Letters from the entire lowercase alphabet
Impossible_Letters = set(string.ascii_lowercase) - Possible_Letters

# Display the total number of words before any filtering
print("Total words before filtering:", len(Words))

# Filter words with length greater than 3
Words = [Word for Word in Words if len(Word) > 3]
print("Words after minimum length filtering:", len(Words))

# Filter words with length less than 8
Words = [Word for Word in Words if len(Word) < 8]
print("Words after maximum length filtering:", len(Words))

# Filter words containing the compulsory letter
Words = [Word for Word in Words if Compulsory_Letter.lower() in Word.lower()]
print("Words after compulsory letter filtering:", len(Words))

# Filter words based on the presence of optional letters
Words = [Word for Word in Words if not any(Letter in Word for Letter in Impossible_Letters)]
print("Words after optional letter filtering:", len(Words))

# Convert Letter_Frequencies to a dictionary
Letter_Frequencies = dict(Letter_Frequencies)

# Filter words based on letter frequencies
Words = [Word for Word in Words if all(Word.count(Letter) <= Letter_Frequencies.get(Letter.lower(), 0) for Letter in Word)]

# Remove duplicates by converting the list to a set and back to a list
Words = list(set(Words))

# Display the final list of words and its length
print("Final Number of Words:", len(Words))
print("Final List of Words:", Words)