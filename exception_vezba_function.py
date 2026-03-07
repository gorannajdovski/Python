import pathlib

def count_words(file):
    """Count the approximate number of words in a file."""
    try:
        contents = file.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {file} does not exist.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file} has about {num_words} words.")

filenames = ["text_files/duck.txt", "text_files/moby_dick.txt", "text_files/thumbelina.txt"]
for filename in filenames:
    file = pathlib.Path(filename)
    count_words(file)
