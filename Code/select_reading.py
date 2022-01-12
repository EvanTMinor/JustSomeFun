class SelectReading():

    def __init__(self):
        book = SelectReading.select_book(self)
        selection = SelectReading.select_verse(self, book, "1:1")
        SelectReading.print_book(self, selection)

    
    def select_book(self):
        while(True):
            print("Would you like English or Greek")
            directory = input()
            print("What book would you like to read?")
            selection = input()
            if directory == "Greek":
                selection = "The_Greek_New_Testament/" + selection +".txt"
                return selection
            elif directory == "English":
                selection = "source/WEB_Lined_Verses/" + selection + ".txt"
                return selection
            else:
                print("Please input 'English' or 'Greek'")

    def get_book(self, book, greek=False):
        list = []
        with open(book, "r", encoding ="utf8") as book_file:
            for line in book_file:
                if line != "\n":
                    list.append(line)
        return list

    def print_book(self, book):
        for line in book:
            print(line)

    def select_verse(self, book, verse):
        output = []
        verse = SelectReading.parse_verse(self, verse)
        with open(book, "r", encoding ="utf8") as book_file:
            for line in book_file:
                if verse in line:
                    output.append(line)
                    break
        return(output)

    def parse_verse(self, verse, language):
        position = verse.index(':')
        first, last = verse[:position], verse[position+1:]
        if len(first)<3:
            for i in range (3-len(first)):
                first = "0" + first

        if len(last)<3:
            for i in range (3-len(last)):
                last = "0" + last

        verse = first + ":" + last
        return verse

        

SelectReading()