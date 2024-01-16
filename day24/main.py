with open("./Input/Letters/starting_letter.txt") as starting_tx:
    base_txt = starting_tx.read()
with open("./Input/Names/invited_names.txt") as names:
    all_names = names.readlines()
for name in all_names:
    name = name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as readi_tx:
        readi_tx.write(base_txt.replace("[name]", name))
