#|= This modifies dict1 directly
dict1 = {'a': 1}
dict2 = {'b': 2}
dict1 |= dict2
print(dict1)