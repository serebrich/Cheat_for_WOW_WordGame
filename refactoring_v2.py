import itertools
import functools
from datetime import datetime

words = input('Input all words in game\n')
start_time = datetime.now()

final_words = []

def str_combination(word):
    for n in range(3, len(word) + 1):
        yield from map(functools.partial(str.join, ''), itertools.permutations(word, n))

with open('Slovar.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    data = set(data.split())
    final_words = data.intersection(str_combination(words))

for position, word in enumerate(set(final_words), start=1):
    print(f'{position}. {word}')

print(datetime.now() - start_time)