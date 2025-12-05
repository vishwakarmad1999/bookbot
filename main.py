from stats import get_num_words, get_sorted_chars_list
from sys import argv, exit


def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    print("============ BOOKBOT ============")
    path = argv[1]
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(path)} total words")
    print("--------- Character Count -------")
    chars_list = get_sorted_chars_list(path)
    for el in chars_list:
        if not el["char"].isalpha():
            continue
        print(f"{el["char"]}: {el["num"]}")
    print("============= END ===============")


main()
