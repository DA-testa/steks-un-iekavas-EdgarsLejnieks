# python3
# 221RDB168 Edgars Lejnieks 7. grupa

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"]) #array, but cooler (actually a type apparently)

def find_mismatch(text):
    global opening_brackets_stack
    opening_brackets_stack = [] #opening brackets are placed in a stack
    
    pairsdictionary = { 
        ")":"(",
        "]":"[",        #dictionary that provides the horizontal opposite to each opening bracket
        "}":"{"
    }
    
    
    global check        #check will tell us whether brackets are matched
    check = False
    
    global index        #index will tell us positions and stuff
    for index, next in enumerate(text):
        
        if next in "([{": # Process opening bracket
            opening_brackets_stack.append(Bracket(next, index)) #place opening bracket in stack
            
        
        if next in ")]}": # Process closing bracket  
            cont = False
            
            if next == ")":
                stacklenght = len(opening_brackets_stack) - 1
                if stacklenght < 0:
                    check = False
                    #return index + 1
                checkbracketfromstack = opening_brackets_stack[stacklenght]
                if checkbracketfromstack[0] == pairsdictionary[")"]:
                        opening_brackets_stack.pop(stacklenght)
                        cont = True
                if cont == False:
                    check = False
                    return checkbracketfromstack[1] + 1
                
            if next == "]":
                stacklenght = len(opening_brackets_stack) - 1
                if stacklenght < 0:
                    check = False
                    #return index + 1
                checkbracketfromstack = opening_brackets_stack[stacklenght]
                if checkbracketfromstack[0] == pairsdictionary["]"]:
                        opening_brackets_stack.pop(stacklenght)
                        cont = True
                if cont == False:
                    check = False
                    return checkbracketfromstack[1] + 1
            
            if next == "}":
                stacklenght = len(opening_brackets_stack) - 1
                if stacklenght < 0:
                    check = False
                    #return index + 1
                checkbracketfromstack = opening_brackets_stack[stacklenght]
                if checkbracketfromstack[0] == pairsdictionary["}"]:
                        opening_brackets_stack.pop(stacklenght)
                        cont = True
                if cont == False:
                    check = False
                    return checkbracketfromstack[1] + 1

    if len(opening_brackets_stack) == 0: 
        check = True

def main():
    print("Manual Input: I, File input: F ")
    print("Select input type:")
    inputtype = input()
    if inputtype == "I":
        print("Input text (preferably with brackets): ")
        text = input()
        result = find_mismatch(text)
    elif inputtype == "F":
        print("Input file (location, name and type): ")
        filepath = input()
        file = open(filepath, "r")
        text = file.read()
        result = find_mismatch(text)
    
    
    # Printing answer ---------------------
    if check == True:
        print("Success")
    else:
        if len(opening_brackets_stack) == 0:
            print(result)
        else:
            print(opening_brackets_stack[0][1]+1)
            
            
        #print("Unmatched brackets")
        
        

if __name__ == "__main__":
    main()
    
# Unfinished: 
#   Indexing