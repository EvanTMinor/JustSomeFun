# This is where random things will be made


class Tools:
    def seperate_books(self):
        booknum = 0

        infile = open(r"eng_web_word.txt", "r")
        stopline = "Book 0"
        dicttitle = "Book 1"
        output = {}
        linesofbook = []
        bookstracker = 0
        divisible = 1

        for line in infile:
            if stopline in line:
                print(line)
                output[dicttitle] = linesofbook
                linesofbook = []
                booknum = booknum + 1
                print(booknum)
                if booknum % 10 == divisible:
                    divisible = bookstracker - 1
                    bookstracker = bookstracker + 1
                    num = str(bookstracker)
                    stopline = "Book " + num
                num = str(booknum)
                dicttitle = "Book 0" + num
            linesofbook.append(line)

        for title, item in output.items():
            outputfile = title + ".txt"
            with open(outputfile, "w") as outfile:
                for line in item:
                    outfile.write(line)
                    outfile.write("\n")
