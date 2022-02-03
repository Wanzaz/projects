"""
A list of size 10 rotated 3 times.
A list of size 8 rotated 5 times.
A list that wasn't rotated at all.
A list that was rotated just once.
A list that was rotated n-1 times, where n is the size of the list.
A list that was rotated n times (do you get back the original list here?)
An empty list.
A list containing just one element.
"""

test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

# A list of size 8 rotated 5 times.
test1 = {
    'input': {
        'nums': [4, 5, 6, 7, 8, 1, 2, 3]
    },
    'output': 5
}

# A list that wasn't rotated at all.
test2 = {
    'input': {
        'nums': [1, 2, 3, 4, 5, 6, 7, 8]
    },
    'output': 0
}

# A list that was rotated just once.
test3 = {
    'input': {
        'nums': [2, 3, 4, 5, 6, 7, 8, 1]
    },
    'output': 1
}

# A list that was rotated n-1 times, where n is the size of the list.
test4 = {
    'input': {
        'nums': [2, 3, 4, 5, 6, 7, 8, 1]
    },
    'output': 7
}

# A list that was rotated n times, where n is the size of the list
test5 = {
    'input': {
        'nums': [3, 5, 7, 8, 9, 10]
    },
    'output': 0
}

# An empty list.
test6 = {
    'input': {
        'nums': []
    },
    'output': 0
}

# A list containing just one element.
test7 = {
    'input': {
        'nums': [1]
    },
    'output': 0
}

tests = [test, test1, test2, test3, test3, test5, test6, test7]
