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

