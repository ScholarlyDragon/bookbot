#This file contains functions for analyzing the text.

path_to_file = "books/frankenstein.txt"

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    return text

def count_words():
    text = get_book_text(path_to_file)
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    print(f"Found {word_count} total words")
    return word_count

def count_chars():
    text = get_book_text(path_to_file)
    lowercase_text = text.lower()
    chars = list(lowercase_text)
    char_dict = {}
    for char in chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    print(char_dict)

