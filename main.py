from stats import get_num_words
from stats import sort_dict
from stats import get_num_char

def main():
    book_path ="books/frankenstein.txt" 
    file_contents = get_book_text(book_path)
    print_report(book_path, file_contents)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def print_report(book_path, file_contents):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_contents)} total words")
    print("--------- Character Count -------")
    for key, value in sort_dict(get_num_char(file_contents)).items():
        print(f"{key}: {value}")
    print("============= END ===============")    

main()