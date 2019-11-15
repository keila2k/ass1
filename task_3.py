import itertools


def generate_n_grams(size, words_list):
    i = 0
    while i < len(words_list)-2:
        yield words_list[i:i+3]
        i += 1


sentence = "the quick red fox jumps over the lazy brown dog"
# <generator object ngrams at 0x109a36ca8>
print(generate_n_grams(3, sentence))
for x in generate_n_grams(3, sentence.split()):
    print(x)


def generate_sentence(subjects, verbs, objects):
    min_length = min(len(subjects), len(verbs), len(objects))

    i = 0
    while i < min_length:
        yield ' '.join([subjects[i], verbs[i], objects[i]])
        i += 1


subjects = ["I", "You"]
verbs = ["play", "love"]
objects = ["Basketball", "Football"]
for sentence in generate_sentence(subjects, verbs, objects):
    print(sentence)


def generate_permutations(some_list):
    if len(some_list) <= 1:
        yield tuple(some_list)
    else:
        for permutation in generate_permutations(some_list[1:]):
            for i in range(len(some_list)):
                yield tuple(list(permutation[:i]) + list(some_list[0:1]) + list(permutation[i:]))


some_list = [1, 2, 3]
for perm in generate_permutations(some_list):
    print(perm)
