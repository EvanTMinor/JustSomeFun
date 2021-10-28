# This is where random things will be made
from books_list import BooksList


class Tools:
    def seperate_books(self):
        booknum = 0

        infile = open(r"World_English_Bible/eng_web_word.txt", "r")
        lastcheck = open(r"World_English_Bible/eng_web_word.txt", "r")
        lines = lastcheck.readlines()
        last = lines[-1]

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
            if line == last:
                output[dicttitle] = linesofbook
        return output

    def create_books(self):
        dictionary = Tools.seperate_books(self)
        output = Tools.name_books(self, dictionary)
        for title, item in output.items():
            outputfile = "World_English_Bible/" + title + ".txt"
            with open(outputfile, "w") as outfile:
                for line in item:
                    outfile.write(line)
                    outfile.write("\n")
    
    def name_books(self, dictionary):
        books = BooksList.get_list(self)
        i = 0
        output = {}
        for title in dictionary:
            output[books[i]] = dictionary[title]
            i+=1
        return output

    def join_verse(self, book):
        book = "World_English_Bible/" + book + ".txt"
        past_title = False
        output = {}
        lines_of_verse = []
        current_verse = ""
        with open(book, "r") as book_file:
            for line in book_file:
                if "001:001" in line:
                    past_title = True
                if past_title == True:
                    if line != "\n":
                        if(line[3]==':'):
                            print(current_verse)
                            output[current_verse] = lines_of_verse
                            lines_of_verse = []
                            current_verse = line[0:7]
                            lines_of_verse.append(line)
                        else:
                                lines_of_verse.append(line)
                '''else:
                    if "Book" in line and past_title == False:
                        output[current_verse] = line'''
        outputfile = "linedverse.txt"
        with open(outputfile, "w") as outfile:
            for title, item in output.items():
                outfile.write(title)
                for line in item:
                    outfile.write(line)
                outfile.write("\n")
    