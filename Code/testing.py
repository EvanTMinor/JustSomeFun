#This is where random things will be made

class Testing:

    def edit_character(character):
        with open(r'eng_web_word.txt', 'r') as infile, \
            open(r'word.txt', 'w') as outfile:
            data = infile.read()
            data = data.replace(character, "")
            outfile.write(data)
