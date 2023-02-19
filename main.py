# python3
# 221RDB168 Edgars Lejnieks 7. grupa

from collections import namedtuple

def find_mismatch(text):
    
    opening_brackets_stack = [] #opening brackets are placed in a stack
    
    pairsdictionary = { 
        ")":"(",
        "]":"[",        #dictionary that provides the asymmetrical opposite to each opening bracket
        "}":"{"
    }
    
    
    global check        #check will tell us whether brackets are matched
    check = False
    
    global index        #index will tell us which bracket is unopened or unmatched(not closed)
    for index, next in enumerate(text):
        
        if next in "([{": # Process opening bracket
            opening_brackets_stack.append(next) #place opening bracket in stack
            
        
        if next in ")]}": # Process closing bracket  
            cont = False
            
            if next == ")":
                stacklenght = len(opening_brackets_stack) - 1
                checkbracketfromstack = opening_brackets_stack[stacklenght]
                if checkbracketfromstack == pairsdictionary[")"]:
                        opening_brackets_stack.pop(stacklenght)
                        cont = True
                if cont == False:
                    check = False
                    return
                
            if next == "]":
                stacklenght = len(opening_brackets_stack) - 1
                checkbracketfromstack = opening_brackets_stack[stacklenght]
                if checkbracketfromstack == pairsdictionary["]"]:
                        opening_brackets_stack.pop(stacklenght)
                        cont = True
                if cont == False:
                    check = False
                    return
            
            if next == "}":
                stacklenght = len(opening_brackets_stack) - 1
                checkbracketfromstack = opening_brackets_stack[stacklenght]
                if checkbracketfromstack == pairsdictionary["}"]:
                        opening_brackets_stack.pop(stacklenght)
                        cont = True
                if cont == False:
                    check = False
                    return

    if len(opening_brackets_stack) == 0: 
        check = True

def main():
    print("Input text (preferably with brackets): ")
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer ---------------------
    if check == True:
        print("Success")
    else:
        print("Unmatched brackets")

if __name__ == "__main__":
    main()
    
# Unfinished: Indexing