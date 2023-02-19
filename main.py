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
Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"] 
'''
#not used because i uderstood what it does only after figuring out how to do it my way.
#oops.


def find_mismatch(text):
    opening_brackets_stack = [] #opening brackets are placed in a stack
    pairsdictionary = { 
        ")":"(",
        "]":"(",        #dictionary that provides the asymmetrical opposite to each opening bracket
        "}":"{"
    }
    global borat        #borat will tell us whether everything checks out
    borat = False   
    for i, next in enumerate(text):
        
        if next in "([{": # Process opening bracket
            opening_brackets_stack.append(next) #place opening bracket in stack
            
            
        if next in ")]}": # Process closing bracket  
            if next == ")":
                for j, next in enumerate(reversed(opening_brackets_stack)): 
                    checkbracketfromstack = opening_brackets_stack[j]
                    if checkbracketfromstack == pairsdictionary[")"]:
                        opening_brackets_stack.pop(j)
                        break
                    borat = False
                    return
                    
            
            elif next == "]":
                for j, next in enumerate(reversed(opening_brackets_stack)): 
                    checkbracketfromstack = opening_brackets_stack[j]
                    if checkbracketfromstack == pairsdictionary["]"]:
                        opening_brackets_stack.pop(j)
                        break
                    borat = False
                    return
                    

            elif next == "}":
                for j, next in enumerate(reversed(opening_brackets_stack)): 
                    checkbracketfromstack = opening_brackets_stack[j]
                    if checkbracketfromstack == pairsdictionary["}"]:
                        opening_brackets_stack.pop(j)
                        break
                    borat = False
                    return

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