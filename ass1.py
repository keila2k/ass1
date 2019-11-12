# p1.1
def p_1_1_lc(inputlist):
    return [item*2 + 1 for item in inputlist]


print(p_1_1_lc([0, 1, 2, 3]))


def p_1_1_fp(inputlist):
    return list(map(lambda item: item*2 + 1, inputlist))


print(p_1_1_fp([0, 1, 2, 3]))

# p1.2


def p_1_2_lc(inputlist):
    return [item % 3 == 0 for item in inputlist]


print(p_1_2_lc([3, 5, 9, 8]))


def p_1_2_fp(inputlist):
    return list(map(lambda item: item % 3 == 0, inputlist))


print(p_1_2_fp([3, 5, 9, 8]))


# p1.3

def p_1_3_lc(inputlist):
    return [item**2 for item in inputlist]


print(p_1_3_lc([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


def p_1_3_fp(inputlist):
    return list(map(lambda item: item ** 2, inputlist))


print(p_1_3_fp([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

# p1.4


def p_1_4_lc(inputlist):
    return [item[0].upper() for item in inputlist]


print(p_1_4_lc(['apple', 'orange', 'pear']))


def p_1_4_fp(inputlist):
    return list(map(lambda item: item[0].upper(), inputlist))


print(p_1_4_fp(['apple', 'orange', 'pear']))

# p1.5
test = ['apple', 'orange', 'pear']


def p_1_5_lc(inputlist):
    return [inputlist[0], inputlist[-1]]


def p_1_5_fp(inputlist):
    return list(filter(lambda item: inputlist.index(item) == 0 or inputlist.index(item) == len(inputlist) - 1, inputlist))


print(p_1_5_lc(test))
print(p_1_5_fp(test))


# p1.6

def p_1_6_lc(inputlist):
    return [(item, len(item)) for item in inputlist]


def p_1_6_fp(inputlist):
    return list(map(lambda item: (item, len(item)), inputlist))


print(p_1_6_lc(test))
print(p_1_6_fp(test))

# p1.7


def p_1_7_lc(inputlist):
    return [item for item in inputlist if item % 2 == 1]


def p_1_7_fp(inputlist):
    return list(filter(lambda item: item % 2 == 1, inputlist))


print(p_1_7_lc([0, 1, 2, 3, 4, 5, 6, 8]))
print(p_1_7_fp([0, 1, 2, 3, 4, 5, 6, 8]))

# p1.8


def p_1_8_lc(inputlist):
    return [item for idx, item in enumerate(inputlist) if idx % 2 == 0]


def p_1_8_fp(inputlist):
    return list(filter(lambda item: inputlist.index(item) % 2 == 0, inputlist))


print(p_1_8_lc([1, 2, 4, 5, 7]))
print(p_1_8_fp([1, 2, 4, 5, 7]))
