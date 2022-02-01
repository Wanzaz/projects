from tests import tests, test

# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

# PROBLEM: We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3


def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

result = locate_card_linear(test['input']['cards'], test['input']['query'])
print(result)
#print(tests)
