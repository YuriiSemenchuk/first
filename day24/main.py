with open("./Input/Letters/starting_letter.txt") as starting_tx:  # получаю текст який треба відредагувати
    base_txt = starting_tx.read()
with open("./Input/Names/invited_names.txt") as names:  # получаю список імен для редагування тексту
    all_names = names.readlines()
for name in all_names:  # створюю відредаговані текстові файли
    name = name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as readi_tx:
        readi_tx.write(base_txt.replace("[name]", name))
