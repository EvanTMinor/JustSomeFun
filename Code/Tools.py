# This is where random things will be made


class Tools:
    def seperate_books(self):
        booknum = 0

        infile = open(r"eng_web_word.txt", "r")
        dicttitle = "Book 0"
        title = "Book 0"
        output = {}
        linesofbook = []
        booktracker = 1

        for line in infile:
            if title in line:
                output[dicttitle] = linesofbook
                linesofbook = []
                booknum = booknum + 1
                num = str(booknum)
                booktracker = booknum + 1
                tracknum = str(booktracker)
                if booknum >= 10:
                    dicttitle = "Book " + num
                else:
                    dicttitle = "Book 0" + num
                if booktracker >= 10:
                    title = "Book " + tracknum
                else:
                    title = "Book 0" + tracknum
            linesofbook.append(line)

        for title, item in output.items():
            print(title)
        for title, item in output.items():
            outputfile = title + ".txt"
            with open(outputfile, "w") as outfile:
                for line in item:
                    outfile.write(line)
                    outfile.write("\n")
