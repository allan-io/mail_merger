PLACEHOLDER = "[name]"
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    new_content = letter_contents
    for name in names:
        new_letter = letter_contents.replace("[Name]", name.strip())
        with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
