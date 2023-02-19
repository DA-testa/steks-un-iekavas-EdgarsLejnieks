# python3
# 221RDB168 Edgars Lejnieks 7. grupa

"""
First priority is to find the first unmatched closing bracket which either doesn’t 
have an opening bracket before it, like ] in ](), 
or closes the wrong opening bracket, like } in ()[}

If there are no such mistakes, then it should 
find the first unmatched opening bracket without the 
corresponding closing bracket after it, like ( in {}([].

all brackets in the code should be divided into pairs of matching brackets, 
such that in each pair the opening bracket goes before the closing bracket, 
and for any two pairs of brackets either one of them is nested inside 
another one as in (foo[bar]) or they are separate as in f(a,b)-g[c]. 
The bracket [ corresponds to the bracket ], { corresponds to }, and ( corresponds to ).

 Input contains one string 𝑆 which consists of big and small latin letters, digits, 
 punctuation marks and brackets from the set []{}(). 
 
 Constraints: The length of 𝑆 is at least 1 and at most 105. 
 Output Format: If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes). 
 Otherwise, output the 1-based index of the first unmatched closing bracket,
 if there are no unmatched closing brackets, output the 1-based index of the first unmatched opening bracket.
"""

from collections import namedtuple

'''
Bracket = namedtuple("Bracket", ["char", "position"]) #kautkāds masīvs laikam


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"] 
'''
#not used


def find_mismatch(text):
    opening_brackets_stack = [] #opening brackets are placed here
    global borat
    borat = False
    for i, next in enumerate(text):
        if next in "([{": # Process opening bracket
            
            opening_brackets_stack.append(next) #ievietoju atvērto iekavu šeit (cerams)

        if next in ")]}": # Process closing bracket
            stacksize = len(opening_brackets_stack) #get stack size
            for j, next in enumerate(reversed(opening_brackets_stack)): #bug fixed (wrong type of indices)
                active = opening_brackets_stack[j]
                if next == active:
                    opening_brackets_stack.pop(j)
                    break
    if len(opening_brackets_stack) == 0: 
        borat = True
        


def main():
    print("Input text (preferably with brackets): ")
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer ---------------------
    if borat == True:
        print("Success")
    else:
        print("uh oh")
        
    # TODO: make this return position of error


if __name__ == "__main__":
    main()

#current bugs
# ()) <- success
# {) <- success