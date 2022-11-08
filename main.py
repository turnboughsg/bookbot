from collections import defaultdict


class BookBot:
    def __init__(self, filepath):
        self.filepath = filepath
        self.letter_counts = defaultdict(int)

    def read_text(self):
        # reads the file and returns the text as a string
        with open(self.filepath) as f:
            self.text = f.read()
            return self.text

    def count_words(self):
        # returns the number of words in the text
        return len(self.text.split())

    def count_letters(self):
        # returns a dictionary with the count of each letter in the text
        for letter in self.text.lower():
            if letter.isalpha():
                self.letter_counts[letter] = self.letter_counts.get(
                    letter, 0) + 1
        return self.letter_counts

    def print_report(self):
        self.read_text()
        # print report of the text
        print(f"--- Begin report of {self.filepath} ---")
        print(f"\n Number of words found in document: {self.count_words()} \n")

        # sort the dictionary by key
        letter_keys_sorted = sorted([key for key in self.letter_counts.keys()])
        for key in letter_keys_sorted:
            print(
                f"The {key} character was found {self.letter_counts[key]} times.")

        print(f"\n --- End report of {self.filepath} --- \n")


def main():
    # create an instance of the BookBot class
    frankenstein = BookBot("./books/frankenstein.txt")
    frankenstein.print_report()


if __name__ == "__main__":
    main()
