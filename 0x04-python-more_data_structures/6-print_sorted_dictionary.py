def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    n = len(keys)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if keys[j] > keys[j + 1]:
                keys[j], keys[j + 1] = keys[j + 1], keys[j]

    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
