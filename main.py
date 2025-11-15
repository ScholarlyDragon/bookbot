#This file is the entry point to the program and includes any code that doesn't fit somewhere else.

import sys

from stats import get_book_text

from stats import count_words

from stats import count_and_sort_chars

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path_to_file = sys.argv[1]

    try:
        get_book_text(path_to_file)
    except FileNotFoundError:
        print(f"Error: file not found: {path_to_file}")
        sys.exit(1)
    except PermissionError:
        print(f"Error: permission denied: {path_to_file}")
        sys.exit(1)
    except OSError as e:
        print(f"Error: could not read '{path_to_file}': {e.strerror}")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    count_words(path_to_file)
    print("--------- Character Count -------")
    count_and_sort_chars(path_to_file)
    print("============= END ===============")

main()