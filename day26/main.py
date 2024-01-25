import pandas

# получаю і переробляю файл в словник
phonetic_alfabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alfabet = {row.letter: row.code for (index, row) in phonetic_alfabet_data.iterrows()}

# получаю слово розбиваю на букви і спіставляю з словником ствоюючи список
word = input("Enter a word: ").upper()
word_phonetic = [phonetic_alfabet[letter] for letter in word]
print(word_phonetic)
