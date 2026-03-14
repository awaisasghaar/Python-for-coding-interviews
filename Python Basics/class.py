# class of a Book
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def book_name(self):
        name = input("What's your name: ")
        print(f'Welcome, {name}')
        return f'\nThe title of the book is {self.title}'

    def book_pages(self, page):
        pages = page * 1
        return f'The total of number of pages in {self.title } is {pages}'
    
    @classmethod
    def chapter(cls, book):
        a = int(input(f"\nHow many chapters are there in {book}: "))
        return f'There are {a} chapters in {book}'


if __name__ == '__main__':
   book = Book('Atomic Habits', 305)
   print(book.book_name())
   print(book.book_pages(305))
   print(book.chapter('Atomic Habits'))