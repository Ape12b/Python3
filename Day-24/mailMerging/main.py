with open("./Input/Letters/starting_letter.txt") as letter_template:
    letter = letter_template.readlines()
    with open("./Input/Names/invited_names.txt") as guests_name:
        guests = [x.rstrip('\n') for x in guests_name]
        for guest in guests:
            if guest != " ":
                for lineNumber in range(len(letter)):
                    if lineNumber == 0:
                        letter[0] = letter[0].replace("[name]", guest)
                with open(f"./Output/ReadyToSend/{guest}.txt", mode="a") as invite:
                    for line in letter:
                        invite.write(line)


