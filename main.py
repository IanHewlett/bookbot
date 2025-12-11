import sys
from stats import get_num_words, get_character_count, sort_dict

def get_book_text(path):
  with open(path) as f:
    return f.read()

def main():
  #print(get_book_text("books/frankenstein.txt"))
  #get_num_words(get_book_text("books/frankenstein.txt"))
  #get_character_count(get_book_text("books/frankenstein.txt"))
  #print(sort_dict(get_character_count(get_book_text("books/frankenstein.txt"))))

  #print(sys.argv)
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  #filepath = "books/frankenstein.txt"
  filepath = sys.argv[1]

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}...")
  print("----------- Word Count ----------")
  get_num_words(get_book_text(filepath))
  print("--------- Character Count -------")
  for entry in sort_dict(get_character_count(get_book_text(filepath))):
    if entry['char'].isalpha():
      print(f"{entry['char']}: {entry['num']}")
  print("============= END ===============")

main()
