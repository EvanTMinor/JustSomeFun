# This is where random things will be made
from books_list import BooksList
import os


class Tools:
    def seperate_books(self):
        booknum = 0

        infile = open(r"source/eng_web_word.txt", "r")
        lastcheck = open(r"source/eng_web_word.txt", "r")
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

    def create_books(self, outputfile):
        dictionary = Tools.seperate_books(self)
        output = Tools.name_books(self, dictionary)
        for title, item in output.items():
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

    def join_book_verse(self, file_name, file_path, output_location):
        past_title = False
        title = True
        output = {}
        lines_of_verse = []
        current_verse = ""
        with open(file_path, "r") as book_file:
            for line in book_file:
                line = Tools.remove_unneeded_data(self, line)
                if "001:001" in line:
                    past_title = True
                if past_title == True:
                    if line != "\n":
                        if(len(line) >= 3 and line[3]==':'):
                            output[current_verse] = lines_of_verse
                            lines_of_verse = []
                            current_verse = line[0:7]
                            lines_of_verse.append(line)
                        else:
                                lines_of_verse.append(line)
                                output[current_verse] = lines_of_verse
                else:
                    if title == True:
                        title = False
                        output["title"] = line
        outputfile = output_location + file_name
        with open(outputfile, "w") as outfile:
            for title, item in output.items():
                for line in item:
                    outfile.write(line)
                outfile.write("\n")

    def remove_unneeded_data(self, line):
        line = line.replace("      ", "")
        line = line.replace("\n","")
        return line

    def run_all_folder_files(self, folder):
        #Makes a list of all files in folder
        a_directory = folder
        for filename in os.listdir(a_directory):
            filepath = os.path.join(a_directory, filename)
            Tools.join_book_verse(self, filename, filepath, "source/WEB_Lined_Verses/")
    