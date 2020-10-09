import itertools
import functools


def letters_2_words(letters: str) -> set:
    final_words = []

    def str_combination(word):
        for n in range(3, len(word) + 1):
            yield from map(
                functools.partial(str.join, ""), itertools.permutations(word, n)
            )

    with open("Slovar.txt", "r", encoding="utf-8") as file:
        data = set(file.read().split())
        final_words = data.intersection(str_combination(letters))

    return final_words
