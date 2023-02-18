# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"]) #kautkāds masīvs laikam

'''
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"] 
'''
#man nav ne jausmas kas šis ir ^^^^^

# 'pass' novērš tukšas funkcijas kļūdu vai kautkas tamlīdzīgs... ?


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
