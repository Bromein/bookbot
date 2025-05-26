import sys
from stats import get_word_count, count_character_match, sorted_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents



def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) >= 2:
        my_book = get_book_text(sys.argv[1])
        word_length = get_word_count(my_book)

        print(f"Analyzing book found at books/{sys.argv[1]}")

        print("----------- Word Count ----------")
        print(f"Found {word_length} total words")

        print("--------- Character Count -------")
        sorted_char_count(count_character_match(my_book))

        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    


main()