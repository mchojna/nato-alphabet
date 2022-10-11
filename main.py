import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row[1].letter: row[1].code for row in nato_df.iterrows()}


word = input("Enter a word: ").upper()
nato_word = []

for letter in word:
    for (key, value) in nato_dict.items():
        if letter == key:
            nato_word.append(value)

if len(nato_word) == 0:
    print("Sorry, only letters in the alphabet please.")
else:
    print(nato_word)
