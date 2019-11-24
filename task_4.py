import json


def search(file_name, *args):
    keywords = [arg for arg in args if arg[0] != '+' and arg[0] != '-']
    includes = [arg[1:] for arg in args if arg[0] == '+']
    excludes = [arg[1:] for arg in args if arg[0] == '-']

    db = open(file_name, 'r')
    for line in db:
        if all(keyword in line for keyword in keywords) and all(include in line for include in includes) and all(exclude not in line for exclude in excludes):
            yield json.loads(line)


# for recipe in search('20170107-061401-recipeitems.json', 'Fennel', '+mushrooms', '+butter', '+garlic'):
#     print(recipe)


def statistics(aggregate_function, data, property=None):
    lst = [x for x in data]
    return aggregate_function(lst, property)

# res = statistics(min, search('20170107-061401-recipeitems.json', 'Fennel', '+mushrooms', '+butter', '+garlic'), property=None)
# print(res)
