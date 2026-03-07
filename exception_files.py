import pathlib
file = pathlib.Path("text_files/duck.txt")  
try:
    contents = file.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {file} does not exist.")
else:
    words = contents.split() # Pravi listu deleći kada naiđe na razmak
    num_words = len(words)
    print(f"The file {file} has about {num_words} words.")