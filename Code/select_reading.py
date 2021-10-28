class SelectReading():

    def run(self):
        book = SelectReading.select_book(self)
        book_eng = SelectReading.get_book(self, book, False)
        SelectReading.print_book(self, book_eng)

    
    def select_book(self):
        print("What book would you like to read?")
        selection = input()
        return selection

    def get_book(self, book, greek=False):
        list = []
        if greek == True:
            book = "The_Greek_New_Testament/" + book + ".txt"
            with open(book, "r", encoding ="utf8") as book_file:
                for line in book_file:
                    if line != "\n":
                        list.append(line)
        else:
            book = "World_English_Bible/" + book + ".txt"
            with open(book, "r") as book_file:
                for line in book_file:
                    if line != "\n":
                        list.append(line)
        return list

    def print_book(self, book):
        for line in book:
            print(line)