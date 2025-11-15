#This file contains functions for analyzing the text.

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    return text

def count_words(path_to_file):
    text = get_book_text(path_to_file)
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    print(f"Found {word_count} total words")

#This function counts the characters in the path_to_file and returns a dictionary
#This is irrelevant now that count_and_sort_chars exists
def count_chars(path_to_file):
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
    return char_dict


#This function counts the characters in the path_to_file and returns a list of sorted dicts
#It also prints the values of each dict
def count_and_sort_chars (path_to_file):
    text = get_book_text(path_to_file)
    lowercase_text = text.lower()
    chars = list(lowercase_text)
    char_dict = {}
    for char in chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    list_of_dicts = []
    for char in char_dict:
        new_dict = {"char":char, "num":char_dict[char]}
        list_of_dicts.append(new_dict)
    
    def sort_on(new_dict):
        return new_dict["num"]
    
    list_of_dicts.sort(reverse=True, key=sort_on)

    for item in list_of_dicts:
        var = item["char"]
        if var.isalpha():
            print(f'{item["char"]}: {item["num"]}')

    return list_of_dicts
    