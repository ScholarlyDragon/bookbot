#This file is the entry point to the program and includes any code that doesn't fit somewhere else.
 
from stats import count_words

from stats import path_to_file

from stats import count_and_sort_chars

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path_to_file}...")
print("----------- Word Count ----------")
count_words()
print("--------- Character Count -------")
count_and_sort_chars()
print("============= END ===============")