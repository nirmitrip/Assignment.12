from Ass12.handler import read_file, write_file

def borrow_book():
    book_id = input(" Book ID: ")
    member_id = input(" Member ID: ")

    # Check if the book is available and the member exists

    borrowed_data = f"{book_id},{member_id}\n"
    write_file("borrowed_books.txt", borrowed_data)
    print("Book borrowed")
def return_book():
    book_id = input(" Book ID: ")
    member_id = input(" Member ID: ")
    borrowed_books = read_file("borrowed_books.txt")
    updated_borrowed_books = []
    for borrowed_book in borrowed_books:
        if not borrowed_book.startswith(f"{book_id},{member_id}"):
            updated_borrowed_books.append(borrowed_book)
    write_file("borrowed_books.txt", updated_borrowed_books)
    print("Book returned")

def display_borrowed_books():
    borrowed_books = read_file("borrowed_books.txt")
    if borrowed_books:
        print("===== Borrowed Books =====")
        for borrowed_book in borrowed_books:
            book_id, member_id = borrowed_book.strip().split(",")
            print("Book ID:", book_id)
            print("Member ID:", member_id)
            print("********************")
    else:
        print("No books are borrowed!")