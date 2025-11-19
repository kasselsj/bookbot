import sys
from stats import get_num_words, count_chars, chars_dict_to_sorted_list

if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

book_path = sys.argv[1]

def get_book_text(path):
    with open(path, "r") as f:
        return f.read()

def main():
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)

    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_freq = count_chars(text)
    sorted_chars = chars_dict_to_sorted_list(char_freq)
    
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ================")

main()
