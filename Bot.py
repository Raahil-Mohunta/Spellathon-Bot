import string
from collections import Counter

# Read words from file and strip leading/trailing whitespaces
with open("Every Word (No Letters Or Symbols).txt", "r") as File:
    Words = [line.strip() for line in File]

# Get compulsory letter from user input and convert to lowercase
Compulsory_Letter = input("What is the compulsory letter? ").lower()

Possible_Letters = input("Give all possible letters. ").lower()
Possible_Letters = list(Possible_Letters)
Letter_Frequencies = Counter(Possible_Letters)
print(Letter_Frequencies)
Possible_Letters = set(Possible_Letters)

# Create a set of Impossible Letters
Impossible_Letters = set(string.ascii_lowercase) - Possible_Letters

# Display the total number of words before any filtering
print("Total words:", len(Words))

# Filter words with length greater than 3
Words = [Word for Word in Words if len(Word) > 3]
print("Words after minimum length filtering:", len(Words))

# Filter words with length less than 8
Words = [Word for Word in Words if len(Word) < 8]
print("Words after maximum length filtering:", len(Words))

Words = [Word for Word in Words if Compulsory_Letter.lower() in Word.lower()]
print("Words after compulsory letter filtering:", len(Words))

# Filter words based on letter frequencies
Words = [Word for Word in Words if not any(Letter in Word for Letter in Impossible_Letters)]
print("Words after optional letter filtering:", len(Words))

New_List = []

for Word in Words:
    Word_Frequencies = Counter(Word.lower())
    if all(Word_Frequencies[Letter] <= Letter_Frequencies[Letter] for Letter in Impossible_Letters):
        New_List.append(Word)

# Remove duplicates by converting the list to a set and back to a list
Words = list(set(New_List))

# Display the final list of words and its length
print("Final List of Words:", Words)
print("Number of Words:", len(Words))