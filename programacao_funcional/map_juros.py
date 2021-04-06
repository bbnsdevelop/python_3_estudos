#!/usr/bin/python3
# coding: utf-8


def aplicar_multa(list_dict_book):
    list_with_juros = map(lambda book: (book['price'] + (book['price'] * (20 / 100)) if book['price'] >= 100 else book), list_dict_book)
    return list_with_juros


if __name__ == '__main__':
    books = [
        {"autor": "sammy", "price": 200, "tank number": 11, "type": "fish"},
        {"autor": "ashley", "price": 99, "tank number": 25, "type": "shellfish"},
        {"autor": "jo", "price": 150, "tank number": 18, "type": "fish"},
        {"autor": "jackie", "price": 80, "tank number": 21, "type": "shellfish"},
        {"autor": "charlie", "price": 500, "tank number": 12, "type": "fish"},
        {"autor": "olly", "price": 800, "tank number": 34, "type": "turtle"}
    ]
    books_juros = aplicar_multa(books)
    print(list(books_juros))