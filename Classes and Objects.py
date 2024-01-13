#Classes and Objects:

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def set_information(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_information(self):
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Genre: " + self.genre)

# Creating an instance of the Book class
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy")

# Displaying information about the book
book1.display_information()

