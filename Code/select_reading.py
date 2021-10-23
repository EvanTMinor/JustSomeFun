class SelectReading():
    
    def select_book(self):
        print("What book would you like to read?")
        selection = input()
        book = "World_english_Bible/" + selection + ".txt"
        with open(book, "r") as book_file:
            for line in book_file:
                if line != "\n":
                    print(line)