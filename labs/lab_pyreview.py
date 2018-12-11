#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from string import ascii_lowercase


"""

:mod:`lab_pyreview` -- Python review
=========================================

LAB PyReview Learning Objective: Review the topics from the previous courses

a. Load the data from the two dictionary files in the data directory into two
   list objects.  data/dictionary1.txt data/dictionary2.txt
   Print the number of entries in each list of words from the dictionary files.

b. Use sets in Python to merge the two lists of words with no duplications (union).
   Print the number of words in the combined list.

c. Import the random library and use one of the functions to print out five random
   words from the combined list of words.

d. Use a list comprehension to find all the words that start with the letter 'a'.
   Print the number of words that begin with the letter 'a'.

e. Create a function called wordcount() with a yield that takes the list of
   all words as an argument and yields a tuple of
   (letter, number_of_words_starting_with_that_letter) with each iteration.

"""


def file_to_list(filepath):
    with open(filepath) as f:
        return [x.strip("\n") for x in f.readlines()]


def print_step(step_name):
    print()
    print(f"**** Step {step_name} ****")
    print()


def print_len(label, item):
    print(f"{label}: {len(item)} items long.")


def print_lens(*items):
    for idx, item in enumerate(items, start=1):
        print_len(f"List {idx}", item)


def list_union(list_a, list_b):
    return list(set(list_a).union(list_b))


def words_starting_with(target_letter, list_of_words):
    return [x for x in list_of_words if x.startswith(target_letter)]


def wordcount(list_of_words):
    for letter in ascii_lowercase:
        yield (letter, len(words_starting_with(letter, list_of_words)))


def main():
    a = file_to_list("data/dictionary1.txt")
    b = file_to_list("data/dictionary2.txt")

    # Step A
    print_step("A")
    print_lens(a, b)

    # Step B
    print_step("B")
    combined = list_union(a, b)
    print_len("Combined List", combined)

    # Step C
    print_step("C")
    for word in random.sample(combined, 5):
        print(word)

    # Step D
    print_step("D")
    print_len("Words starting with 'a'", words_starting_with("a", combined))

    # Step E
    print_step("E")
    for letter, count in wordcount(combined):
        print(f"Words starting with '{letter}': {count}")


if __name__ == "__main__":
    main()
