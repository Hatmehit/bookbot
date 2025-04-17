
from stats import get_num_words, get_count_characters, chars_dic_to_sorted_list
import sys






def get_book_text(filepath):

    with open (filepath) as f:
        
        file_contents = f.read()

        return(file_contents)

def main():

    if len(sys.argv) < 2:

        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
    
        filepath = sys.argv[1]
        file_contents = get_book_text(filepath)
        num_words = get_num_words(file_contents)
        chars_dict = get_count_characters(file_contents)
        chars_sorted_list = chars_dic_to_sorted_list(chars_dict)

        output(chars_sorted_list, num_words, filepath)

def output(chars_sorted_list, num_words, filepath):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char in chars_sorted_list:

        if char["char"].isalpha() == False:

            pass
        
        else:
            print(f"{char["char"]}: {char["num"]}")





    print("============= END ===============")

main()