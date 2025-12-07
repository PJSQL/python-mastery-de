"""
Week 1 - Mini Project: Word Counter

Goal:
Write a script that:
- Reads a text file
- Normalizes the words (lowercase, strips punctuation)
- Counts how often each word appears
- Prints the top N most frequent words

Usage from the command line (once you have a file, e.g. sample.txt):

    python word_counter.py sample.txt 10
"""

import sys
from collections import Counter
from typing import List


def normalize_word(word: str) -> str:
    """
    Lowercase the word and strip common punctuation from the start and end.
    """
    return word.lower().strip(".,!?:;\"'()[]{}")


def read_words_from_file(path: str) -> List[str]:
    words: List[str] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            for raw_word in line.split():
                word = normalize_word(raw_word)
                if word:
                    words.append(word)
    return words


def count_words(words: List[str]) -> Counter:
    return Counter(words)


def print_top_n(counter: Counter, n: int = 10) -> None:
    print(f"Top {n} words:")
    for word, count in counter.most_common(n):
        print(f"{word:<20} {count}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python word_counter.py <file_path> [top_n]")
        sys.exit(1)

    file_path = sys.argv[1]
    top_n = 10

    if len(sys.argv) >= 3:
        try:
            top_n = int(sys.argv[2])
        except ValueError:
            print("top_n must be an integer. Using default 10.")

    words = read_words_from_file(file_path)
    counter = count_words(words)

    print(f"Total words: {sum(counter.values())}")
    print(f"Unique words: {len(counter)}")
    print()
    print_top_n(counter, top_n)


if __name__ == "__main__":
    main()

    # Self practice:
    # 1. Update normalize_word to also remove digits or keep only alphabetic characters.
    # 2. Add an option to ignore a list of stopwords like ["the", "and", "of"].
    # 3. Write the top N words and counts to a CSV file instead of just printing.
