from itertools import permutations


def convertTuple(tup):
    str = ''.join(tup)
    return str


words = input('Input all words in game\n')

set1 = words
set2 = words
set3 = words
set4 = words
set5 = words
mutabel_set1 = None
mutabel_set2 = None
mutabel_set3 = None
mutabel_set4 = None
mutabel_set5 = None

final_list = []
final_words = []

if len(words) == 3:
    mutabel_set1 = permutations(list(set1))
if len(words) == 4:
    mutabel_set1 = permutations(list(set1), r=3)
    mutabel_set2 = permutations(list(set2), r=4)

if len(words) == 5:
    mutabel_set1 = permutations(list(set1), r=3)
    mutabel_set2 = permutations(list(set2), r=4)
    mutabel_set3 = permutations(list(set3), r=5)
if len(words) == 6:
    mutabel_set1 = permutations(list(set1), r=3)
    mutabel_set2 = permutations(list(set2), r=4)
    mutabel_set3 = permutations(list(set3), r=5)
    mutabel_set4 = permutations(list(set4), r=6)

if len(words) == 7:
    mutabel_set1 = permutations(list(set1), r=3)
    mutabel_set2 = permutations(list(set2), r=4)
    mutabel_set3 = permutations(list(set3), r=5)
    mutabel_set4 = permutations(list(set4), r=6)
    mutabel_set5 = permutations(list(set5), r=7)

if mutabel_set1 != None:
    for h in mutabel_set1:
        string = convertTuple(h)
        final_list.append(string)
if mutabel_set2 != None:
    for h in mutabel_set2:
        string = convertTuple(h)
        final_list.append(string)
if mutabel_set3 != None:
    for h in mutabel_set3:
        string = convertTuple(h)
        final_list.append(string)
if mutabel_set4 != None:
    for h in mutabel_set4:
        string = convertTuple(h)
        final_list.append(string)
if mutabel_set5 != None:
    for h in mutabel_set5:
        string = convertTuple(h)
        final_list.append(string)

file = open('Slovar.txt', 'r')
data = file.read()
data = list(data.split())

for word in final_list:
    if word in data:
        final_words.append(word)
file.close()

num = 1
for enum in set(final_words):
    print(str(num) + '. ' + str(enum))
    num+=1
