import collections
import sys

def find_unpopular_books(book_list):
    if not book_list:
        return []

    book_counts = collections.Counter(book_list)
    min_frequency = min(book_counts.values())

    unpopular_books = []
    for book, count in book_counts.items():
        if count == min_frequency:
            unpopular_books.append(book)

    unpopular_books.sort()
    return unpopular_books

if __name__ == "__main__":
    input_books = []
    for line in sys.stdin:
        book_title = line.strip()
        if book_title:
            input_books.append(book_title)

    result = find_unpopular_books(input_books)

    for book in result:
        print(book)