class SelectReading():

    def __init__(self):
        book = SelectReading.select_book(self)
        book_eng = SelectReading.get_book(self, book, False)
        SelectReading.print_book(self, book_eng)

    
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

SelectReading()